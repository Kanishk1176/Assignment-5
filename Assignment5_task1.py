student = {"Alice": 85,"Carol": 97}
student_list = [i for i in student]
print("The students whose data is available are:",student_list)
student_name = str(input("Enter the student's name: " ))
if student_name in student:
    print(f"{student_name}'s marks: {student[student_name]}")
else:
    print("Student not found.")
 
