# Conversion of integer decimal numbers to binary numbers 

def dec_to_bin(n):
    assert int(n) ==n , "The parameter must be an integer only!"
    if n//2==0:return n%2
    return dec_to_bin(int(n/2))*10+n%2

if __name__ == "__main__":
    print(dec_to_bin(-5))