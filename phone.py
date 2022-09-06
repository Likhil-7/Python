phone =input("phone:")

digits_map ={
    "1" :"one",
    "2" :"two",
    "3" :"three",
    "4" :"four"
}

output =""
for i in phone:
    output+=digits_map.get(i,"!") +" "

print(output)

