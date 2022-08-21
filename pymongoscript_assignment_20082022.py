from flask import Flask, request,jsonify
import pymongo


client = pymongo.MongoClient("mongodb+srv://ADUBEYFORU:Train12#$@alok.0ddhn.mongodb.net/?retryWrites=true&w=majority")

db = client.test

database = client['dt21082022']
collection = database["db21082022"]

app = Flask(__name__)

@app.route('/insert',methods=['GET','POST'])
def function_insert():
    if request.method=='POST':
        employee_id = request.json['employee_id']
        emp_name = request.json['emp_name']
        emp_mailid = request.json['emp_mailid']
        emp_salary = int(request.json['emp_salary'])
        emp_attendance = int(request.json['emp_attendance'])
        insert_data = {
            'employee_id':employee_id,
            'emp_name' : emp_name,
            'emp_mailid':emp_mailid,
            'emp_salary':emp_salary,
            'emp_attendance':emp_attendance
        }
        collection.insert_one(insert_data)
        return jsonify('1 row inserted in mongodb')

@app.route('/update',methods=['GET','POST'])
def function_update():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        emp_oldsalary = int(request.json['emp_oldsalary'])
        emp_salary = int(request.json['emp_salary'])
        d = collection.find({'employee_id': employee_id})
        for i in d:
            collection.update_one({'emp_salary': emp_oldsalary}, {'$set': {'emp_salary': emp_salary}})
        return jsonify('1 row updated')

@app.route('/delete',methods=['GET','POST'])
def function_delete():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        collection.delete_one({'employee_id': employee_id})
        return jsonify('1 row deleted')

@app.route('/select',methods=['GET','POST'])
def function_select():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        d = collection.find({'employee_id':employee_id})
        for i in d:
            return jsonify('1 row selected')
        return jsonify(str('data not found'))

if __name__ == '__main__':
    app.run()

