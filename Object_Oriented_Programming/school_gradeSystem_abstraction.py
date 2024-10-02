from abc import ABC, abstractmethod

# Abstract class with implementation logic
class Grade(ABC):
    
    def __init__(self, passing_score=50):
        # Shared attribute: Define a default passing score
        self.passing_score = passing_score
    
    # Method with common logic for all schools (optional for override)
    def is_pass(self, score):
        # General pass/fail logic based on passing_score
        return score >= self.passing_score
    
    # Abstract methods must be implemented by subclasses
    @abstractmethod
    def calculate_grade(self, score):
        pass
    
    @abstractmethod
    def grade_evaluation(self, score):
        pass

# Concrete class for Primary School Grade
class PrimarySchool(Grade):
    
    def calculate_grade(self, score):
        if 0 <= score <= 100:
            return f'Primary school total score: {score}'
        else:
            return 'Invalid score! Score must be between 0 and 100.'

    def grade_evaluation(self, score):
        # Use shared is_pass() method for pass/fail evaluation
        if self.is_pass(score):
            return 'Primary school result: Pass'
        else:
            return 'Primary school result: Fail'

# Concrete class for JHS Grade
class JHS(Grade):
    
    def calculate_grade(self, score):
        if 0 <= score <= 100:
            return f'JHS total score: {score}'
        else:
            return 'Invalid score! Score must be between 0 and 100.'

    def grade_evaluation(self, score):
        # Using the shared is_pass() method as part of letter grade logic
        if score >= 80:
            return 'JHS grade: A'
        elif score >= 70:
            return 'JHS grade: B'
        elif score >= 60:
            return 'JHS grade: C'
        elif score >= 50:
            return 'JHS grade: D'
        else:
            return 'JHS grade: F'

# Usage
def grade_calculator(school, score):
    print(school.calculate_grade(score))
    print(school.grade_evaluation(score))

# Create instances of different schools
primary_school = PrimarySchool()
jhs_school = JHS()

# Process grades
grade_calculator(primary_school, 80)  # Output: Pass for primary school
grade_calculator(jhs_school, 30)      # Output: F for JHS
