def percent(att, tot):
    return (att / tot) * 100

def num_class(att, tot):
    if att / tot < 0.75:
        d = att
        while True:
            att += 1
            tot += 1
            if att / tot >= 0.75:
                num = att - d
                return "For safe attendance, you need to attend the next " + str(num) + " days"
    else:
        d = tot
        while True:
            tot += 1
            if att / tot < 0.75:
                num = tot - d
                return "For safe attendance, you can take leave up to " + str(num - 1) + " days"
