def isHappy(n):
    output = False

    sum = n
    already_used = []

    i = 0

    while sum != 1:
        i += 1
        print(f"\nLoop #{i}")
        print(f"sum = {sum}")

        number_arr = []

        for digit in str(sum):
            number_arr.append(int(digit))

        print(f"converted into an array: {number_arr}")

        sum = 0
        for digit in number_arr:
            sum += digit**2
            print(f"{digit}^2 = {(digit**2)}")

        print(f"current sum = {sum}")

        print(f"Sums seen so far: {already_used}")

        if sum in already_used:
            print(f"already saw this sum")
            break
        else:
            already_used.append(sum)
            print("adding sum to list")

    print(f"out of the loop somehow, sum={sum}")
    if sum == 1:
        output = True

    return output


n = 2
if isHappy(n):
    print("HAPPY")
else:
    print("NAH")

# code working
# passed all test cases
