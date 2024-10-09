from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .utils import *


#-------------------------- Professor CRUD 
@api_view(['GET'])
def professor_list(request):
    professors = Professor.objects.all()
    serializer = ProfessorSerializer(professors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_professor(request):
    if request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'PUT':
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Professor Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'DELETE':
        professor.delete()
        return Response({"success": "Professor Deleted"}, status=status.HTTP_204_NO_CONTENT)


# ------------------------  Student CRUD 
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Student Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'DELETE':
        student.delete()
        return Response({"success": "Student Deleted"}, status=status.HTTP_204_NO_CONTENT)

# ------------------------  Supervisor CRUD 
@api_view(['GET'])
def supervisor_list(request):
    supervisors = Supervisor.objects.all()
    serializer = SupervisorSerializer(supervisors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_supervisor(request):
    if request.method == 'POST':
        serializer = SupervisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_supervisor(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'PUT':
        serializer = SupervisorSerializer(supervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Supervisor Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_supervisor(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'DELETE':
        supervisor.delete()
        return Response({"success": "Supervisor Deleted"}, status=status.HTTP_204_NO_CONTENT)


# ------------------------    Course CRUD
@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_course(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Course Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'DELETE':
        course.delete()
        return Response({"success": "Course Deleted"}, status=status.HTTP_204_NO_CONTENT)
    
# ---------------------------  LearningProgram CRUD
@api_view(['GET'])
def learningprogram_list(request):
    learningprograms = LearningProgram.objects.all()
    serializer = LearningProgramSerializer(learningprograms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_learningprogram(request):
    if request.method == 'POST':
        serializer = LearningProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_learningprogram(request, pk):
    learningprogram = get_object_or_404(LearningProgram, pk=pk)
    if request.method == 'PUT':
        serializer = LearningProgramSerializer(learningprogram, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Learning Program Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_learningprogram(request, pk):
    learningprogram = get_object_or_404(LearningProgram, pk=pk)
    if request.method == 'DELETE':
        learningprogram.delete()
        return Response({"success": "Learning Program Deleted"}, status=status.HTTP_204_NO_CONTENT)


def student_status_view(request, student_id):
    """
    View to get the average score and program status of a student.
    """
    student = get_object_or_404(Student, id=student_id)
    average_score = StudentUtils.calculate_student_average(student)
    program_status = StudentUtils.check_program_status(student)

    return JsonResponse({
        "student": student.name,
        "average_score": average_score if average_score is not None else "Not enough classes enrolled",
        "program_status": program_status
    })
