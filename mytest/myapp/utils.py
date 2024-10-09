from .models import *


class StudentUtils:
    
    @staticmethod
    def calculate_student_average(student):
        """
        Calculate the average score for a given student based on their enrollments.
        - num_classes: Count the courses assigned to each student
        - The student must have at least 5 courses enrolled else return None
        - I decided to assign values ​​to be able to calculate the average:
            - If a student approved 4, conditional 3 and if he disapproved 2.
        """
        enrolled = LearningProgram.objects.filter(student=student)
        total_score = 0
        num_classes = enrolled.count()
        
        # filter
        if num_classes < 5:
            return None 

        for enroll in enrolled:
            if enroll.exam_result == 'approved':
                total_score += 4
            elif enroll.exam_result == 'conditional':
                total_score += 3
            elif enroll.exam_result == 'disapproved':
                total_score += 2

        if num_classes == 0:
            return 0  # Avoid division by zero

        average_score = total_score / num_classes
        return average_score


    @staticmethod
    def check_program_status(student):
        """
        Check the program status for a given student based on their average score.
        """
        average_score = StudentUtils.calculate_student_average(student)
        if average_score is None:
            return "Insufficient classes enrolled"

        if average_score >= 3.5:
            return "approved"
        else:
            return "disapproved"


    @staticmethod
    def can_retake_exam(enroll):
        """
        Check if a student can retake an exam based on their current enrollment status.
        """
        if enroll.attempts < 3 and enroll.exam_result == 'disapproved':
            return True
        return False
    

    @staticmethod
    def conditional_classes(student):
        """
        To: Classes conditional must be qualified again with a new exam.
        Returns a list of courses that need to be qualified again.
        """
        conditional_classes = LearningProgram.objects.filter(student=student, exam_result='conditional')
        return conditional_classes


    @staticmethod
    def disapproved_classes(student):
        """
        To: Classes disapproved must be enrolled again.
        Returns a list of courses that need to be re-enrolled.
        """
        disapproved_classes = LearningProgram.objects.filter(student=student, exam_result='disapproved')
        return disapproved_classes
    

    def student_final_status(student):
        """
        To: Classes disapproved must be enrolled again.
        Returns a list of courses that need to be re-enrolled.
        """
        disapproved_classes = StudentUtils.disapproved_classes(student)
        
        if disapproved_classes.exists():
            return "The student must repeat the whole program"
        
        final_status = StudentUtils.check_program_status(student)

        return final_status