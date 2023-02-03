num = int(input("Please enter a num:"))
if num <= 0:
    print("Please enter a valid choice.")
if num == 1:
     print('Process complete.')
elif num > 1:
   while num > 1:
    if num == 6:
        num -= 1
    print(num)
    if num > 1 and num != 6:
        print(num)
        num -= 1
elif num == 1:
    print(num)
    print('Process complete.')
