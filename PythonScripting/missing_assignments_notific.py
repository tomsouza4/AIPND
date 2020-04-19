# get and process input for a list of names
names =  str(input("Enter names separated by commas: ")).title().split(",")
# get and process input for a list of the number of assignments
assignments =  str(input("Enter assignments separated by commas: ")).split(",")
# get and process input for a list of grades
grades =  str(input("Enter grades separated by commas: ")).split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
#    message.format(names[i], assignments[i], grades[i])
    print(message.format(names[i], assignments[i], grades[i], int(grades[i])+int(assignments[i])*2))
    #print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
