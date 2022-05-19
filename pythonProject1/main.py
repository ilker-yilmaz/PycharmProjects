#counts lowercase and uppercase letters in a string
def counts(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return lower, upper