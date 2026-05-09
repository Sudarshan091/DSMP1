task=[]
while True:
    choose=input('choose options:\n1 for viewing tasks\n2 for adding tasks \n3 for removing tasks\n4 for exiting the program ')
    if choose=='1':
        print(task)

    elif choose=='2':
        add=input('enter the task that you want to add: ')
        task.append(add)
        print(task)

    elif choose=='3':
        remove=input('enter the task that you wnat to remove:')
        if remove in task:
            task.remove(remove)
            print(task)
        else:
            print('task not found')
    elif choose=='4':
        print('exiting...')  
        break  
    else:
        print('invalid option')
            

            