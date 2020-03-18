
f = open("input.txt", "r")
for x in f:
    a_string = x;

    alphanumeric = " "

    for character in a_string:
        if character.isalnum():
            alphanumeric += character
    print(alphanumeric)
