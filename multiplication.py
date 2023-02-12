'''
In this code the multiplication of two integer numbers is done by Karatsuba method.
this method is an example of divide and coquer algorithm.
'''
import math as m


def summation(a,b):
    if len(a) < len(b):
        a = '0'*(len(b)-len(a)) + a
    else: 
        b = '0'*(len(a)-len(b)) + b
    la = a[::-1]
    lb = b[::-1]
    sum_over = 0
    sum_total = []
    for i, j in zip(la, lb):
        sum_1 = int(i) + int(j) + sum_over
        sum_over = sum_1 // 10
        sum_total.insert(0,str(sum_1 % 10))
    if sum_over > 0:
      sum_total.insert(0,str(sum_over))  
    return ''.join(sum_total).lstrip('0')
    
    
def multiply(x, y):
    if len(x)==0 or len(y)==0:
        return '0'
    if len(x) + len(y) < 10:
        return str(int(x) * int(y))
    lx = len(x)
    ly = len(y)
    a = x[:lx//2]
    b = x[lx//2:]
    c = y[:ly//2]
    d = y[ly//2:]
    ac = multiply(a, c)
    ad = multiply(a, d)
    bc = multiply(b, c)
    bd = multiply(b, d)
    ac_10 = ac + '0'*m.ceil(lx/2) + '0'*m.ceil(ly/2)
    ad_10 = ad + '0'*m.ceil(lx/2)
    bc_10 = bc + '0'*m.ceil(ly/2)
    ad_bc_10 = summation(ad_10, bc_10)
    return summation(summation(ac_10, ad_bc_10), bd)


a = '3141592653589793238462643383279502884197169399375105820974944592'
b = '2718281828459045235360287471352662497757247093699959574966967627'
print(multiply(a,b))