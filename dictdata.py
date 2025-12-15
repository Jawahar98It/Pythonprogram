balance = {
    "Samuel": 1500.75,
    "Raj": 1200.50,
    "John":200000.00,
    "Emma": 2500.00,
    "Olivia": 3000.25,
    "Liam": 1800.00}
print(balance)
print(type(balance))

#accessing values using keys
print("Balance of Samuel is:", balance["Samuel"])
print("Balance of Raj is:", balance["Raj"])
print("Balance of John is:", balance["John"])

#accessing values using get() method
print("Balance of Samuel is:", balance.get("Samuel"))
print("Balance of Raj is:", balance.get("Raj"))
print("Balance of John is:", balance.get("John"))

#modifying values
balance["Samuel"] = 2000.00
print("After modifying, Balance of Samuel is:", balance["Samuel"])
balance["Raj"] = balance["Raj"] + 500.00
print("After modifying, Balance of Raj is:", balance["Raj"])
balance["John"] += 10000.00
print("After modifying, Balance of John is:", balance["John"])
#len() method
print("Number of customers in balance dictionary is:", len(balance))
#adding new key-value pair
balance["Alice"] = 3000.00  
print("New entry in balance: ",balance)
#built-in methods
print("Dictionary keys are:", balance.keys())
print("Dictionary values are:", balance.values())
print("Dictionary items are:", balance.items())

print("Is John present in balance dictionary?", "John" in balance)
#pop method
removed_balance = balance.pop("Raj")
print("Removed balance of Raj is:", removed_balance)
print("Balance dictionary after removing Raj:", balance)
print("Pop items",balance.popitem())
del balance["Liam"]
print("Balance dictionary after deleting Alice:", balance)

contents = {"name": "David", "age": 30, "city": "New York"}
print(contents.clear())

new_balance = balance.copy()
print("Copied balance dictionary:", new_balance)
balance.update({"Emma": 3000.00, "Olivia": 3500.50})
print("Balance dictionary after update:", balance)