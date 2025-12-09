balance = {"Jaimie": 25000,
           "Cassie": 12000,
           "Megan": 25700}
print(balance)
print(balance["Cassie"])
print(balance.get("Megan"))
balance["Cassie"] = 26900
print(balance)
print(len(balance))
balance['Doroti'] = 25000
print(balance)
print("key value of dictionary", balance.keys())
print("Jaimie" in balance)
print("Eren" in balance)
print("Values in dictionary", balance.values())
print("items methods", balance.items())
print(balance.pop("Megan"))
print(balance)
print(balance.popitem())
print(balance)
del balance['Jaimie']
print(balance)
balance.clear()
print(balance)
balance1 = {"Jaimie": 25000,
            "Cassie": 12000,
            "Megan": 25700,
            "Stuart": 23551,
            "King": 34900}
balance2 = balance1.copy()
print(balance2)
balance2.update({'samuel': 50000})
print(balance2, balance1)
