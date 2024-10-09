from django.db import models


class Professor(models.Model):
    """Model to register the profesor rol

    Args:
        - name: CharField to add the name of the professor
    """
    name = models.CharField(max_length=255, verbose_name="Professor")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'


class Student(models.Model):
    """Model to register the student rol

    Args:
        - name: CharField to add the name of the student
        - professor: ForeignKey to assign the professor
    """
    name = models.CharField(max_length=255, verbose_name="Student")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Supervisor(models.Model):
    """Model to register the supervisor rol

    Args:
        - name: CharField to add the name of the supervisor
    """
    name = models.CharField(max_length=255, verbose_name="Supervisor")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisors'


class Course(models.Model):
    """Model to register the classes of the program

    Args:
        - name: CharField to add the name of the class
        - time: PositiveIntegerField to set the maximum time
        - professor: ForeignKey to assign a professor by class
    """
    name = models.CharField(max_length=255, verbose_name="Class")
    time = models.PositiveIntegerField( null=True, verbose_name="Maximum time to be delivered")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class LearningProgram(models.Model):
    """Model to register the enrollment

    Args:
        - student: ForeignKey to enrolled a student
        - course_assigned: ForeignKey to enrolled the classes
        - exam_result: CharField to add the reviews of the exams
        - exam_attached : FileField to attach the exams
        - attempts : PositiveIntegerField to count the times to repeat the exam before considered disapproved
        - supervisor : ForeignKey to assign a supervisor
    """
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
        ('conditional', 'Conditional'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_assigned = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_result = models.CharField(max_length=15, choices=STATUS_CHOICES, blank=True, null=True)
    exam_attached = models.FileField(upload_to='exam_attached/', blank=True, null=True)
    attempts = models.PositiveIntegerField(default=1)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, related_name='supervisor')

    def __str__(self):
        return f'{self.student.name} - {self.course_assigned.name}'

    class Meta:
        verbose_name = 'Learning Program Enrollment'
        verbose_name_plural = 'Learning Program Enrollment'