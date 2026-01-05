with open('Data.txt', 'r') as file:
    data = file.read().strip()
    
    ranges = [list(map(int, item.split("-"))) for item in data.split(",")]
#print(ranges)


#Part 1

values = sum((list(range(a, b + 1)) for a, b in ranges), [])
#print(values)


counter = 0 
for value in values:
    str(value)
    if len(str(value)) % 2 == 0 and str(value)[:len(str(value)) // 2] * 2 == str(value):
    # checking if number is even           checking if both halves are equal 
        counter += value
print("Part 1:", counter)
#I got a star!!!
# Ans: 22062284697


#Part 2

values = sum((list(range(a, b + 1)) for a, b in ranges), [])

counter_2 = 0
for value in values:
    str(value)
    for k in range(2, len(str(value)) + 1):
        if len(str(value)) % k == 0 and str(value)[:len(str(value)) // k] * k == str(value):
# checking if the number divided by anything between 2 and the length of the number are all equals by replacing 2 with k
            counter_2 += value
            break
print("Part 2:", counter_2)


#P2A1 = 46719601268 (Too high)
#P2A2 = 46647025515 (Too low)
# Star 2
# Ans: 46666175279
