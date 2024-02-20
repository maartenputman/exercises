# Write your code here

def target_sum(ns, target):
    for i in range(0, len(ns)):
        for j in range(i, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False