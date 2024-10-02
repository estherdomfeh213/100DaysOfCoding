from abc import ABC, abstractmethod

# Abstract class 
class Grade(ABC):
  @abstractmethod
  def calculate_grade(self, score):
    pass
  
  @abstractmethod
  def grade_average(self, score):
    pass
  
#   Concrete class 
class PrimarySchool(Grade):
  def calculate_grade(self, score):
    return f'Primary school total score: {score}'
  
  def grade_average(self, score):
    return f'Average grade for the primary school: {score}'

# Concrete class for JHS Grade 
class JHS(Grade):
  def calculate_grade(self, score):
    return f'Jhs Grade: {score}'
  
  def grade_average(self, score):
    return f'Jhs Average grade: {score}'
  
  
# Usage 
def grade_calculator(school, score):
  print(school.calculate_grade(score))
  print(school.grade_average(score))
  
  
# create of different school
primary_school = PrimarySchool()
jhs_school = JHS()

# process grades 
grade_calculator(primary_school, 80)
grade_calculator(jhs_school, 30)