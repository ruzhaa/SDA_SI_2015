def validation_max_weight(number):
    try:
        number == int(number)
    except (TypeError, ValueError):
        raise TypeError("Error type!")


def validation_commands(split_text):
    if split_text[0] == "exit" or split_text[0] == "EXIT":
        return True
    if len(split_text) != 3:
        raise Exception("Your input is not validation!")
    item = split_text[0]
    weight = split_text[1]
    value = split_text[2]

    if item.isdigit():
        raise TypeError("Error type!")
    try:
        item == str(item)
        weight == int(weight)
        value == int(value)
    except (TypeError, ValueError):
        raise TypeError("Error type!")
