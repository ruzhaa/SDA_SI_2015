import validation
import dynamic_programming
from branch_and_bound import BranchAndBound


class CLI:

    @staticmethod
    def input_max_weight():
        enter_n = input("Enter N kg: ")
        validation.validation_max_weight(enter_n)
        return enter_n

    @staticmethod
    def input_command():
        input_items = input("Enter item, weight and value or exit: ")
        split_text = input_items.split(" ")
        validation.validation_commands(split_text)
        return split_text

    def __init__(self):
        self.tuple_of_items = ()
        self.N = 0
        self.algorithm = None

    def __get_max_weight(self):
        return int(self.N)

    def __get_tuple(self):
        return self.tuple_of_items

    def create_tuple_of_items(self, item, weight, value):
        self.tuple_of_items += ((item, int(weight), int(value)), )

    def start_input(self):
        self.algorithm = input("Choose algorithm - dynamic programing (as dp) or branch&bound (as bb): ")
        self.N = CLI.input_max_weight()
        text_input = CLI.input_command()
        while text_input[0] != "exit" and text_input[0] != "EXIT":
            self.create_tuple_of_items(text_input[0],
                                       text_input[1],
                                       text_input[2])

            print("OK!!!")
            text_input = CLI.input_command()
        return self.tuple_of_items

    def start_indiana_jones(self):
        self.start_input()
        items = self.__get_tuple()
        limit = self.__get_max_weight()

        bagged = None

        if self.algorithm == "dp":
            bagged = dynamic_programming.knapsack_problem_dp(limit, items)
            val, weight = self.total_value_and_weight(bagged)
            print("for a total value of {} and a total weight of {}".\
                       format(val, weight))
            # self.print_dynamic_programming(bagged)
        elif self.algorithm == "bb":
            bagged = BranchAndBound.start_branch_and_bound(limit, items)
            self.print_branch_and_bound(bagged)

    # def print_dynamic_programming(self, bagged):

    @staticmethod
    def print_branch_and_bound(bagged):
        print("Items are \n  " + '\n  '.join(bagged[item] for item in range(len(bagged))))

    def total_value_and_weight(self, items_in_bag):
        ' Totalise a particular items_in_bagination of items'
        total_weight = total_value = 0
        for item, weight, val in items_in_bag:
            total_weight += weight
            total_value += val
        return (total_value, total_weight) if total_weight <= self.__get_max_weight() else (0, 0)



def main():
    indiana_jones = CLI()
    indiana_jones.start_indiana_jones()


if __name__ == '__main__':
    main()
