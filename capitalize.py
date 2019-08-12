def solve(s):
    full_name = s.split(' ')
    return ' '.join((word.capitalize() for word in full_name))

str = input("Enter your string: ")
p= solve(str)
print(p)