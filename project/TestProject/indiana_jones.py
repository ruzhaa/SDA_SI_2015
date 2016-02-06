class CLI:

    @staticmethod
    def validation_n(number):
        try:
            number == int(number)
        except (TypeError, ValueError):
            raise TypeError("Error type!")

    @staticmethod
    def validation_commands(split_text):
        if split_text[0] == "exit" or split_text[0] == "EXIT":
            return True
        if len(split_text) != 3:
            raise Exception("Your input is not validation!")
        item = split_text[0]
        value = split_text[1]
        weight = split_text[2]

        if item.isdigit():
            raise TypeError("Error type!")
        try:
            item == str(item)
            value == int(value)
            weight == int(weight)
        except (TypeError, ValueError):
            raise TypeError("Error type!")

    @staticmethod
    def input_n():
        enter_n = input("Enter N kg: ")
        CLI.validation_n(enter_n)
        return enter_n

    @staticmethod
    def input_command():
        text = input("Enter item, value and weight or exit: ")
        split_text = text.split(" ")
        CLI.validation_commands(split_text)
        return split_text

    def __init__(self):
        self.dict_of_items = dict()
        self.N = 0

    def create_dict_of_value_and_weight(self, item, value, weight):
        self.dict_of_items[item] = (int(value), int(weight))
        return self.dict_of_items

    def get_dict(self):
        return self.dict_of_items

    def get_n(self):
        return int(self.N)

    def start(self):
        self.N = CLI.input_n()
        text_input = CLI.input_command()
        while text_input[0] != "exit" and text_input[0] != "EXIT":
            self.create_dict_of_value_and_weight(text_input[0],
                                                 text_input[1],
                                                 text_input[2])
            print("OK")
            text_input = CLI.input_command()
        return self.dict_of_items


class IndianaJones:

    def __init__(self):
        cli = CLI()
        self.dict_from_input = cli.start()
        self.list_of_items = []
        self.n = cli.get_n()
        self.carried_items = []

    def dict_to_list(self):
        for item in self.dict_from_input:
            self.list_of_items.append(self.dict_from_input[item])

        self.list_of_items = sorted(self.list_of_items)
        self.list_of_items.reverse()

        return self.list_of_items

    def get_key_from_dict(self, value):
        for key in self.dict_from_input:
            if self.dict_from_input[key] == value:
                return key

    def knapsack_problem(self):
        self.dict_to_list()

        for item in self.list_of_items:
            if item[1] <= self.n:
                self.carried_items.append(self.get_key_from_dict(item))
                self.n -= item[1]

        return self.carried_items


# def main():
#     ij = IndianaJones()
#     print(ij.knapsack_problem())


# if __name__ == '__main__':
#     main()
