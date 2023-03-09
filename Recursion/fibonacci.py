def fibonacci(n):
    assert int(n)==n and n>0,"The number should be an +ve integer only!"
    if n in [0,1]:return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print(fibonacci(int(input("Enter a number: "))))