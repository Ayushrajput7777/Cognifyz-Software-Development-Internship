# Task 2: Number Patterns
n = int(input("Rows kitni? : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()