with open('Data.txt', 'r') as int:
    Data = int.read()


def part1(Data: str):
    ranges = (Data)
    invalid_ids = []
    for prod_id_range in ranges:
        for prod_id in range(prod_id_range[0], prod_id_range[1] + 1):
            prod_id_str = str(prod_id)
            id_len = len(prod_id_str)
            if id_len % 2 != 0: # odd numbers of digits can't contain invalid IDs
                continue
            if prod_id_str[0:id_len//2] == prod_id_str[id_len//2:id_len]:
                invalid_ids.append(prod_id)

    return sum(invalid_ids)
