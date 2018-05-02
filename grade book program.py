math_grade = input('enter your math grade:')
science_grade = input('enter your science grade:')
computer_grade = input('enter your computer grade:')
english_grade = input('enter your english grade:')
history_grade = input('enter your history grade:')

grade_list = [math_grade, science_grade, computer_grade, english_grade, history_grade]

average = (int(math_grade) + int(science_grade) + int(computer_grade) + int(english_grade) + int(history_grade)) / 5

grade_list.append(average)

print "your average will be the last number in this list."
print str(grade_list)

if average < 60:
    print "you need help!"
elif average >= 60 and average <= 69:
    print "you have a D try harder"
elif average >= 70 and average <= 79:
    print "you have a C average right now you can get it up to at least a B"
elif average >= 80 and average <= 89:
    print "keep pushing you got this"
elif average >= 90 and average <= 100:
    print "your doing great!"
