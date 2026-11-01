subjects=('Python','Maths','DBMS')
print(f"subjects: {subjects}")
student=int(input("How many students?"))
marks=[]
student_ids=[]
students={}


for i in range(student):
    student_id=input("Student ID: ")
    student_id.upper()
    if student_id=="":
        print("student ID cannot be empty")
    else:
        student_ids.append(student_id)
    name=input("Name: ") 
    
    while(True):
       marks1=int(input("Python marks: "))
       if marks1>0 and marks1<=100:
         marks.append(marks1)
         break
       else:
          print("enter valid marks")
    while(True):
       marks2=int(input("Maths marks: "))
       if marks2>0 and marks2<=100:
          marks.append(marks2)
          break
       else:
          print("enter valid marks")
    while(True):
       marks3=int(input("DBMS marks: "))
       if marks3>0 and marks3<=100:
          marks.append(marks3)
          break
       else:
          print("enter valid marks")
    students[student_id]={
   'name':name,
   'marks':[marks1,marks2,marks3]
}

print("-----STUDENT REPORT-----")
for id in student_ids:
   print(f"{id} | {students[id]['name']}")
   print(f"Python:{students[id]['marks'][0]}, Maths:{students[id]['marks'][1]}, DBMS:{students[id]['marks'][2]}")
   total=students[id]['marks'][0]+students[id]['marks'][1]+students[id]['marks'][2]
   average=int((students[id]['marks'][0]+students[id]['marks'][1]+students[id]['marks'][2])/3)
   if average>=75:
      result="Distinction"
   elif average>=40:
      result="pass"
   else:
      result="fail"
   print(f"Total: {total} | Average: {average} | Result: | {result}\n\n")

#search and inspect
print("===for search student details by there id===")
student_id=input("enter student id: ")
print(students[student_id])

#student id showing using list slicing
print(f"student ID are: {student_ids[0:2]}")

#set operations
student_passed=set()
for record in students.values():
   for i in range(len(subjects)):
      if record['marks'][i]>=40:
         student_passed.add(subjects[i])
print(f"set of subjects at least one student passed: {sorted(student_passed)}\n")

#to find union, intersection,difference,symmetric difference of to sets of subjects passed by two selected students
print("total student id are: ",student_ids)
id1 = input("enter first student id: ")
s1 = set()
for i in range(len(subjects)):
	if students[id1]['marks'][i] >= 40:
		s1.add(subjects[i])
print(f"subject passed by {id1}: {sorted(s1)}")
id2 = input("enter second student id: ")
s2 = set()
for i in range(len(subjects)):
	if students[id2]['marks'][i] >= 40:
		s2.add(subjects[i])
print(f"subject passed by {id2}: {sorted(s2)}\n")
print("union: ",sorted(s1|s2))
print("inersection: ",sorted(s1&s2))
print("difference: ",sorted(s1-s2))
print("symmetric difference: ",sorted(s1^s2))