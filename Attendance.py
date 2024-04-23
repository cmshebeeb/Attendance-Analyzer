'''
    Counting the percentage of attendance and number of days for safe
'''
#define a function for calculating percentage
def percent(att,tot):
    percentage=(att/tot)*100
    return percentage


#define a function for calculating number of days for safe
def num_class(att, tot):
    if att / tot < 0.75:
        d=att
        while (True):
            att=att+1
            tot=tot+1
            if att / tot >= 0.75:
                num = att-d
                break
        print("For safe attendance, you need to attend the next " + str(num) + " days")
    else:
        d=tot
        while (True):
            tot=tot+1
            if att / tot < 0.75:
                num=tot-d
                break
        print("For safe attendance, you can take leave upto" + str(num-1) + " days")


total=int(input("Total number of class "))
attendance=int(input("Number of class attended "))
x=percent(attendance,total)
print(x)
num_class(attendance,total)   