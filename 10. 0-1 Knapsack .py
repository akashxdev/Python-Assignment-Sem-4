def knapsack(W, wt, val, n):
   
    def knapsack_helper(remaining_weight, items):
        if not items or remaining_weight == 0:
            return 0
        elif wt[items[0]] > remaining_weight:
            return knapsack_helper(remaining_weight, items[1:])
        else:
            item_index = items[0]
            remaining_items = items[1:]
            value_with_item = val[item_index] + knapsack_helper(remaining_weight - wt[item_index], remaining_items)
            value_without_item = knapsack_helper(remaining_weight, remaining_items)
            return max(value_with_item, value_without_item)
        
    items = list(range(n))
    items.sort(key=lambda x: val[x] / wt[x], reverse=True)
    return knapsack_helper(W, items)
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = len(wt)
print(knapsack(W, wt, val, n))  
