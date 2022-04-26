# madojo-db
Repo for INFO290T Final Project

## Madojo DB Setup

To build a local copy of this web app:

1. Clone this repo to your desired location 
2. run ```pip install -r requirements.txt```
3. run ```python madojo.py```
4. visit http:127.0.0.1:5000 in your browser

## CRUD Details

### Users
* Add/Update/Delete User Endpoints:  
``` python 
@madojo.route("/addstudent", methods = ['GET','POST']) 
@madojo.route('/updatestudent/<int:id>',methods = ['GET','POST'])
@madojo.route('/deletestudent/<int:id>')
```
* Add/Update/Delete User view functions: 
``` python 
addStudent()
updateStudent(id)
deleteStudent(id)
```


### Companies
* Add/Update/Delete Company Endpoints:  
``` python 
@madojo.route("/addcompany", methods = ['GET','POST']) 
@madojo.route('/updatecompany/<int:id>',methods = ['GET','POST'])
@madojo.route('/deletecompany/<int:id>')
```
* Add/Update/Delete Company view functions: 
``` python 
addCompany()
updateCompany(id)
deleteCompanyt(id)
```


### Schools
* Add/Update/Delete School Endpoints:  
``` python 
@madojo.route("/addschool", methods = ['GET','POST']) 
@madojo.route('/updateschool/<int:id>',methods = ['GET','POST'])
@madojo.route('/deleteschool/<int:id>')
```
* Add/Update/Delete School view functions: 
``` python 
addSchool()
updateSchool(id)
deleteSchool(id)
```
