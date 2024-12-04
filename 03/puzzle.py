###################################
#          Advent of Code         #
# Day: 03 | Completed: 12/03/2024 #
###################################



# ===== Support Functions ===== #
def get_all_positions(text):
    positions = []

    # Find multiply statements
    for match in re.finditer(r'mul\(\d+,\d+\)', text):
        nums = match.group()[4:-1].split(",")
        positions.append(('mul', match.start(), int(nums[0]) * int(nums[1])))
    
    # Find do() statements
    for match in re.finditer(r'do\(\)', text):
        positions.append(('do', match.start(), 0))
    
    # Find don't() statements
    for match in re.finditer(r"don't\(\)", text):
        positions.append(('dont', match.start(), 0))
    
    # Sort by position
    return sorted(positions, key=lambda x: x[1])
# ============================= #



# ===== Solve ===== #
# Part 1
def solvePart1(d):
    pattern = r'mul\(\d+,\d+\)'
    total = 0
    matches = re.findall(pattern, d) 
    for match in matches:
        nums = match[4:-1].split(",")
        total += (int(nums[0])*int(nums[1]))
    return total

# Part 2
def solvePart2(d):
    instructions = get_all_positions(d)
    enabled = True 
    total = 0
    
    for inst_type, pos, value in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            total += value
    
    return total

# ================= #

# ===== Setup ===== #
# Modules
import re

# Variables
data = []

# Read the input file
input_file = open("input","r")
for line in input_file:
    data.append(line)
# ================= #

# ===== Show Solution ===== #
print("Part 1: " + str(solvePart1(''.join(data))))
print("Part 2: " + str(solvePart2(''.join(data))))
# ========================= #