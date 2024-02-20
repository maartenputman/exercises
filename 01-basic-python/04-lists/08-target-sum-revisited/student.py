# Write your code here

def target_sum(ns, target):
    for i in range(0, len(ns) - 1):
        for j in range(i + 1, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False