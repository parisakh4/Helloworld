numbers = {
    "1":"one",
    "2":"two",
    "3":"three",
    }
phone = input("phone: ")
output = ""

for i in phone:
    output += numbers.get(i, "!")
print(output)
