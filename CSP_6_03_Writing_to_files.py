import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    with open(fileName, "w") as file:
        for line in inputList:
            file.write(str(line) + "\n")
    with open(fileName, "r") as new:
        return new.read()


def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    li = []
    with open(fileName, "r") as file:
        for line in file:
            li.append(line)
        li.sort()
    with open(targetFile, "w") as file:
        for i in li:
            file.write(i)
    with open(targetFile, "r") as new:
        return new.read()

def highScore(newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all the scores in scores.txt
    with open("CSP_6_03_scores.txt", "a") as file:
        file.write(str(newScore) + "\n")
    li = []
    with open("CSP_6_03_scores.txt", "r") as file:
        for line in file:
            li.append(int(line))
        x = sum(li)
        y = len(li)
        avg = x / y
    return avg

