myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}

def calculateAverage(finalMarks):
    total=0

    for key in finalMarks:
        total = total+finalMarks[key]

    average = total/len(finalMarks)

    return average

print(calculateAverage(myFinalMarks))
