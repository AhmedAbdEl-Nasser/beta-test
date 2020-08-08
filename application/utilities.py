from application import app, logic
from flask_sqlalchemy import SQLAlchemy
from enum import Enum


app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://iypdniqowjsnwb:6cbe81deed2ad012ce17027fad3c084984f4b2db7324ad4eb6021e2f74fbb1a1@ec2-35-173-94-156.compute-1.amazonaws.com:5432/d5rnv8kp6o66uh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define Database
db = SQLAlchemy(app)

# Instantiate database
#db.drop_all()
#db.create_all()

class Level(Enum):
    Freshmen = 0
    Sophomore = 1
    Junior = 2
    Senior1 = 3
    Senior2 = 4

# Students table
class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    program = db.Column(db.String, nullable=False)
    level = db.Column(db.Enum(Level), nullable=False)
    ph = db.Column(db.Integer, nullable=False)  # Passed hours
    gpa = db.Column(db.Float, nullable=False)

    def __init__(self, id, name, program, level, ph, gpa):
        self.id = id
        self.name = name
        self.program = program
        self.level = level
        self.ph = ph
        self.gpa = gpa

    def __repr__(self):
        return f"Student('{self.id}', '{self.gpa}')\n"

# Randomize dummy data
Student_1 = Student("17p2412", "Ahmed", "MCTA", Level.Senior2, 162, 3.7)
Student_2 = Student("17p8120", "Amr Mohamed", "CESS", Level.Senior1, 71, 2.73)
Student_3 = Student("21a9101", "Dina", "BLD",Level.Junior, 72, 2.8)
Student_4 = Student("15p3041", "Menna", "CESS",Level.Senior1, 118, 2.95)
Student_5 = Student("23g1415", "Sara", "COMM",Level.Freshmen, 18, 2.1)

# Fill database
db.session.add(Student_1)
db.session.add(Student_2)
db.session.add(Student_3)
db.session.add(Student_4)
db.session.add(Student_5)
db.session.commit()

# Transcripts
#logic.GenerateTranscript(Student_1.id)
#logic.GenerateTranscript(Student_2.id)
#logic.GenerateTranscript(Student_3.id)
#logic.GenerateTranscript(Student_4.id)
#logic.GenerateTranscript(Student_5.id)