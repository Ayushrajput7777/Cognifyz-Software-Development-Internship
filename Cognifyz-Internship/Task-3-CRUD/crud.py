# Task 3: CRUD - Task Manager
tasks = []

while True:
    print("\n1.CREATE 2.SHOW 3.UPDATE 4.DELETE 5.EXIT")
    ch = input("Choice: ")
    if ch == '1':
        tasks.append(input("Task naam: "))
        print("Added!")
    elif ch == '2':
        print(tasks if tasks else "Empty")
    elif ch == '3':
        for i, t in enumerate(tasks): print(f"{i}. {t}")
        idx = int(input("Kaunsa update? index: "))
        tasks[idx] = input("Naya naam: ")
    elif ch == '4':
        idx = int(input("Kaunsa delete? index: "))
        tasks.pop(idx)
        print("Deleted!")
    elif ch == '5':
        break