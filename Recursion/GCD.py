# This method uses Euclildean Algorithm to find gcd of two numbers.
# In this algorithm we first divide a from b, from next step we divide
# b from reminder of and a and b until the reminder becomes 0.
# the last reminder before 0 will be gcd.

def gcd(a, b):
    assert int(a) ==a and int(b) == b, 'The numbers must be integer only!'
    if a<0:abs(a)
    if b<0:abs(b)
    if a%b==0: return b
    return gcd(b,a%b)

if __name__ == "__main__":
    print(gcd(48,18))