#students exams data entries for terminal report card
print("Westside Educational Complex--End Of second Terminal Report--Class-KKJA--Name:Theodora Obaa Yaa Gyarbeng")
while True:
   
    student_score = float(input ("Enter the student score:"))
    if student_score >= 1.0 and student_score <= 39.9:
        print("student_score is F9", "fail")
    elif student_score >= 40 and student_score <= 49.9:
        print("student_score is E8", "pass" )
    elif student_score >= 50 and student_score <= 59.9:
        print("student_score is D7", "credit")
    elif student_score >= 60 and student_score <= 69.9:
        print("student_score is C4", "good")
    elif student_score >= 70 and student_score <= 79.9:
        print("student_score is B2", "very_good")
    elif student_score >= 80 and student_score <= 100:
        print("student_score is A1", "excellent")
    else:
        
        print("student_score is invalid entry")
           
student = []

