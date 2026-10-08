resources = [
    {"id": "R001", "name": "laptop", "category": "electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "keyboard", "category": "accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "headset", "category": "accessories", "total": 3, "available": 3}
]

follow = {
    "F001": "Ada", 
    "F002": "John", 
    "F003": "Grace"
}

borrow_amounts = {
    "F001": 2,
    "F002": 3,
}
 

for follow_id, name in follow.items():
    amount = borrow_amounts.get(follow_id, 0)
    for item in resources:
        print(f"{follow_id} ({name}) borrow {amount}: {item['name']} ({item['available']}: available)")


def borrow_item(tx, user_id, item_name, amount):
    item = next((r for r in resources if r["name"].lower() == item_name.lower()), None)
    if item and item["available"] >= amount:
                item["available"] -= amount      
                print(f"\n[Tx {tx}] {follow[user_id]} borrowed {amount} {item_name}.Available: {item['available']}")
            
    else:
                print(f"\n[Tx {tx}] {follow[user_id]} borrow {amount} {item_name} -> DANIED (insufficient stock)")

def return_item(tx, user_id, item_name, amount):
    item = next((r for r in resources if r["name"].lower() == item_name.lower()), None)
    if item and (item["available"] + amount <= item["total"]):
        item["available"] += amount
        print(f"\n[Tx {tx}] {follow[user_id]} returned {amount} {item_name}.Available: {item['available']}")
    else:
        print(f"\n[Tx {tx}] {follow[user_id]} return {amount} {item_name} -> DENIED")


def search_item(tx, item_name):
    item = next((r for r in resources if r["name"]. lower() == item_name.lower()), None)
    print(f"\n[Tx {tx}] Search '{item_name}': Found -> {item}" if item else f"\n[Tx {tx}]Search '{item_name}': Not Found")

def generate_report(tx):
    print(f"\n[Tx {tx}] --- FINAL REPORT ---")
    for r in resources:
        print(f"{r['name']}: {r['available']} available out of {r['total']}")

                        

borrow_item(1, "F001", "laptop", 2)
borrow_item(2, "F002", "keyboard", 3)
return_item(3, "F001", "laptop", 1)
borrow_item(4, "F003", "headset", 4)   
return_item(5, "F002", "keyboard", 4)  
search_item(6, "LAPtop")               
generate_report(7)