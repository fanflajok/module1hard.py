students={}
students = {"Johny", "Bilbo", "Steave","Khendrik", "Aaron"}
students = list(students)
students.sort()
grades=[]
grades= [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades[0]=sum(grades[0])/len(grades[0])
grades[1]=sum(grades[1])/len(grades[1])
grades[2]=sum(grades[2])/len(grades[2])
grades[3]=sum(grades[3])/len(grades[3])
grades[4]=sum(grades[4])/len(grades[4])
students_and_grades=dict(zip(students, grades))
print(students_and_grades)
