# color_list = ["Red", "White", "Black"]
# print(color_list[0])
# print(color_list[-1])
#
# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1
#
# i = 10
# while i >= 0:
#     print(i * "*")
#     i -= 1
#
# random = 8
# while True:
#     line = int(input('Your guess:'))
#     if line == random:
#         print('Correct')
#         break
#     print(line)

# x = range(6)
# for n in x:
#     print(n)

# x = range(3, 20)
# for n in x:
#     print(n)
#
# x = range (10, 100, 5)
# for n in x:
#     print(n)

n = 10;
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')


for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')



