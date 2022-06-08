def find(word, letter, index):
    while index <len(word):
        if word[index]==letter:
            return index
        index =index+1
    return -1

print(find('banana', 'a', 2))




# Task 5

def test_is_valid(test):
    if (isinstance(test, int) == True) and (1 <= test <= 3):
        return True
    else:
        return False


print(test_is_valid(2))
print(test_is_valid(3))
print(test_is_valid(4))
print(test_is_valid(4.0))

# Task 4
# def compare (x, y):
#     if x < y:
#         return -1
#     elif x >y:
#         return 1
#     elif x==y:
#         return 0
#
# print(compare(1, 4))
# print(compare(4, 1))
# print(compare(3, 3))


# def fancy_hello_world():
#     fancy_string = """
# ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
# ───█▒▒░░░░░░░░░▒▒█───
# ────█░░█░░░░░█░░█────
# ─▄▄──█░░░▀█▀░░░█──▄▄─
# █░░█─▀▄░░░░░░░▄▀─█░░█
# Triple quotes allow to span string across multiple lines
# """
#     print(fancy_string)
#
#
# fancy_hello_world()
#
# def fancy_hello_world2():
#     fancy_string = """
# ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
# ───█▒▒░░░░░░░░░▒▒█───
# ────█░░█░░░░░█░░█────
# ─▄▄──█░░░▀█▀░░░█──▄▄─
# █░░█─▀▄░░░░░░░▄▀─█░░█
# Triple quotes allow to span string across multiple lines 2
# """
#     return fancy_string
#
#
#
# print(fancy_hello_world2())


#     print(fancy_string)
#
# fancy_hello_world()
#
# def fancy_hello_world2():
#     fancy_string = """
# ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
# ───█▒▒░░░░░░░░░▒▒█───
# ────█░░█░░░░░█░░█────
# ─▄▄──█░░░▀█▀░░░█──▄▄─
# █░░█─▀▄░░░░░░░▄▀─█░░█
# """
#     return(fancy_string)
#
# print(fancy_hello_world2())

#
# def compare(x, y):
#     if x > y:
#         return 1
#     elif x < y:
#         return -1
#     elif x == y:
#         return 0
#
#
# print(compare(3, 4))
#

# def test_is_valid(test):
#     if (isinstance(test, int) == True) and (1 <= test <=3):
#         return True
#     else:
#         return False
