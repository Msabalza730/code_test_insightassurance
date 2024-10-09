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
