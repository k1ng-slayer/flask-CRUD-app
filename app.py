from flask import Flask, abort, redirect, render_template, request
from models import db, EmployeeModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee_details.db'  # path where the database file is created by the name "employee_details.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        experience = request.form['experience']
        job_profile = request.form['job_profile']

        employee = EmployeeModel(employee_id=employee_id, name=name, experience=experience, job_profile=job_profile)
        
        db.session.add(employee)
        db.session.commit()
        
        return redirect('/data')
    
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html', employees=employees)

@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee=employee)
    return f"Employee with ID = {id} does not exist."

@app.route('/data/update/<int:id>', methods =['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()
            
            name = request.form['name']
            experience = request.form['experience']
            job_profile = request.form['job_profile']

            employee = EmployeeModel(employee_id=id, name=name, experience=experience, job_profile=job_profile)

            db.session.add(employee)
            db.session.commit()

            return redirect(f'/data/{id}')
        return f"Employee with ID ={id} does not exist."
    
    return render_template('update.html', employee=employee)

@app.route('/data/delete/<int:id>', methods = ['GET',"POST"])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        return f"Employee with ID ={id} does not exist."
    
    return render_template('delete.html')


# app.run(host='localhost', port=5000)
if __name__ == "__main__":
    app.run(debug=True)