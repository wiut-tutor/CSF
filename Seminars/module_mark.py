#Use f-string, input(), int() functions to calculate mark for the CSF module.

# cw_mark = 50
# exam_mark = 80
# total_mark = 0.4*cw_mark+0.6*exam_mark
# print(total_mark)
#
# #modified version
# moduleName = input("Enter module Name:" )
n = int(input("Enter number of components: "))

def components(n, totalmark):
    if n<=0:
        print("Finished calculating for ")
    else:
        component_mark = int(input("Enter mark for component "+str(n)))
        component_weight = float(input("Enter cw weighting "))
        submark = component_mark * component_weight
        print(submark)
        total_mark = totalmark+submark
        print(total_mark)
        print(n)
        components(n-1, totalmark)

components(n, 0)

# exam_mark = int(input("Enter mark for exam "))
# exam_weight = float(input("Enter exam weighting "))


#keep in mind there is no validation in place

