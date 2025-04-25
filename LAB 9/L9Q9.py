print("Name:Shubh Raval")
print("Roll No.:24BEE154")
def countAlphaDigit(string):
    count = {'Alpha': 0, 'Digit': 0}
    for char in string:
        if char.isalpha():
            count['Alpha'] += 1
        elif char.isdigit():
            count['Digit'] += 1
    return count
string = input("Enter a string: ")
print(countAlphaDigit(string))
