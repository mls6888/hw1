# Author: Michael Sullivan msulli6293@psu.edu

GPA = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'D': 1.0, 'F': 0.0}
C1 = input("Enter your course 1 letter grade: ")
char = C1
credit1 = input("Enter your course 1 credit: ")
credit1 = int(credit1)
gradepoint1 = float(f"{GPA[C1]}")
print("Grade point for course 1 is: "f"{GPA[C1]}") 
C2 = input("Enter your course 2 letter grade: ")
char = C2
credit2 = input("Enter Course 2 credit: ")
credit2 = int(credit2)
gradepoint2 = float(f"{GPA[C2]}")
print("Grade point for course 2 is: " f"{GPA[C2]} ")
C3 = input("Enter Course 3 letter grade: ")
char = C3
credit3 = input("Enter Course 3 credit: ")
credit3 = int(credit3)
gradepoint3 = float(f"{GPA[C2]}") 
print("Grade point for course 3 is: " f"{GPA[C3]} ")
GPA = (gradepoint1*credit1+gradepoint2*credit2+gradepoint3*credit3)/(credit1+credit2+credit3)
print("Your GPA is:",GPA)
 











