# B4. Mutating a list during iteration
# Identify the problem, explain its consequences and rewrite the function correctly.

resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]
for resource in resources:
    if resource["available"] == 0:
        resources.remove(resource)
print(resource)

print()


# B3. Aggregate transaction data*
# Write a function that returns a dictionary of the total quantity per fellow, 
# without hardcoding results.

transactions = [
         {"fellow": "Ada", "quantity": 2 },
         {"fellow": "John", "quantity": 4},
         {"fellow": "Ada",  "quantity": 3},
         {"fellow": "Grace", "quantity": 1},
         {"fellow": "John", "quantity": 2}
    ] 
total = {}
for transaction in transactions:
    if transaction["quantity"] == 0:
        transactions. remove(transaction)
        continue
    name = transaction["fellow"]
    quantity = transaction["quantity"]

    total[name] = total.get(name, 0) + quantity

for fellow, total_quantity in total.items():
    print(f"{fellow}: {total_quantity}")
# B2. Diagnose and repair a borrowing bug
# Identify the problem, explain its consequences and rewrite the function correctly.



def borrow(resource, quantity):
    resource["available"] -= quantity
    if resource["available"] < 0:
        return "Not enough stock"
    resource["available"] -= quantity
    return "Success"

item = {"name": "headset", "available": 3}
print(borrow(item, 5))
print(item["available"]) 
print(borrow(item, 2))  
print(item["available"]) 
