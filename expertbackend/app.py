from flask import Flask, request, jsonify
from flask_cors import CORS
from experta import Fact
from knowledge import Career, Skill, Interest, Education, CareerAdvisor    # Adjust the import as needed

app = Flask(__name__)
CORS(app)

@app.route('/api/recommendations', methods=['POST'])
def get_career_recommendations():
    data = request.get_json()
    skills = data.get('skills', [])
    interests = data.get('interests', [])
    education = data.get('education', '')

    engine = CareerAdvisor()

    # Reset the engine to clear any previous facts
    engine.reset()

    # Assert education fact
    engine.declare(Education(level=education))

    # Assert skill facts
    for skill in skills:
        engine.declare(Skill(name=skill))

    # Assert interest facts
    for interest in interests:
        engine.declare(Interest(name=interest))

    # Run the engine
    engine.run()

    # Collect recommendations
    recommendations = []
    for fact in engine.facts.values():
        if isinstance(fact, Career):
            recommendations.append({
                "title": fact['title'],
                "description": fact['description'],
                "qualifications": fact['qualifications']
            })

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
