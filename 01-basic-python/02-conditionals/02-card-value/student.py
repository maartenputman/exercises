# Write your code here

def card_value(string):
    faces = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 1}
    return faces.get(str(string), string)