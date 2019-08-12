def merge_the_tools(s, k):
    # your code goes here
    m= list(map(''.join, zip(*[iter(s)]*k)))
    for i in m:
        z= ''.join(sorted(set(i), key=i.index))
        print(z)

if __name__ == '__main__':
    string, k = input("Enter String: "), int(input("Enter Number: "))
    merge_the_tools(string, k)