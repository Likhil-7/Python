def emoji_converter(message):
    words = message.split(" ")
    emoji ={
        ":)":"😁",
        ":(":"😒"
    }
    output =""

    for i in words:
        output+=emoji.get(i,i) + " " #1st i is for emoji and 2nd i is for return value if emoji isn't given
    return output


message =input(">")
print(emoji_converter(message))