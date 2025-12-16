with open('Data.txt', 'r') as fp:
    Data = fp.readlines()


def starts_with_zero(data:str) -> bool:
    return data.startswith('0') if data else False
if starts_with_zero ==True:
    print("Starts with zero:", starts_with_zero)
else:
    print("No values starting with zero.")



def find_doubles(sequence):
    doubles = []
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            doubles.append((sequence[i], i, i + 1))
    return doubles

result = find_doubles(Data)
print("Doubles found:")
for num, start, end in result:
    print(f"Number {num} at positions {start} and {end}")



