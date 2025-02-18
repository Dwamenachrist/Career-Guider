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

    @Rule(Skill(name='communication') & Skill(name='leadership') &
      Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_project_manager(self):
        self.declare(Career(
            title="Project Manager",
            description="Plans, organizes, and oversees the completion of projects, ensuring they are on time and within budget.",
            qualifications="Strong communication, leadership, and organizational skills. Knowledge of project management methodologies."
        ))

    @Rule(Skill(name='writing') & Skill(name='editing') &
      Interest(name='communication') & Education(level="Bachelor's Degree"))
    def recommend_content_writer(self):
        self.declare(Career(
            title="Content Writer",
            description="Creates written content for various platforms, including websites, blogs, and social media.",
            qualifications="Excellent writing and editing skills. Understanding of SEO and content marketing principles."
        ))

    @Rule(Skill(name='accounting') & Skill(name='finance') &
      Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_accountant(self):
        self.declare(Career(
            title="Accountant",
            description="Manages financial records, prepares financial statements, and ensures compliance with tax regulations.",
            qualifications="Knowledge of accounting principles and practices. Attention to detail and analytical skills."
        ))

    @Rule(Skill(name='design') & Skill(name='creativity') &
      Interest(name='art') & Education(level="Bachelor's Degree"))
    def recommend_graphic_designer(self):
        self.declare(Career(
            title="Graphic Designer",
            description="Creates visual designs for various media, including websites, logos, and marketing materials.",
            qualifications="Strong design skills and creativity. Proficiency in design software."
        ))

    @Rule(Skill(name='customer service') & Skill(name='communication') &
      Interest(name='helping others') & Education(level="High School Diploma"))
    def recommend_customer_service_representative(self):
        self.declare(Career(
            title="Customer Service Representative",
            description="Provides support to customers, answering questions and resolving issues.",
            qualifications="Excellent communication and customer service skills. Patience and problem-solving abilities."
        ))

    @Rule(Skill(name='nursing') & Skill(name='healthcare') &
      Interest(name='helping others') & Education(level="Associate's Degree"))
    def recommend_nurse(self):
        self.declare(Career(
            title="Nurse",
            description="Provides care to patients in hospitals, clinics, and other healthcare settings.",
            qualifications="Knowledge of nursing principles and practices. Compassion and strong clinical skills."
        ))

    @Rule(Skill(name='teaching') & Skill(name='communication') &
      Interest(name='education') & Education(level="Bachelor's Degree"))
    def recommend_teacher(self):
        self.declare(Career(
            title="Teacher",
            description="Educates students in various subjects at different grade levels.",
            qualifications="Strong teaching and communication skills. Knowledge of pedagogy and subject matter expertise."
        ))

    @Rule(Skill(name='sales') & Skill(name='communication') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_sales_representative(self):
        self.declare(Career(
            title="Sales Representative",
            description="Sells products or services to customers, building relationships and closing deals.",
            qualifications="Excellent communication and sales skills. Persuasion and negotiation abilities."
        ))

    @Rule(Skill(name='coding') & Skill(name='web development') &
        Interest(name='technology') & Education(level="Bachelor's Degree"))
    def recommend_web_developer(self):
        self.declare(Career(
            title="Web Developer",
            description="Designs and develops websites and web applications.",
            qualifications="Proficiency in HTML, CSS, and JavaScript. Knowledge of web development frameworks."
        ))

    @Rule(Skill(name='data analysis') & Skill(name='statistics') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_data_analyst(self):
        self.declare(Career(
            title="Data Analyst",
            description="Analyzes data to identify trends, patterns, and insights to support business decisions.",
            qualifications="Strong analytical and data analysis skills. Proficiency in data analysis tools and techniques."
        ))

    @Rule(Skill(name='problem-solving') & Skill(name='critical thinking') &
        Interest(name='science') & Education(level="Doctorate"))
    def recommend_research_scientist(self):
        self.declare(Career(
            title="Research Scientist",
            description="Conducts research to advance knowledge in a specific field.",
            qualifications="Strong research and analytical skills. Expertise in a specific scientific discipline."
        ))

    @Rule(Skill(name='creativity') & Skill(name='artistic expression') &
        Interest(name='art') & Education(level="Bachelor's Degree"))
    def recommend_artist(self):
        self.declare(Career(
            title="Artist",
            description="Creates original works of art in various media.",
            qualifications="Strong artistic talent and creativity.  Portfolio of work."
        ))

    @Rule(Skill(name='legal research') & Skill(name='writing') &
      Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_lawyer(self):
        self.declare(Career(
            title="Lawyer",
            description="Advises clients on legal matters, represents them in court, and drafts legal documents.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills."
        ))

    @Rule(Skill(name='medical knowledge') & Skill(name='patient care') &
        Interest(name='healthcare') & Education(level="Doctor of Medicine"))
    def recommend_physician(self):
        self.declare(Career(
            title="Physician",
            description="Diagnoses and treats illnesses and injuries.",
            qualifications="Doctor of Medicine degree. Strong medical knowledge and clinical skills."
        ))

    @Rule(Skill(name='software engineering') & Skill(name='programming') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_software_engineer(self):
        self.declare(Career(
            title="Software Engineer",
            description="Designs, develops, and maintains software systems.",
            qualifications="Strong programming skills and knowledge of software engineering principles."
        ))

    @Rule(Skill(name='financial analysis') & Skill(name='investment management') &
        Interest(name='finance') & Education(level="Master's Degree"))
    def recommend_financial_analyst(self):
        self.declare(Career(
            title="Financial Analyst",
            description="Analyzes financial data, provides investment recommendations, and manages financial risk.",
            qualifications="Strong analytical and financial modeling skills. Knowledge of financial markets."
        ))

    @Rule(Skill(name='project management') & Skill(name='leadership') &
        Interest(name='business') & Education(level="Master's Degree"))
    def recommend_program_manager(self):
        self.declare(Career(
            title="Program Manager",
            description="Oversees multiple related projects, ensuring they align with strategic goals.",
            qualifications="Strong project management, leadership, and communication skills."
        ))

    @Rule(Skill(name='teaching') & Skill(name='research') &
        Interest(name='academia') & Education(level="Doctorate"))
    def recommend_professor(self):
        self.declare(Career(
            title="Professor",
            description="Teaches courses at the university level and conducts research in a specific field.",
            qualifications="Doctorate degree. Strong teaching and research skills. Subject matter expertise."
        ))

    @Rule(Skill(name='writing') & Skill(name='journalism') &
      Interest(name='news') & Education(level="Bachelor's Degree"))
    def recommend_journalist(self):
        self.declare(Career(
            title="Journalist",
            description="Researches, writes, and reports news stories for various media outlets.",
            qualifications="Strong writing and communication skills.  Investigative skills and knowledge of current events."
        ))

    @Rule(Skill(name='public speaking') & Skill(name='persuasion') &
        Interest(name='politics') & Education(level="Bachelor's Degree"))
    def recommend_political_scientist(self):
        self.declare(Career(
            title="Political Scientist",
            description="Studies political systems, theories, and behavior.",
            qualifications="Strong analytical and research skills. Knowledge of political theory and current events."
        ))

    @Rule(Skill(name='design') & Skill(name='user experience') &
        Interest(name='technology') & Education(level="Bachelor's Degree"))
    def recommend_ux_designer(self):
        self.declare(Career(
            title="UX Designer",
            description="Designs user-friendly and effective interfaces for websites and applications.",
            qualifications="Strong design and user research skills. Knowledge of user-centered design principles."
        ))

    @Rule(Skill(name='data analysis') & Skill(name='business intelligence') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_business_analyst(self):
        self.declare(Career(
            title="Business Analyst",
            description="Analyzes business processes and identifies areas for improvement.",
            qualifications="Strong analytical and problem-solving skills.  Knowledge of business processes and data analysis."
        ))

    @Rule(Skill(name='teaching') & Skill(name='mentoring') &
        Interest(name='education') & Education(level="Master's Degree"))
    def recommend_educational_administrator(self):
        self.declare(Career(
            title="Educational Administrator",
            description="Manages educational institutions and programs.",
            qualifications="Strong leadership and management skills.  Knowledge of educational principles and practices."
        ))

    @Rule(Skill(name='creative writing') & Skill(name='storytelling') &
        Interest(name='art') & Education(level="Bachelor's Degree"))
    def recommend_writer(self):
        self.declare(Career(
            title="Writer",
            description="Writes books, articles, scripts, and other forms of written content.",
            qualifications="Excellent writing and storytelling skills. Creativity and imagination."
        ))

    @Rule(Skill(name='mechanics') & Skill(name='troubleshooting') &
      Interest(name='engineering') & Education(level="High School"))
    def recommend_automotive_technician(self):
        self.declare(Career(
            title="Automotive Technician",
            description="Diagnoses and repairs vehicles.",
            qualifications="Knowledge of automotive systems and repair procedures. Mechanical skills."
        ))

    @Rule(Skill(name='culinary arts') & Skill(name='cooking') &
        Interest(name='food') & Education(level="Associate's Degree"))
    def recommend_chef(self):
        self.declare(Career(
            title="Chef",
            description="Prepares and cooks food in restaurants and other food service establishments.",
            qualifications="Knowledge of culinary techniques and food safety. Creativity and passion for food."
        ))

    @Rule(Skill(name='marketing') & Skill(name='advertising') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_marketing_manager(self):
        self.declare(Career(
            title="Marketing Manager",
            description="Develops and implements marketing strategies to promote products or services.",
            qualifications="Strong marketing and communication skills. Knowledge of marketing principles and techniques."
        ))

    @Rule(Skill(name='computer science') & Skill(name='software development') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_computer_scientist(self):
        self.declare(Career(
            title="Computer Scientist",
            description="Conducts research in computer science and develops new technologies.",
            qualifications="Strong computer science background and research skills.  Knowledge of algorithms and data structures."
        ))

    @Rule(Skill(name='law') & Skill(name='legal writing') &
        Interest(name='justice') & Education(level="Juris Doctor"))
    def recommend_paralegal(self):
        self.declare(Career(
            title="Paralegal",
            description="Assists lawyers with legal research, document preparation, and client communication.",
            qualifications="Knowledge of legal procedures and terminology. Strong research and writing skills."
        ))

    @Rule(Skill(name='dental hygiene') & Skill(name='patient care') &
        Interest(name='healthcare') & Education(level="Associate's Degree"))
    def recommend_dental_hygienist(self):
        self.declare(Career(
            title="Dental Hygienist",
            description="Cleans teeth, provides oral hygiene education, and performs other dental care procedures.",
            qualifications="Knowledge of dental hygiene principles and practices.  Clinical skills and patient communication skills."
        ))

    @Rule(Skill(name='electrician') & Skill(name='wiring') &
      Interest(name='engineering') & Education(level="High School"))
    def recommend_electrician(self):
        self.declare(Career(
            title="Electrician",
            description="Installs and maintains electrical systems.",
            qualifications="Knowledge of electrical codes and safety procedures.  Technical and problem-solving skills."
        ))

    @Rule(Skill(name='welding') & Skill(name='fabrication') &
        Interest(name='manufacturing') & Education(level="Associate's Degree"))
    def recommend_welder(self):
        self.declare(Career(
            title="Welder",
            description="Joins metal parts using welding techniques.",
            qualifications="Knowledge of welding processes and safety procedures.  Technical and manual skills."
        ))

    @Rule(Skill(name='human resources') & Skill(name='employee relations') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_human_resources_manager(self):
        self.declare(Career(
            title="Human Resources Manager",
            description="Manages employee relations, recruitment, and benefits.",
            qualifications="Strong communication and interpersonal skills. Knowledge of employment law and HR best practices."
        ))

    @Rule(Skill(name='cybersecurity') & Skill(name='network security') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_cybersecurity_analyst(self):
        self.declare(Career(
            title="Cybersecurity Analyst",
            description="Protects computer systems and networks from cyber threats.",
            qualifications="Knowledge of cybersecurity principles and technologies.  Analytical and problem-solving skills."
        ))

    @Rule(Skill(name='legal research') & Skill(name='litigation') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_litigation_lawyer(self):
        self.declare(Career(
            title="Litigation Lawyer",
            description="Represents clients in lawsuits and other legal proceedings.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills."
        ))

    @Rule(Skill(name='pharmacy') & Skill(name='patient counseling') &
        Interest(name='healthcare') & Education(level="Doctor of Pharmacy"))
    def recommend_pharmacist(self):
        self.declare(Career(
            title="Pharmacist",
            description="Dispenses medications and provides drug information to patients.",
            qualifications="Doctor of Pharmacy degree.  Knowledge of pharmacology and patient counseling skills."
        ))

    @Rule(Skill(name='carpentry') & Skill(name='construction') &
      Interest(name='building') & Education(level="High School"))
    def recommend_carpenter(self):
        self.declare(Career(
            title="Carpenter",
            description="Constructs and repairs building frameworks and structures using wood.",
            qualifications="Knowledge of carpentry techniques and tools.  Manual and technical skills."
        ))

    @Rule(Skill(name='medical assisting') & Skill(name='patient care') &
        Interest(name='healthcare') & Education(level="Associate's Degree"))
    def recommend_medical_assistant(self):
        self.declare(Career(
            title="Medical Assistant",
            description="Provides clinical and administrative support to physicians in medical offices.",
            qualifications="Knowledge of medical procedures and terminology. Clinical and interpersonal skills."
        ))

    @Rule(Skill(name='finance') & Skill(name='investment') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_financial_advisor(self):
        self.declare(Career(
            title="Financial Advisor",
            description="Provides financial advice to individuals and businesses.",
            qualifications="Strong financial knowledge and communication skills.  Analytical and interpersonal skills."
        ))

    @Rule(Skill(name='artificial intelligence') & Skill(name='machine learning') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_ai_engineer(self):
        self.declare(Career(
            title="AI Engineer",
            description="Develops and implements artificial intelligence and machine learning systems.",
            qualifications="Strong computer science and mathematics background. Knowledge of AI/ML algorithms and techniques."
        ))

    @Rule(Skill(name='contract law') & Skill(name='negotiation') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_corporate_lawyer(self):
        self.declare(Career(
            title="Corporate Lawyer",
            description="Advises businesses on legal matters related to contracts, mergers, and acquisitions.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and negotiation skills."
        ))

    @Rule(Skill(name='veterinary medicine') & Skill(name='animal care') &
        Interest(name='animals') & Education(level="Doctor of Veterinary Medicine"))
    def recommend_veterinarian(self):
        self.declare(Career(
            title="Veterinarian",
            description="Provides medical care to animals.",
            qualifications="Doctor of Veterinary Medicine degree.  Knowledge of animal health and disease. Clinical skills."
        ))

    @Rule(Skill(name='plumbing') & Skill(name='pipe fitting') &
      Interest(name='construction') & Education(level="High School"))
    def recommend_plumber(self):
        self.declare(Career(
            title="Plumber",
            description="Installs and repairs water and drainage systems.",
            qualifications="Knowledge of plumbing codes and techniques. Technical and problem-solving skills."
        ))

    @Rule(Skill(name='early childhood education') & Skill(name='child development') &
        Interest(name='education') & Education(level="Associate's Degree"))
    def recommend_preschool_teacher(self):
        self.declare(Career(
            title="Preschool Teacher",
            description="Teaches and cares for young children in preschool settings.",
            qualifications="Knowledge of child development and early childhood education principles.  Patience and communication skills."
        ))

    @Rule(Skill(name='public relations') & Skill(name='communication') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_public_relations_manager(self):
        self.declare(Career(
            title="Public Relations Manager",
            description="Manages communication between organizations and the public.",
            qualifications="Strong communication and interpersonal skills. Knowledge of public relations principles and techniques."
        ))

    @Rule(Skill(name='biotechnology') & Skill(name='molecular biology') &
        Interest(name='science') & Education(level="Master's Degree"))
    def recommend_biotechnologist(self):
        self.declare(Career(
            title="Biotechnologist",
            description="Applies biological principles to develop new technologies and products.",
            qualifications="Strong biology background and research skills. Knowledge of biotechnology techniques and applications."
        ))

    @Rule(Skill(name='international law') & Skill(name='human rights') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_international_lawyer(self):
        self.declare(Career(
            title="International Lawyer",
            description="Advises clients on legal matters related to international law and human rights.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills. Knowledge of international law."
        ))

    @Rule(Skill(name='physical therapy') & Skill(name='rehabilitation') &
        Interest(name='healthcare') & Education(level="Doctor of Physical Therapy"))
    def recommend_physical_therapist(self):
        self.declare(Career(
            title="Physical Therapist",
            description="Helps patients recover from injuries and illnesses through exercise and rehabilitation programs.",
            qualifications="Doctor of Physical Therapy degree. Knowledge of anatomy and physiology.  Clinical and interpersonal skills."
        ))

    @Rule(Skill(name='hvac') & Skill(name='refrigeration') &
      Interest(name='engineering') & Education(level="High School"))
    def recommend_hvac_technician(self):
        self.declare(Career(
            title="HVAC Technician",
            description="Installs and maintains heating, ventilation, and air conditioning systems.",
            qualifications="Knowledge of HVAC systems and repair procedures. Technical and problem-solving skills."
        ))

    @Rule(Skill(name='paralegal studies') & Skill(name='legal research') &
        Interest(name='law') & Education(level="Associate's Degree"))
    def recommend_legal_assistant(self):
        self.declare(Career(
            title="Legal Assistant",
            description="Provides administrative and legal support to lawyers.",
            qualifications="Knowledge of legal procedures and terminology. Strong organizational and communication skills."
        ))

    @Rule(Skill(name='marketing research') & Skill(name='data analysis') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_market_research_analyst(self):
        self.declare(Career(
            title="Market Research Analyst",
            description="Studies consumer behavior and market trends to provide insights to businesses.",
            qualifications="Strong analytical and research skills. Knowledge of marketing principles and statistics."
        ))

    @Rule(Skill(name='bioinformatics') & Skill(name='genetics') &
        Interest(name='science') & Education(level="Master's Degree"))
    def recommend_bioinformatician(self):
        self.declare(Career(
            title="Bioinformatician",
            description="Applies computational and statistical methods to analyze biological data.",
            qualifications="Strong biology and computer science background. Knowledge of bioinformatics tools and databases."
        ))

    @Rule(Skill(name='environmental law') & Skill(name='policy analysis') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_environmental_lawyer(self):
        self.declare(Career(
            title="Environmental Lawyer",
            description="Advises clients on legal matters related to environmental protection.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills. Knowledge of environmental law."
        ))

    @Rule(Skill(name='occupational therapy') & Skill(name='rehabilitation') &
        Interest(name='healthcare') & Education(level="Master's Degree"))
    def recommend_occupational_therapist(self):
        self.declare(Career(
            title="Occupational Therapist",
            description="Helps patients develop or regain skills needed for daily living and working.",
            qualifications="Master's degree in Occupational Therapy. Knowledge of anatomy and physiology. Clinical and interpersonal skills."
        ))

    @Rule(Skill(name='masonry') & Skill(name='construction') &
      Interest(name='building') & Education(level="High School"))
    def recommend_mason(self):
        self.declare(Career(
            title="Mason",
            description="Builds and repairs structures using brick, stone, and other masonry materials.",
            qualifications="Knowledge of masonry techniques and materials. Manual and technical skills."
        ))

    @Rule(Skill(name='medical coding') & Skill(name='billing') &
        Interest(name='healthcare') & Education(level="Associate's Degree"))
    def recommend_medical_coder(self):
        self.declare(Career(
            title="Medical Coder",
            description="Assigns codes to medical diagnoses and procedures for billing and insurance purposes.",
            qualifications="Knowledge of medical coding systems and terminology.  Analytical and detail-oriented skills."
        ))

    @Rule(Skill(name='sales') & Skill(name='business development') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_business_development_manager(self):
        self.declare(Career(
            title="Business Development Manager",
            description="Identifies and develops new business opportunities for organizations.",
            qualifications="Strong sales and communication skills.  Strategic thinking and networking abilities."
        ))

    @Rule(Skill(name='data science') & Skill(name='machine learning') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_machine_learning_engineer(self):
        self.declare(Career(
            title="Machine Learning Engineer",
            description="Develops and implements machine learning algorithms and models.",
            qualifications="Strong computer science and mathematics background. Knowledge of machine learning techniques and tools."
        ))

    @Rule(Skill(name='intellectual property law') & Skill(name='patent law') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_patent_lawyer(self):
        self.declare(Career(
            title="Patent Lawyer",
            description="Advises clients on patent law matters and helps them obtain patents for their inventions.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills. Knowledge of patent law."
        ))

    @Rule(Skill(name='speech therapy') & Skill(name='communication disorders') &
        Interest(name='healthcare') & Education(level="Master's Degree"))
    def recommend_speech_language_pathologist(self):
        self.declare(Career(
            title="Speech-Language Pathologist",
            description="Diagnoses and treats communication and swallowing disorders.",
            qualifications="Master's degree in Speech-Language Pathology. Knowledge of communication disorders. Clinical and interpersonal skills."
        ))

    @Rule(Skill(name='automotive repair') & Skill(name='diagnostics') &
      Interest(name='engineering') & Education(level="High School"))
    def recommend_diesel_mechanic(self):
        self.declare(Career(
            title="Diesel Mechanic",
            description="Diagnoses and repairs diesel engines and vehicles.",
            qualifications="Knowledge of diesel engine systems and repair procedures. Technical and problem-solving skills."
        ))

    @Rule(Skill(name='office administration') & Skill(name='clerical skills') &
        Interest(name='business') & Education(level="Associate's Degree"))
    def recommend_administrative_assistant(self):
        self.declare(Career(
            title="Administrative Assistant",
            description="Provides administrative support to offices and organizations.",
            qualifications="Strong organizational and communication skills. Proficiency in office software."
        ))

    @Rule(Skill(name='brand management') & Skill(name='marketing') &
        Interest(name='business') & Education(level="Bachelor's Degree"))
    def recommend_brand_manager(self):
        self.declare(Career(
            title="Brand Manager",
            description="Develops and implements marketing strategies to promote brands.",
            qualifications="Strong marketing and communication skills. Knowledge of brand management principles."
        ))

    @Rule(Skill(name='computer vision') & Skill(name='image processing') &
        Interest(name='technology') & Education(level="Master's Degree"))
    def recommend_computer_vision_engineer(self):
        self.declare(Career(
            title="Computer Vision Engineer",
            description="Develops and implements computer vision algorithms and systems.",
            qualifications="Strong computer science and mathematics background. Knowledge of computer vision techniques."
        ))

    @Rule(Skill(name='real estate law') & Skill(name='property law') &
        Interest(name='law') & Education(level="Juris Doctor"))
    def recommend_real_estate_lawyer(self):
        self.declare(Career(
            title="Real Estate Lawyer",
            description="Advises clients on legal matters related to real estate transactions.",
            qualifications="Juris Doctor degree. Strong legal research, writing, and advocacy skills. Knowledge of real estate law."
        ))

    @Rule(Skill(name='music therapy') & Skill(name='music') &
        Interest(name='healthcare') & Education(level="Master's Degree"))
    def recommend_music_therapist(self):
        self.declare(Career(
            title="Music Therapist",
            description="Uses music to help patients with physical, emotional, and cognitive challenges.",
            qualifications="Master's degree in Music Therapy. Knowledge of music and therapy techniques. Clinical and interpersonal skills."
        ))

    @Rule(Skill(name='welding') & Skill(name='metal fabrication') & Interest(name='manufacturing') & Education(level="High School"))
    def recommend_industrial_welder(self):
        self.declare(Career(
            title="Industrial Welder", 
            description="Performs welding in manufacturing or construction settings.", 
            qualifications="Welding skills, knowledge of safety procedures, ability to read blueprints."
        ))

@Rule(Skill(name='phlebotomy') & Skill(name='blood drawing') & Interest(name='healthcare') & Education(level="Associate's Degree"))
def recommend_phlebotomist(self):
    self.declare(Career(title="Phlebotomist", description="Draws blood for medical testing.", qualifications="Phlebotomy certification, knowledge of blood drawing techniques, patient communication skills."))

@Rule(Skill(name='digital marketing') & Skill(name='social media marketing') & Interest(name='business') & Education(level="Bachelor's Degree"))
def recommend_social_media_manager(self):
    self.declare(Career(title="Social Media Manager", description="Manages social media presence for organizations.", qualifications="Social media marketing skills, content creation abilities, data analysis skills."))

@Rule(Skill(name='natural language processing') & Skill(name='computational linguistics') & Interest(name='technology') & Education(level="Master's Degree"))
def recommend_nlp_engineer(self):
    self.declare(Career(title="NLP Engineer", description="Develops natural language processing systems.", qualifications="Computer science background, knowledge of NLP techniques, programming skills."))

@Rule(Skill(name='family law') & Skill(name='divorce law') & Interest(name='law') & Education(level="Juris Doctor"))
def recommend_family_lawyer(self):
    self.declare(Career(title="Family Lawyer", description="Handles legal matters related to families, such as divorce and custody.", qualifications="Juris Doctor degree, knowledge of family law, strong communication skills."))

@Rule(Skill(name='art therapy') & Skill(name='counseling') & Interest(name='healthcare') & Education(level="Master's Degree"))
def recommend_art_therapist(self):
    self.declare(Career(title="Art Therapist", description="Uses art to help patients with emotional and mental health issues.", qualifications="Master's degree in Art Therapy, knowledge of art and therapy techniques, clinical skills."))

    @Rule(Skill(name='aircraft mechanics') & Skill(name='aviation') & Interest(name='engineering') & Education(level="High School"))
    def recommend_aircraft_mechanic(self):
        self.declare(Career(
            title="Aircraft Mechanic", 
            description="Maintains and repairs aircraft.", qualifications="Aviation maintenance certification, knowledge of aircraft systems, technical skills."
        ))

@Rule(Skill(name='medical transcription') & Skill(name='typing') & Interest(name='healthcare') & Education(level="Associate's Degree"))
def recommend_medical_transcriptionist(self):
    self.declare(Career(title="Medical Transcriptionist", description="Transcribes medical reports dictated by physicians.", qualifications="Medical transcription certification, knowledge of medical terminology, typing skills."))

@Rule(Skill(name='public relations') & Skill(name='media relations') & Interest(name='business') & Education(level="Bachelor's Degree"))
def recommend_media_relations_manager(self):
    self.declare(Career(title="Media Relations Manager", description="Manages communication between organizations and the media.", qualifications="Public relations skills, media relations experience, strong communication skills."))

@Rule(Skill(name='database management') & Skill(name='data modeling') & Interest(name='technology') & Education(level="Master's Degree"))
def recommend_database_administrator(self):
    self.declare(Career(title="Database Administrator", description="Manages and maintains databases.", qualifications="Computer science background, knowledge of database systems, data modeling skills."))

@Rule(Skill(name='tax law') & Skill(name='tax preparation') & Interest(name='law') & Education(level="Juris Doctor"))
def recommend_tax_lawyer(self):
    self.declare(Career(title="Tax Lawyer", description="Advises clients on tax law matters and represents them before tax authorities.", qualifications="Juris Doctor degree, knowledge of tax law, strong analytical skills."))

@Rule(Skill(name='dance therapy') & Skill(name='dance') & Interest(name='healthcare') & Education(level="Master's Degree"))
def recommend_dance_therapist(self):
    self.declare(Career(title="Dance Therapist", description="Uses dance to help patients with physical, emotional, and mental health issues.", qualifications="Master's degree in Dance Therapy, knowledge of dance and therapy techniques, clinical skills."))

    @Rule(Skill(name='wind turbine maintenance') & Skill(name='renewable energy') & Interest(name='engineering') & Education(level="Associate's Degree"))
    def recommend_wind_turbine_technician(self):
        self.declare(Career(
            title="Wind Turbine Technician", description="Installs, maintains, and repairs wind turbines.", 
            qualifications="Technical skills, knowledge of electrical and mechanical systems, ability to work at heights."
        ))

@Rule(Skill(name='medical billing') & Skill(name='insurance claims') & Interest(name='healthcare') & Education(level="Associate's Degree"))
def recommend_medical_billing_specialist(self):
    self.declare(Career(title="Medical Billing Specialist", description="Prepares and submits medical insurance claims.", qualifications="Knowledge of medical billing codes and procedures, attention to detail, computer skills."))

@Rule(Skill(name='event planning') & Skill(name='logistics') & Interest(name='business') & Education(level="Bachelor's Degree"))
def recommend_event_planner(self):
    self.declare(Career(title="Event Planner", description="Plans and organizes events.", qualifications="Organizational skills, communication skills, attention to detail."))

@Rule(Skill(name='network engineering') & Skill(name='computer networking') & Interest(name='technology') & Education(level="Master's Degree"))
def recommend_network_engineer(self):
    self.declare(Career(title="Network Engineer", description="Designs, implements, and maintains computer networks.", qualifications="Computer science background, knowledge of networking protocols, technical skills."))

@Rule(Skill(name='criminal law') & Skill(name='legal advocacy') & Interest(name='law') & Education(level="Juris Doctor"))
def recommend_criminal_lawyer(self):
    self.declare(Career(title="Criminal Lawyer", description="Represents clients accused of crimes.", qualifications="Juris Doctor degree, knowledge of criminal law, strong advocacy skills."))

@Rule(Skill(name='drama therapy') & Skill(name='theater') & Interest(name='healthcare') & Education(level="Master's Degree"))
def recommend_drama_therapist(self):
    self.declare(Career(title="Drama Therapist", description="Uses drama and theater techniques to help patients with emotional and mental health issues.", qualifications="Master's degree in Drama Therapy, knowledge of theater and therapy techniques, clinical skills."))

    @Rule(Skill(name='solar panel installation') & Skill(name='renewable energy') & Interest(name='engineering') & Education(level="High School"))
    def recommend_solar_panel_installer(self):
        self.declare(Career(
            title="Solar Panel Installer", description="Installs and maintains solar panels.", 
            qualifications="Technical skills, knowledge of electrical systems, ability to work at heights."
        ))

@Rule(Skill(name='medical coding') & Skill(name='data entry') & Interest(name='healthcare') & Education(level="Associate's Degree"))
def recommend_medical_records_technician(self):
    self.declare(Career(title="Medical Records Technician", description="Maintains and organizes medical records.", qualifications="Knowledge of medical terminology, attention to detail, computer skills."))

@Rule(Skill(name='advertising') & Skill(name='marketing strategy') & Interest(name='business') & Education(level="Bachelor's Degree"))
def recommend_advertising_manager(self):
    self.declare(Career(title="Advertising Manager", description="Develops and implements advertising campaigns.", qualifications="Marketing skills, advertising experience, communication skills."))

@Rule(Skill(name='information security') & Skill(name='network security') & Interest(name='technology') & Education(level="Master's Degree"))
def recommend_information_security_analyst(self):
    self.declare(Career(title="Information Security Analyst", description="Protects computer systems and networks from security threats.", qualifications="Computer science background, knowledge of security protocols, analytical skills."))

@Rule(Skill(name='contract law') & Skill(name='negotiation') & Interest(name='law') & Education(level="Juris Doctor"))
def recommend_entertainment_lawyer(self):
    self.declare(Career(title="Entertainment Lawyer", description="Advises clients in the entertainment industry on legal matters.", qualifications="Juris Doctor degree, knowledge of contract law, strong negotiation skills."))

@Rule(Skill(name='music education') & Skill(name='music performance') & Interest(name='music') & Education(level="Master's Degree"))
def recommend_music_teacher(self):
    self.declare(Career(title="Music Teacher", description="Teaches music to students of various ages and skill levels.", qualifications="Music degree, teaching experience, strong communication skills."))

    @Rule(Skill(name='animation') & Skill(name='graphic_design') & Interest(name='art') & Education(level="Bachelor's Degree"))
    def recommend_animator(self):
        self.declare(Career(
            title="Animator", 
            description="Creates animated content for films, television, and video games.", 
            qualifications="Animation skills, graphic design skills, creativity, storytelling abilities"
        ))

    # Add more rules as needed

    @Rule(Career(title=MATCH.title, description=MATCH.description, qualifications=MATCH.qualifications))
    def display_recommendation(self, title, description, qualifications):
        print(f"Recommended Career: {title}")
        print(f"Description: {description}")
        print(f"Qualifications: {qualifications}\n")
