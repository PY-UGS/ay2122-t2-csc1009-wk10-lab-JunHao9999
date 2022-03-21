#question1
print("Hello Glasgow!")

#question2
x=float(input("input x"))
y=float(input("input y"))
print("Avg: ",(x+y)/2)

# 3 (wk01 2b)
def switch(mod):
    match mod:
        case "CSC1006":
            return "Mathematics 2"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return "Data Structures and algorithms"
        case "CSC1009":
            return "Objected Oriented Programming"
        case "CSC1010":
            return "Computer Networks"

mods=input("Enter module code: ")
print(switch(mods))

# 3 (wk01 2c)
for i in range(102,66,-1):
    if i%2!=0:
        print(i)

