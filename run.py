mylist = [["Apple","Banana",["Jack","Rose"],"Love"],["Apple","Orange",["Rose"]]]

x = "Rose"

for i in mylist:
    if x in i:
        print(x)
    elif x in i[2]:
        print(x)
