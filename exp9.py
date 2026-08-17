student_names=[]
student_marks=[]

while True:
    print("=" *40)
    print(" STUDENT MARKS MANAGEMENT SYSTEM")
    print("=" *40)
    print("1. insert student record")
    print("2. delete student record")
    print("3. update student marks")
    print("4. traverse/ display all records")
    print("5. search student")
    print("6. show statistics")
    print("7. exit")
    print("=" *40)

    choice = input("enter your choice(1-7): ").strip()

    #---------------insertion------------------

    if choice == '1':
            name = input("enter student name:").strip()

            if name in student_names:
                  print(f"student '{name} ' already exits! use update option insted.\n")
            else:
                  marks = float(input(f"enter marks of {name}:"))
                  student_names.append(name)
                  student_marks.append(marks)
                  print(f"record for '{name}' inserted successfully.\n")

    elif choice =="2" :
          name = input("enter student name to delete:").strip()

          if name in student_names:
                index = student_names.index(name)
                student_names.pop(index)
                student_marks.pop(index)
                print(f"record for '{name}' deleted successfully.\n")
          else:
                print(f"student '{name}' not found.\n")      

    elif choice =="3":            
          name = input("enter student name to update:").strip()

          if name in student_names:
                index = student_names.index(name)
                new_marks = float(input(f"enter new marks for {name}:"))
                student_marks[index] = new_marks
                print(f"marks for '{name}' update successfully.\n")

          else:
                print(f"student '{name}' not found.\n")      


    elif choice =="4":
          if len(student_names)== 0:
                print("no records to display.\n")

          else:
                print("\n{:<5} {:<20} {:<10}".format("no.", "name", "marks"))      
                print("-" *35)
                for i in range(len(student_names)):
                    print("{:<5} {:<20} {:<30}". format(i+1, student_names[i],student_marks[i]))
                print()

    elif choice == "5":
          name = input("enter the student name to search :").strip()

          if name in student_names:
                index = student_names.index(name) 
                print(f"{name} -> marks: {student_marks[index]}\n")                     
          else:
                print(f"student '{name}' not found.\n")  


    elif choice == "6":
          if len(student_marks) == 0:
                print("no records available for statistics.\n")
          else:
                total = sum(student_marks)
                average = total /len(student_marks)
                highest = max(student_marks)
                lowest = min(student_marks)

                topper_index = student_marks.index(highest)
                weakest_index = student_marks.index(lowest)     

                print("\n-------class statistics------")
                print(f"total students : {len(student_names)}")
                print(f"average marks  : {average:.2f}") 
                print(f"highest marks  :  {highest} (student: {student_names[topper_index]})")
                print(f"lowest marks  :  {lowest} (student: {student_names[weakest_index]})")
                print()


    elif choice == '7':
          print("exiting program. thank you!")           
          break

    else:
          print("invalid choice. please enter a number between 1 and 7.\n")
                      
          
          