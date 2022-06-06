# Slide 17
# cheeses = ['cheddar', 'edam', 'gouda']
# numbers = [14,45,8]
# empty = []
# mixed = [14,45,8,['cheddar', 'edam', 'gouda']]
#
# print(cheeses, numbers, empty, mixed)
# print (cheeses[0])
#
# print('Edam' in cheeses)
# print('edam' in cheeses)

# Task 5
# i = 1
# while i <=10:
#     print(i*"*")
#     i+=1

#Task 6
# i = 10
# while i>=0:
#     print(i*"*")
#     i-=1

# WHILE COUNTDOWN
# # def countdown(n):
# #     if n <= 0:
# #         print('Finish!')
# #     else:
# #         print(n)
# #         print("*"*n)
# #         countdown(n-1)#call itself recursion happens
# #
# # countdown(10)# call the function first time

#Task 7
# random = 8
# while True:
#    line = int(input('Your guess:'))
#    if line == random:
#        print('Correct')
#        break
#    print(line)

subjects= ["CSF", "FunPro", "WT"]
for x in subjects:
  print(x)

for x in range(6):
  print(x)

for x in range(3,6):
  print(x)

x = range(3, 10, 2)
for n in x:
  print(n)

color_list = ["Red","Green","White" ,"Black"]
print((color_list[0],color_list[-1]))
# print(color_list[0])
# print(color_list[3])
# print(color_list[-1])
# print(color_list[-2])


print('new')
n=10;
for i in range(n):
   for j in range(i):
       print ('* ', end="")
   print('')

for i in range(n, 0, -1):
   for j in range(i):
       print ('* ', end="")
   print('')


# secret = 7
#
# while True:
#     line = input('Guess the number <@-@> ')
#     if int(line) == secret:
#         break
#         print('Correct!')


def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


