message =input(">")
words = message.split(" ")
emoji ={
    ":)":"😁",
    ":(":"😒"
}
output =""

for i in words:
    output+=emoji.get(i,i) + " " #1st i is for emoji and 2nd i is for return value if emoji isn't given

print(output)