numbers = {
    "1":"one",
    "2":"two",
    "3":"three",
    }
phone = input("phone: ")
message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😂",
    ":(":"😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)