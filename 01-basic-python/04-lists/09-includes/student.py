# Write your code here

def includes(xs, ys):
    for ele_y in ys:
        match = False
        for ele_x in xs:
            if ele_x == ele_y:
                match = True
        if match == False:
            return False
    return True