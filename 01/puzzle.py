##################################
#          Advent of Code        #
# Day: 1 | Completed: 12/01/2024 #
##################################



# ===== Setup ===== #
input_file = open("input","r")
list1,list2 = [],[]
distance,similarity = 0,0
for line in input_file:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()
# ================= #



# ===== Solve ===== #
# Part 1
for i in range(len(list1)):
    distance += abs(list1[i]-list2[i])

print("Total Distance: " + str(distance))

# Part 2
for i in list1:
    count = 0
    for x in list2:
        if x == i:
            count += 1
    
    similarity += (i*count)

print("Similarity Score: " + str(similarity))
# ================= #