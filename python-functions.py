def max_num(x,y,z):
    return max([x,y,z])
print(max_num(20,30,40))

def mult_list(list):
    total = 1
    for i in list:
        total *= i
    return total
print(mult_list((1,2,3,4,5)))

def rev_string(string):
    return string[::-1]
print(rev_string("God is Good"))

def num_within(a,b,c):
    return a in range(a,b,c)
print(num_within(5,2,3))


