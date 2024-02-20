# Write your code here

def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 1:
        # uneven
        return ns[int(len(ns)/2)]
    else:
        return (ns[int(len(ns)/2)] + ns[int(len(ns)/2) - 1])/2