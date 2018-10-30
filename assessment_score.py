##Assessment Score
##Build a report card printing tool for primary school students.
##You need to take in the following values: School, Name, Class, Score of Math test, Score of Science test, Score of English test

school_name = input("Please enter the school name: ")
class_name = input("Please enter the class: ")
student_initials = input("Please enter the student's first and last initials in capital letters: ")
math_score = int(input("Please enter the Math score (out of 100): "))
science_score = int(input("Please enter the Science score (out of 100): "))
english_score = int(input("Please enter the English score (out of 100): "))
total = math_score + science_score + english_score

print("""
School: %s
Class:  %s
-------------------------
           \t%s
Math       \t|\t%d/100
Science    \t|\t%d/100
English    \t|\t%d/100
-------------------------
Total Score\t|\t%d/100
-------------------------
""" % (school_name, class_name, student_initials, math_score, science_score, english_score, total))


