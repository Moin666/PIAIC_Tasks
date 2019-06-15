phone = input("enter a phone")
dic = {
    "1" : "ONE",
    "2" : "Two",
    "3" : "Three"
}
output =""
for x in phone:
    output +=dic.get(x) + "  "
print(output)

