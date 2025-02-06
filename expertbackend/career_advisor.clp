; Define templates for facts
(deftemplate skill
   (slot name))

(deftemplate interest
   (slot name))

(deftemplate education
   (slot level))

(deftemplate career
   (slot title)
   (slot description)
   (slot qualifications))

; Clear out the system
(defrule clear-facts
    (declare (salience 100)) ; Ensure this rule fires first
    ?f <- (initial-fact)
    =>
    (retract ?f)
    (reset)) ; Reset the engine

; Rules for career recommendations
(defrule suggest-software-developer
   (skill (name programming))
   (skill (name problem-solving))
   (interest (name technology))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Software Developer")
                  (description "Develops software applications and systems. Designs, codes, and tests software.")
                  (qualifications "Strong programming skills, problem-solving abilities, knowledge of data structures and algorithms"))))

(defrule suggest-data-scientist
   (skill (name statistics))
   (skill (name machine-learning))
   (skill (name programming))
   (interest (name science))
   (interest (name technology))
   (education (level "Master's Degree"))
   =>
   (assert (career (title "Data Scientist")
                  (description "Analyzes large datasets to extract meaningful insights and build predictive models.")
                  (qualifications "Statistics, Machine Learning, Programming, Data Visualization"))))

(defrule suggest-financial-analyst
   (skill (name finance))
   (skill (name analytical-thinking))
   (interest (name finance))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Financial Analyst")
                  (description "Analyzes financial data, provides investment recommendations, and manages financial risk.")
                  (qualifications "Financial modeling, analytical skills, knowledge of financial markets"))))

(defrule suggest-marketing-manager
   (skill (name communication))
   (skill (name creativity))
   (skill (name business))
   (interest (name business))
   (interest (name arts))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Marketing Manager")
                  (description "Develops and executes marketing campaigns to promote products or services.")
                  (qualifications "Marketing strategy, communication skills, market research"))))

(defrule suggest-mechanical-engineer
   (skill (name engineering))
   (skill (name problem-solving))
   (interest (name engineering))
   (interest (name science))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Mechanical Engineer")
                  (description "Designs, develops, and tests mechanical devices and systems.")
                  (qualifications "Engineering principles, CAD software, problem-solving skills"))))

(defrule suggest-electrical-engineer
    (skill (name engineering))
    (skill (name problem-solving))
    (skill (name analytical-thinking))
    (interest (name technology))
    (interest (name science))
    (education (level "Bachelor's Degree"))
    =>
    (assert (career (title "Electrical Engineer")
                   (description "Designs, develops, and tests electrical devices and systems.")
                   (qualifications "Engineering principles, circuit design, electrical systems knowledge"))))

(defrule suggest-civil-engineer
   (skill (name engineering))
   (skill (name problem-solving))
   (interest (name engineering))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Civil Engineer")
                  (description "Designs, constructs, and maintains infrastructure projects (roads, bridges, buildings).")
                  (qualifications "Structural analysis, project management, knowledge of construction materials"))))

(defrule suggest-registered-nurse
   (skill (name healthcare))
   (skill (name communication))
   (skill (name problem-solving))
   (interest (name healthcare))
   (education (level "Associate's Degree"))
   =>
   (assert (career (title "Registered Nurse")
                  (description "Provides direct patient care, administers medications, and educates patients and families.")
                  (qualifications "Nursing skills, patient care, communication skills"))))

(defrule suggest-teacher
   (skill (name communication))
   (skill (name patience))
   (interest (name education))
   (education (level "Bachelor's Degree"))
   =>
   (assert (career (title "Teacher")
                  (description "Educates students in a specific subject area.")
                  (qualifications "Subject matter expertise, classroom management, communication skills"))))

(defrule suggest-lawyer
   (skill (name law))
   (skill (name communication))
   (skill (name analytical-thinking))
   (interest (name law))
   (education (level "Juris Doctor"))
   =>
   (assert (career (title "Lawyer")
                  (description "Represents clients in legal matters, provides legal advice, and drafts legal documents.")
                  (qualifications "Legal research, writing skills, courtroom advocacy"))))

; Print if there were no recommendations
(defrule no-recommendation
    (not (career))
    =>
    (printout t "No career was able to be recommended with the given skills, interests, and education. Try changing them and running again." crlf))

; Display the results (run after suggestions)
(defrule print-recommendation
    ?c <- (career (title ?title) (description ?description) (qualifications ?qualifications))
    =>
    (printout t "Recommended Career: " ?title crlf)
    (printout t "Description: " ?description crlf)
    (printout t "Qualifications: " ?qualifications crlf)
    (printout t crlf)
    (retract ?c))

; Fact to allow clean up of the code
(deffacts initial-facts
    (initial-fact))