def reverse_string(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Read input from the user
input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))
