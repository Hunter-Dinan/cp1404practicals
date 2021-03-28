"""Look up hexadecimal colour codes."""

COLOURS = {"aliceblue": "#f0f8ff", "azure1": "#f0ffff", "beige": "#f5f5dc",
           "blue1": "#0000ff", "blueviolet": "#8a2be2", "cadetblue": "#5f9ea0",
           "aquamarine1": "#7fffd4", "chartreuse1": "#7fff00",
           "chocolate": "#d2691e", "cornflowerblue": "#6495ed"}

input_colour = input("Colour: ")

while input_colour != "":
    if input_colour.lower() in COLOURS:
        print("{} hex code is {}".format(input_colour,
                                         COLOURS[input_colour.lower()]))
    else:
        print("Invalid colour option. Try again")
    input_colour = input("Colour: ")
