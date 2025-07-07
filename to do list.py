print("TO-DO LIST")
choose=int(input("""Choose your operation number
1.Add task
2.Show task
3.Mark done
4.Delete task
Enter your operation number="""))
task_list=["1.wake up fast",
"2.eat healty",
"3.call manager",
"4.reach goals"]
def display_task_in_list():
    for tasks in task_list:
       print(tasks)
    
def add_task():
    a=input("Enter the task you want to add (task with serial number): ")
    task_list.append(a)
    print("Your updated tasks")
    display_task_in_list()
    add_another_task()
    further_step_if_want()
     
def add_another_task():
    another_task=str(input("* want to add another task? yes or no:"))
    if another_task=="yes":
        add_task()
    elif another_task=="no":
        print("Your updated tasks")
        display_task_in_list()
    else:
        print( "invalid! please type yes OR no (in lowercase)")
        add_another_task()
        
def further_step_if_want():
    further_step=str(input("* want to perfrom more operations on updated task? yes or no:"))
    if further_step=="yes":
       more_operation=int(input('''Enter the opertion you want to perfrom on the updated task.
    2.show task or 3.mark done or 4.delete task:'''))
       if more_operation ==2:
         show_task()
         further_step_if_want()
       elif more_operation==3:
         mark_done()
         further_step_if_want()
       elif more_operation==4:
         remove_task()
         further_step_if_want()
       else:
         print("invalid! choose only between 2-4 ")
         further_step_if_want()
         
    elif further_step=="no":
        print("your final updated task list!")
        return display_task_in_list()
    else:
        print( "invalid! please type yes OR no (in lowercase)")
        further_step_if_want()
        
        
        
def show_task():
        print("your task list is here!")
        display_task_in_list()
        
def mark_done():
    display_task_in_list()
    status=int(input("Enter the task number which you want to mark as done:"))
    if status in range(1,len(task_list)+1):
        task_list[status-1]=task_list[status-1] +  " X"
        display_task_in_list()
        want_to_mark_done_other_task()
    else:
        print("invalid! choose btetween the task number")
        mark_done()
def want_to_mark_done_other_task():
    ans=str(input("* want to mark more tasks(yes or no):"))
    if ans=="yes":
        mark_done()
    elif ans=="no":
        return display_task_in_list()
    else:
        print( "invalid please type yes OR no (in lowercase)")
        mark_done()
        
def remove_task():
    remove_no=int(input("Enter the task number you want to remove:"))
    if remove_no in range(1,len(task_list)+1):
      removed = task_list.pop(remove_no - 1)  
      display_task_in_list()
      want_to_remove_other_task()
    else:
        print(f"invalid!choose only between 1-{len(task_list)}")
        remove_task()

def want_to_remove_other_task():
    remove_other_task=str(input("* want to remove tasks(yes or no):"))
    if remove_other_task=="yes":
        remove_task()
    elif remove_other_task=="no":
         display_task_in_list()
    else:
        print( "invalid please type yes OR no (in lowercase)")
        remove_task()
    
         
   
      
        
if choose==1:
    add_task()
elif choose==2:
    show_task()
elif choose==3:
    mark_done()
elif choose==4:
    remove_task()
else:
    print("invalid! choose only between 1-4")