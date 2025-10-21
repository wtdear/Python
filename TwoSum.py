# === Two Sum - Python ===

def TwoSum():

    list = [9, 2, 13, 16, 10]
    target = 18

    list_map = {}

    for index, number in enumerate(list):
        result = target - number
        if result in list_map:
            return [list_map[result], index]

        list_map[number] = index
    return[]
result = TwoSum()
print(result)