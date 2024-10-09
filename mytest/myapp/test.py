import unittest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import *


class MyAPPTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = APIClient()
        self.professor = Professor.objects.create(name='Professor1')
        self.student = Student.objects.create(name='Mar', professor=self.professor)
        self.course = Course.objects.create(name='Programming', time=60, professor=self.professor)
        self.learning_program = LearningProgram.objects.create(
            student=self.student,
            course_assigned=self.course,
            exam_result='conditional'
        )

    def test_create_student(self):
        url = reverse('myapp:create_student')
        data = {'name': 'Pepito', 'professor': self.professor.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)

    
    def test_get_professors(self):
        url = reverse('myapp:professor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_update_supervisor(self):
        supervisor = Supervisor.objects.create(name='Supervisor 1')
        url = reverse('myapp:update_supervisor', args=[supervisor.pk])
        data = {'name': 'Supervisor MS'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        supervisor.refresh_from_db()
        self.assertEqual(supervisor.name, 'Supervisor MS')


    def test_delete_course(self):
        url = reverse('myapp:delete_course', args=[self.course.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


if __name__ == '__main__':
    unittest.main()