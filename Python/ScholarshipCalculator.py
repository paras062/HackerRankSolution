# Branch of Study               Score%              Scholarship%                Remarks
#   Arts                    Score is at least 90        50                  The student is eligible only for one
#   Arts                    Score is an odd number      5                   scholarship  % even if both the score
#   Engineering             Score is more than 85       50                  conditions are valid for the given branch of
#   Engineering             Score is divisble by 7      5                   study. In such cases, students are eligible for
#                                                                           the highest scholarship% applicable among the two.

# If there are 500 students who have joined the university, write a pseudo-code to calculate and display the final fees to be paid by each student.
# You may accept the branch of study, score and course fee as inputs for each student and calculate the final fees to be paid by each student based on
# formulae given below:
# Scholarship amount=course fee * (scholarship%)
# Final fee= course fee - scholarship amount

# total_student = 10
branch = input("Enter Branch: ")
course_fee = input("Enter Course Fee: ")
# score = [90, 91, 49, 84, 85, 89, 11, 17, 94, 35]
score = input("Enter the score: ")
scholarship_amount = 0
scholarship = 0
if branch.upper() == 'ARTS':
    if float(score) >= 90:
        scholarship = 50
    elif float(score) % 2 != 0:
        scholarship = 5
elif branch.upper() == "ENG":
    if float(score) > 85:
        scholarship = 50
    elif float(score)%7 == 0:
        scholarship = 5

scholarship_amount = float(course_fee)*float(scholarship)/100

final_fee = float(course_fee)-float(scholarship_amount)
print(final_fee)
