def linear_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            global index
            index=i


            return True
    return False
# list which contains both string and numbers.
list = [1, 2, 'sachin', 4, 'ram', 6]


inp = input('enter a number or string:')

if inp.isnumeric():
    inp = int(inp)
    print('input is number')
else:
    print('input is string' )
if linear_search(list,inp):
    print("found at index %d"%index)
else:
    print("Not Found")


