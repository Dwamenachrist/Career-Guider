from experta import Fact, KnowledgeEngine, Rule, Field, MATCH


class Skill(Fact):
    name = Field(str)

class Interest(Fact):
    name = Field(str)

class Education(Fact):
    level = Field(str)

class Career(Fact):
    title = Field(str)
    description = Field(str)
    qualifications = Field(str)


class CareerAdvisor(KnowledgeEngine):

    @Rule(Skill(name='programming') & Skill(name='problem-solving') &
          Interest(name='technology') & Education(level="Bachelor's Degree"))
    def recommend_software_developer(self):
        self.declare(Career(
            title="Software Developer",
            description="Develops software applications and systems. Designs, codes, and tests software.",
            qualifications="Strong programming skills, problem-solving abilities, knowledge of data structures and algorithms"
        ))

    @Rule(Skill(name='statistics') & Skill(name='machine-learning') &
          Skill(name='programming') & Interest(name='science') &
          Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_data_scientist(self):
        self.declare(Career(
            title="Data Scientist",
            description="Analyzes large datasets to extract meaningful insights and build predictive models.",
            qualifications="Statistics, Machine Learning, Programming, Data Visualization"
        ))

    # Add more rules as needed

    @Rule(Career(title=MATCH.title, description=MATCH.description, qualifications=MATCH.qualifications))
    def display_recommendation(self, title, description, qualifications):
        print(f"Recommended Career: {title}")
        print(f"Description: {description}")
        print(f"Qualifications: {qualifications}\n")
