class CLI:

    @staticmethod
    def validation_max_weight(number):
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

    @staticmethod
    def input_max_weight():
        enter_n = input("Enter N kg: ")
        CLI.validation_max_weight(enter_n)
        return enter_n

    @staticmethod
    def input_command():
        input_items = input("Enter item, weight and value or exit: ")
        split_text = input_items.split(" ")
        CLI.validation_commands(split_text)
        return split_text

    def __init__(self):
        self.tuple_of_items = ()
        self.N = 0

    def create_tuple_of_items(self, item, weight, value):
        self.tuple_of_items += ((item, int(weight), int(value)), )

    def start_input(self):
        self.N = CLI.input_max_weight()
        text_input = CLI.input_command()
        while text_input[0] != "exit" and text_input[0] != "EXIT":
            self.create_tuple_of_items(text_input[0],
                                       text_input[1],
                                       text_input[2])

            print("OK!!!")
            text_input = CLI.input_command()
        return self.tuple_of_items

    def get_max_weight(self):
        return int(self.N)


class IndianaJones:

    def __init__(self):
        cli = CLI()
        self.tuple = cli.start_input()
        self.max_weight = cli.get_max_weight()

    def knapsack_problem_dp(self):

        items = self.tuple
        limit = self.max_weight

        # 1) create table only with 0
        # 2) generation table with new value from tuple_of_items
        # * items[j-1] -> item, wt, val (from tuple)

        table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

        for j in range(1, len(items) + 1):
            item, wt, val = items[j-1]
            for w in range(1, limit + 1):
                if wt > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w], val + table[j-1][w-wt])

        result = []

        for j in range(len(items), 0, -1):
            # return in the previous row
            if table[j][limit] != table[j-1][limit]:
                item, wt, val = items[j-1]
                result.append(items[j-1])
                limit -= wt

        return result

    def total_value_and_weight(self, items_in_bag):
        totwt = totval = 0
        for item, wt, val in items_in_bag:
            totwt += wt
            totval += val
        return (totval, -totwt) if totwt <= self.max_weight else (0, 0)

    def start_indiana_jones(self):
        bagged = self.knapsack_problem_dp()
        print("Items are \n  " +
              '\n  '.join(item for (item, wt, val) in bagged))
        val, wt = self.total_value_and_weight(bagged)
        print("for a total value of %i and a total weight of %i" % (val, -wt))


def main():
    ij = IndianaJones()
    ij.start_indiana_jones()


if __name__ == '__main__':
    main()
