#madojo.py: driver script for DB CRUD API
from flask import Flask, render_template, redirect, Response, request
import psycopg2, os, credlib

madojo = Flask(__name__)


def connection():
    s = 'ec2-3-219-204-29.compute-1.amazonaws.com'
    d = 'd3tkpetdj6me7'
    u = credlib.db_user
    p = credlib.db_secret
    o = '5432'
    conn = psycopg2.connect(host=s, user=u, password=p, database=d, port=o)
    return conn


@madojo.route("/") #default route
def main():
    return render_template('menu.html')

#menu and splashpage

@madojo.route('/menu')
def menu():
    return render_template('menu.html')


#CRUD Operations for Students


@madojo.route("/students")
def students():
    students = []

    try:
        conn = connection()
        msg = print("Sucessfully Connected to Database")
    except:
        msg = print("***** Unsuccessful Connection Attempt! *****")
    cursor = conn.cursor()
    cursor.execute('SELECT * from students')

    for row in cursor.fetchall():
        students.append(({"student_id" : row[0],  "name": row[1], "major": row[2], "interest": row[3],
                          "cv": row[4], "certificate": row[5], "gender" : row[6],"school_year": row[7] }))
    conn.close()

    return render_template("student_list.html", students = students)


@madojo.route("/addstudent", methods = ['GET','POST'])
def addStudent():
    if request.method == 'GET':
        return render_template("addstudent.html")
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        major = request.form["major"]
        interest = request.form["interest"]
        cv = request.form["cv"]
        certificate = request.form["certificate"]
        gender = request.form["gender"]
        school_year = int(request.form["year"])
        msg = print(id,name,major,interest,cv,certificate,gender,school_year)

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, name, major, interest, cv, certificate, gender, school_year))
        conn.commit()
        conn.close()
        return redirect('/students')

@madojo.route('/updateStudent/<int:id>',methods = ['GET','POST'])
def updateStudent(id):
    students = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (str(id)))
        for row in cursor.fetchall():
            students.append(({"student_id" : row[0],  "name": row[1], "major": row[2], "interest": row[3],
                              "cv": row[4], "certificate": row[5], "gender" : row[6],"school_year": row[7] }))
        conn.close()
        return render_template("addstudent.html", student ={})
    if request.method == 'POST':
        name = request.form["name"]
        major = request.form["major"]
        interest = request.form["interest"]
        cv = request.form["cv"]
        certificate = request.form["certificate"]
        gender = request.form["gender"]
        school_year = int(request.form["year"])
        msg = print(id,name,major,interest,cv,certificate,gender,school_year)
        cursor.execute("UPDATE students SET name = %s, major = %s, interest = %s, cv = %s, certificate = %s, gender = %s, "
                       "school_year = %s WHERE student_id = %s", (name, major, interest, cv, certificate, gender, school_year, id) )
        conn.commit()
        conn.close()

    return redirect('/students')


@madojo.route('/deleteStudent/<int:id>')
def deleteStudent(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (str(id)))
    conn.commit()
    conn.close()
    return redirect('/students')


#CRUD Operations for Companies

@madojo.route("/companies")
def companies():
    companies = []

    try:
        conn = connection()
        msg = print("Sucessfully Connected to Database")
    except:
        msg = print("***** Unsuccessful Connection Attempt! *****")
    cursor = conn.cursor()
    cursor.execute('SELECT * from companies')

    for row in cursor.fetchall():
        companies.append(({
            "company_id" : row[0],
            "name": row[1],
            "address" : row[2],
            "industry":row[3]


        }))
    conn.close()

    return render_template("company_list.html", companies = companies)



@madojo.route("/addcompany", methods = ['GET','POST'])
def addCompany():
    if request.method == 'GET':
        return render_template("addcompany.html")
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        address = request.form["address"]
        industry = request.form["industry"]

        msg = print("inserting:",id,name,address,industry)

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO companies VALUES (%s, %s, %s, %s)", (id, name, address, industry))
        conn.commit()
        conn.close()
        return redirect('/companies')


@madojo.route('/updateCompany/<int:id>', methods = ['GET','POST'])
def updateCompany(id):
    companies = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM companies WHERE company_id = %s", (str(id)))
        for row in cursor.fetchall():
            companies.append(({
                "company_id" : row[0],
                "name": row[1],
                "address" : row[2],
                "industry":row[3]


            }))
        conn.close()
        return render_template("addcompany.html", company ={})
    if request.method == 'POST':
        name = request.form["name"]
        address = request.form["address"]
        industry = request.form["industry"]
        msg = print(id,name,address,industry)
        cursor.execute("UPDATE companies SET name = %s, address = %s, industry = %s WHERE company_id = %s",
                       (name, address, industry, id) )
        conn.commit()
        conn.close()

    return redirect('/companies')

@madojo.route('/deleteCompany/<int:id>')
def deleteCompany(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM companies WHERE company_id = %s", (str(id)))
    conn.commit()
    conn.close()
    return redirect('/companies')


#CRUD Operations for Schools
@madojo.route("/schools")
def schools():
    schools = []
    try:
        conn = connection()
        msg = print("Sucessfully Connected to Database")
    except:
        msg = print("***** Unsuccessful Connection Attempt! *****")
    cursor = conn.cursor()
    cursor.execute('SELECT * from school')

    for row in cursor.fetchall():
        schools.append(({
            "school_id" : row[0],
            "address": row[1],
            "name" : row[2],
            "type":row[3],
            "size":row[4]
        }))
    conn.close()

    return render_template("school_list.html", schools = schools)

@madojo.route("/addschool", methods = ['GET','POST'])
def addSchool():
    if request.method == 'GET':
        return render_template("addschool.html")
    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form["name"]
        address = request.form["address"]
        type = request.form["type"]
        size = int(request.form["size"])

        msg = print("inserting:",id,name,address,type,size)

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO school VALUES (%s, %s, %s, %s, %s)", (id, address, name, type,size))
        conn.commit()
        conn.close()
        return redirect('/schools')


@madojo.route('/updateSchool/<int:id>', methods = ['GET','POST'])
def updateSchool(id):
    schools = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM school WHERE school_id = %s", (str(id)))
        for row in cursor.fetchall():
            schools.append(({
                "school_id" : row[0],
                "address": row[1],
                "name" : row[2],
                "type":row[3],
                "size":row[4]
            }))
        conn.close()
        return render_template("addschool.html", company ={})
    if request.method == 'POST':
        address = request.form["address"]
        name = request.form["name"]
        type = request.form["type"]
        size = request.form["size"]
        msg = print("inserting:",id,name,address,type,size)
        cursor.execute("UPDATE school SET address = %s, name = %s, type = %s, size = %s WHERE school_id = %s",
                       ( address, name, type, size,id) )
        conn.commit()
        conn.close()

    return redirect('/schools')


@madojo.route('/deleteSchool/<int:id>')
def deleteSchool(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM school WHERE school_id = %s", (str(id)))
    conn.commit()
    conn.close()
    return redirect('/schools')



#start the server!
if(__name__ == "__main__"):
    madojo.run()