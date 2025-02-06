from flask import Flask, request, jsonify
from flask_cors import CORS
import clips

app = Flask(__name__)
CORS(app)
@app.route('/api/recommendations', methods=['POST'])
def get_career_recommendations():
    data = request.get_json()
    skills = data.get('skills', [])
    interests = data.get('interests', [])
    education = data.get('education', '')

    clips_env = clips.Environment()

    try:
        clips_env.load("career_advisor.clp")

        # Clear existing facts (very important)

        clips_env.assert_string(f"(education (level \"{education}\"))")
        # Add the list
        for skill in skills:
            clips_env.assert_string(f"(skill (name \"{skill}\"))")

        for interest in interests:
            clips_env.assert_string(f"(interest (name \"{interest}\"))")

        clips_env.assert_string("(initial-fact)")
        clips_env.run()

        recommendations = []
        for fact in clips_env.facts():
            if fact.template.name == 'career':
                recommendations.append({
                    "title": fact['title'],
                    "description": fact['description'],
                    "qualifications": fact['qualifications']
                })

        return jsonify(recommendations)
    except clips.CLIPSError as e:
        print("CLIPS error:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        clips_env.clear()  # Clean up the clips environment to avoid memory problems

if __name__ == '__main__':
    app.run(debug=True, port=5000)