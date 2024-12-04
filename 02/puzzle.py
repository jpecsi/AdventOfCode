###################################
#          Advent of Code         #
# Day: 02 | Completed: 12/03/2024 #
###################################



# ===== Setup ===== #
# Modules
import copy

# Variables
data = []

# Read the input file
input_file = open("sample","r")
for line in input_file:
    data.append(line)
# ================= #



# ===== Support Functions ===== #
def checkAllIncreasing(x):
    success,first = True,True
    previous = 0

    for num in x:
        if first:
            previous = int(num)
            first = False
        else:
            if success:
                if (previous-int(num)) < 0:
                    previous = int(num)
                else:
                    success = False
                    return False
    
    return True

def checkAllDecreasing(x):
    success,first = True,True
    previous = 0

    for num in x:
        if first:
            previous = int(num)
            first = False
        else:
            if success:
                if (previous-int(num)) > 0:
                    previous = int(num)
                else:
                    success = False
                    return False
    
    return True

def checkSafeReports(x):

    success,first = True,True
    previous = 0

    for num in x:
        if first:
            previous = int(num)
            first = False
        else:
            if success:
                if abs(previous-int(num)) <= 3 and abs(previous-int(num)) > 0:
                    previous = int(num)
                else:
                    return False
    
    return True
# ============================= #



# ===== Solve ===== #
# Part 1
def solvePart1():
    safe_reports = 0
    for report in data:
        line = report.split()

        if checkAllIncreasing(line) or checkAllDecreasing(line):
            if checkSafeReports(line):
                safe_reports += 1

    return safe_reports

        
        

# Part 2
def solvePart2():
    safe_reports = 0
    
    for report in data:
        line = report.split()
        dampen = True
        if (checkAllIncreasing(line) or checkAllDecreasing(line)) and checkSafeReports(line):
            safe_reports += 1
        else:
            print("Working List: " + str(line))
            for idx,num in enumerate(line):
    
                if dampen:
                    work = copy.deepcopy(line)
                    try:
                        work.pop(idx+1)
                        print(work)
                        if (checkAllIncreasing(work) or checkAllDecreasing(work)) and checkSafeReports(work):
                            print("ADDED")
                            safe_reports += 1
                            dampen = False
                    except:
                        dampen = False

    return safe_reports
# ================= #


# ===== Show Solution ===== #
print("Part 1: " + str(solvePart1()))
print("Part 2: " + str(solvePart2()))
# ========================= #
