from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    experience = db.Column(db.Integer())
    job_profile = db.Column(db.String())


    def __init__(self, employee_id, name, experience, job_profile):
        self.employee_id = employee_id
        self.name = name
        self.experience = experience
        self.job_profile = job_profile

    def __repr__(self):
        return f"{self.name}: {self.employee_id}"