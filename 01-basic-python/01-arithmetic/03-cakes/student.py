# Write your code here

def cakes(eggs, butter, flour):
    egg_cakes = eggs // 5
    butter_cakes = butter // 250
    flour_cakes = flour // 250
    return min(egg_cakes, butter_cakes, flour_cakes)