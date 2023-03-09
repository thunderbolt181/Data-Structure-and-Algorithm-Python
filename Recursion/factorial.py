def factorial(n: int):
    assert int(n)==n and n>=0, "Number must be an +ve integer only!"
    if n >= 1: return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(int(input("Enter the number: "))))