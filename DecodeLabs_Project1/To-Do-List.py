#Poject 1: To-Do List
#DecodeLabs Industrial Trainig Kit


tasks=[]
print("TO-DO List")
print("1.Add Task")
print("2.View task")
print("3.Delete")
print("4.Exit")
while True:
    choice=input("Enter your choice")
    if(choice=="1"):
        task=input("Enter the Task")
        tasks.append(task)
        print("           Task added Successfully")
    elif(choice=="2"):
        if len(tasks)==0:
            print("No tasks added")
        else:
            for i,j in enumerate(tasks,start=1):
                print(f"         {i}.{j}")
    elif(choice=="3"):
        if len(tasks)==0:
            print("No Tasks to delete")
        else:
            print("            Your Tasks")
            for i,j in enumerate(tasks,start=1):
                print(f"        {i}.{j}")
            try:
                num=int(input("Enter the task number you want to delete"))
                if num>=0 and num<=len(tasks):
                    delete=tasks.pop(num-1)
                    print(f"'{delete}' Deleted Successfully")
                else:
                    print("Invalid task Number")
            except ValueError:
                print("Enter a valid number")
    elif(choice=="4"):
        print("You have successfully exited from the list")
        break
    else:
        print("Invalid Choice.Please Try Again")
        
        
    
