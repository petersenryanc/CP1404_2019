"""
CP1404 Practical 5 - Hex Colours
"""

HEX_COLOURS = {"AliceBlue": "f0f8ff", "AntiqueWhite": "faebd7", "aquamarine1": "7fffd4",
               "azure1": "f0ffff", "beige": "f5f5dc", "black": "000000", "blue1": "0000ff",
               "brown": "a52a2a", "CadetBlue": "5f9ea0", "chocolate": "d2691e"}

for i, j in HEX_COLOURS.items():
    print("{} is {}".format(i, j))

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
