from typing import List, Tuple

def fractional_knapsack(capacity: float, items: List[Tuple[float, float]]) -> float:
    
    # Sort the items by their value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda item: item[1]/item[0], reverse=True)
    
    # Define a function that will calculate the maximum value that can be carried by a given weight
    def max_value(weight: float) -> float:
        total_value = 0
        remaining_weight = weight
        
        # Iterate over the sorted items, adding them to the knapsack as much as possible
        for item_weight, item_value in sorted_items:
            if item_weight <= remaining_weight:
                total_value += item_value
                remaining_weight -= item_weight
            else:
                fraction = remaining_weight / item_weight
                total_value += fraction * item_value
                break
        
        return total_value
    
    # Return the maximum value that can be carried in the knapsack
    return max_value(capacity)
    
print("Akash Sarkar")
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print(max_value)  
