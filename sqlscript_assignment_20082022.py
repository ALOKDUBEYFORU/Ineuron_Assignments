from flask import Flask, request,jsonify
import mysql.connector as conn

mydb = conn.connect(host='localhost',user = 'root', passwd = 'Train12#$')

app = Flask(__name__)

@app.route('/insert',methods=['GET','POST'])
def function_insert():
    if request.method=='POST':
        employee_id = request.json['employee_id']
        emp_name = request.json['emp_name']
        emp_mailid = request.json['emp_mailid']
        emp_salary = int(request.json['emp_salary'])
        emp_attendance = int(request.json['emp_attendance'])
        cursor= mydb.cursor()
        sqlquery = "insert into alok.ineuron values ({},'{}','{}',{},{})".format(employee_id,emp_name,emp_mailid,emp_salary,emp_attendance)
        #return jsonify(sqlquery)
        cursor.execute(sqlquery)
        mydb.commit()
        return jsonify('1 row inserted')

@app.route('/update',methods=['GET','POST'])
def function_update():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        emp_salary = int(request.json['emp_salary'])
        cursor= mydb.cursor()
        sqlquery = "update alok.ineuron set emp_salary = {} where employee_id = {}".format(emp_salary,employee_id)
        #return jsonify(sqlquery)
        cursor.execute(sqlquery)
        mydb.commit()
        return jsonify('1 row updated')

@app.route('/delete',methods=['GET','POST'])
def function_delete():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        cursor= mydb.cursor()
        sqlquery = "delete from alok.ineuron where employee_id = {}".format(employee_id)
        #return jsonify(sqlquery)
        cursor.execute(sqlquery)
        mydb.commit()
        return jsonify('1 row deleted')

@app.route('/select',methods=['GET','POST'])
def function_select():
    if request.method=='POST':
        employee_id = int(request.json['employee_id'])
        cursor= mydb.cursor()
        sqlquery = "select * from alok.ineuron where employee_id = {}".format(employee_id)
        #return jsonify(sqlquery)
        cursor.execute(sqlquery)
        list1 = []
        for i in cursor.fetchall():
            list1.append(i)
        return jsonify(list1)

if __name__ == '__main__':
    app.run()
