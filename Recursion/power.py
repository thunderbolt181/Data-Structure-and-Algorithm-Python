def power(base, expo):
    assert int(expo) == expo, "The exponent numst be integer number only"
    if expo == 1: return base
    return base * power(base, expo-1)

if __name__ == "__main__":
    print(power(14,214))