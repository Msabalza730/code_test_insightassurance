# code_test_insightassurance
Technical Test Python Dev By Maryori Sabalza Mejia

For the development of the test, a project was created using Python 3.11 - Django 5.1 and Django Rest Framework for the API. The default database was created with SQLITE3. The goal was to create a system to manage his technical learning program and try to comply with the following requirements:

- Teaching is customized, each student is assigned one teacher only.
- A teacher can have multiple students assigned.
- The Program has 10 classes, but teacher can decide to enroll the student with fewer classes with a minimum of 5. - Each class has a maximum time to be delivered and an exam must be presented at the end. A digital proof of the answered exam must be attached.
- A supervisor (different from the teacher) reviews the exam and gives 1 of 3 results: approved, disapproved, conditional.
- Classes disapproved must be enrolled again.
- Classes conditional must be qualified again with a new exam.
- An exam can be repeated 3 times before considered disapproved.
- After having all approved classes, results are sent to a coordinator who reviews and presents a general result: approved/disapproved (again and different from the first ones) - If the result is disapproved, the student must repeat the whole program

* For the development of this project, the following diagram was created for the models:
![image](https://github.com/user-attachments/assets/c452b519-09a3-41ec-82ce-0436d6e82e38)

* In the utils.py file are the methods to calculate the student's score. I assumed that to pass they must have a score of 4, for the conditional 3 and they fail with 2 or below.
* In the evidence folder you can see some images of the operation of the project and its API.

## Run this project

- git clone https://github.com/Msabalza730/code_test_insightassurance.git

- Create a virtual env 

```python
    python -m venv env
    (windows) cd env -> .\Scripts\activate
    (linux) source env/bin/activate
```

- Install the libraries:

```python
    -  pip install -r requirements.txt
```

- Create a superuser

```python
    - python manage.py createsuperuser 
```

- Run the project

```python
    - python manage.py runserver    
```

- Run test

```python
    - python manage.py test   
```

- The available URLs in this project:
```
    admin/
    myapp/ professors/ [name='professor_list']
    myapp/ professors/create/ [name='create_professor']
    myapp/ professors/update/<int:pk>/ [name='update_professor']
    myapp/ professors/delete/<int:pk>/ [name='delete_professor']
    myapp/ students/ [name='student_list']
    myapp/ students/create/ [name='create_student']
    myapp/ students/update/<int:pk>/ [name='update_student']
    myapp/ students/delete/<int:pk>/ [name='delete_student']
    myapp/ students/status/<int:student_id>/ [name='student_status']
    myapp/ supervisors/ [name='supervisor_list']
    myapp/ supervisors/create/ [name='create_supervisor']
    myapp/ supervisors/update/<int:pk>/ [name='update_supervisor']
    myapp/ supervisors/delete/<int:pk>/ [name='delete_supervisor']
    myapp/ courses/ [name='course_list']
    myapp/ courses/create/ [name='create_course']
    myapp/ courses/update/<int:pk>/ [name='update_course']
    myapp/ courses/delete/<int:pk>/ [name='delete_course']
    myapp/ learningprograms/ [name='learningprogram_list']
    myapp/ learningprograms/create/ [name='create_learningprogram']
    myapp/ learningprograms/update/<int:pk>/ [name='update_learningprogram']
    myapp/ learningprograms/delete/<int:pk>/ [name='delete_learningprogram']
    myapp/ student-status/<int:student_id>/ [name='student-status']
```
