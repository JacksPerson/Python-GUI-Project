'''
length
contains string info
contains numeric value
Contains special characters

a 1 = int, 2 = float, 3 = string
b 1 = less than set length 2 = longer or equal to set length
'''
X = input("Please enter some information here. ")
Y = 15 ## max length + 1
def check_user_input(X,Y):
    a = 0
    b = 0
    if len(X) < Y:
        b = 1
    else:
        b = 2
    try:
        # Convert it into integer
        val = int(X)
        a = 1
    except ValueError:
        try:
            # Convert it into float
            val = float(X)
            a = 2
        except ValueError:
            # Check for String
            a = 3
    report = int(str(a) + str(b))
    return report
print(check_user_input(X,Y))
