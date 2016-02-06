class BranchAndBound:

    def __init__(self, limit, items, level, benefit, weight, token=[]):
        self.max_weight = limit
        self.data_sorted = items
        self.level = level
        self.benefit = benefit
        self.weight = weight
        self.token = token
        self.upperbound_var = self.upperbound(self.token[:self.level]+[1]*(len(self.data_sorted)-level))

    def upperbound(self, available):
        upperbound = 0
        weight_accumulate = 0
        for avail, item in zip(available, self.data_sorted):
            item_weight = item[1]
            item_value = item[2]
            if item_weight * avail <= self.max_weight - weight_accumulate:
                weight_accumulate += item_weight * avail
                upperbound += item_value * avail
            else:
                upperbound += item_value*(self.max_weight - weight_accumulate)/item_weight*avail
                break
        return upperbound

    def develop(self):
        level = self.level + 1
        _, weight, value = self.data_sorted[self.level]
        left_weight = self.weight + weight
        if left_weight <= self.max_weight:
            left_benefit = self.benefit + value
            # dobavqm che elem e vzet -> stava [1]
            left_token = self.token[:self.level]+[1]+self.token[level:]
            left_child = BranchAndBound(self.max_weight,
                                        self.data_sorted,
                                        level,
                                        left_benefit,
                                        left_weight,
                                        left_token)
        else:
            left_child = None
        right_child = BranchAndBound(self.max_weight,
                                     self.data_sorted,
                                     level,
                                     self.benefit,
                                     self.weight,
                                     self.token)
        return ([] if left_child is None else [left_child]) + [right_child]

    @staticmethod
    def start_branch_and_bound(limit, items):
        list_with_items = sorted(items, key=lambda k: float(k[2])/k[1])
        list_with_items.reverse()

# self, max_weight, items, level, benefit, weight, token=[])
        root = BranchAndBound(limit, list_with_items, 0, 0, 0, [0]*len(list_with_items))
        tree_with_nodes = []

        current_node = root

        while current_node.level < len(list_with_items):
            tree_with_nodes.extend(current_node.develop())
            # sortira i trugva po po-golemiq node
            tree_with_nodes.sort(key=lambda x: x.upperbound_var)
            # chrez pop vzima po-golemiq
            current_node = tree_with_nodes.pop()

        return [item for token, (item, _, _)
                in zip(current_node.token, list_with_items) if token == 1]
