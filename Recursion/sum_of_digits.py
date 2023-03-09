def sumofDigits(n):
    assert int(n)==n and n>0, "Then number should be +ve integer number only!"
    if n==0: return 0
    return int(n%10) + sumofDigits(int(n//10))

if __name__ == "__main__":
    print(sumofDigits(12432233))