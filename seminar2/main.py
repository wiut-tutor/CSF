# Task 5
# num = int(input("Enter the number: "))
# print(num)
# print(oct(num))
# print(hex(num))
# Task 6
# num = int(input("Enter the number: "))
# if num % 2 == 1:
#     print("odd")
# else:
#     print("even")
#
# def converter(num):
#     print(num)
#     print(oct(num))
#     print(hex(num))
#
#
# # num = int(input("Enter the number: "))
# converter(10)
# converter(111)

#function  definition  with parameters
def even_odd(number):
    if number % 2 == 1:
        print(number, " is odd")
    else:
        print(number, " is even")


num = int(input("Enter the number: "))
print(even_odd(num)) #function argument is num, even_odd() function call takes place here

print("new update")