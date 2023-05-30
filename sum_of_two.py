Numbers = [3, 3, 6 ]
target = 6
length = len(Numbers)


def constraints(input_list, num):
    for i in range(length):
        x = isinstance(Numbers[i - 1], int)
        if not x:
            return print("Please enter an integer in your list")

    if min(input_list) <= -1000 or max(input_list) >= 1000:
        print("Numbers not between -1000 and 1000")
        return False

    elif length < 2 or length >= 10:
        print("Length of Array not between 2 and 10")
        return False

    elif num >= 1000 or num <= -1000:
        print("Tag not between -1000 and 1000")
        return False
    else:
        return True


def sum_of_two(li, number):
    new_list = []
    while constraints(li, number):
        for i in range(length - 1):
            for j in range(i + 1, length):
                if Numbers[i] + Numbers[j] == number:
                    new_list.append([i, j])
        if len(new_list) > 1:
            return print("Only one valid answer exists. Your input has at least two possible solutions")

        elif len(new_list) == 0:
            return print("There is no no match")
        else:
            return print(new_list[0])


sum_of_two(Numbers, target)
