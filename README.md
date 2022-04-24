# madojo-db
Repo for INFO290T 


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
