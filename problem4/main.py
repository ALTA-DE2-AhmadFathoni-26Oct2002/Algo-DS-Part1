def is_prime (number):
    if number < 1:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    inc = start + 1
    result = ""
    for x in range (height):
        for y in range (width):
            while not is_prime(inc):
                inc += 1
            result += str(inc) + " "
            inc += 1   
        result = result.rstrip() + "\n"     
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """