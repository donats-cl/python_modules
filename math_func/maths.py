import math


class Sqrt:
    def __init__(self, real, sqrt):
        self.real = real
        self.sqrt = sqrt

    def __str__(self):
        return f"{self.real}*sqrt({self.sqrt})"


def show_sqrt(x):

    num = int(x**2)
    intg = 1
    sqrt_n = 1
    is_found = False

    if x > 1:
        for i in range(num, 1, -1):
            if num % i**2 == 0:
                intg = i
                sqrt_n = (x/i)**2
                is_found = True
                break

        if not is_found:
            for i in range(num, 1, -1):
                if num == i:
                    intg = 1
                    sqrt_n = i
                    break
    else:
        for i in range(1, 100):
            for j in range(1, 100):
                if abs(abs(math.sqrt(i)/j)-abs(x)) < 0.0001:
                    intg = 1/j
                    sqrt_n = i
                    is_found = True
                    break
            if is_found: break

    return Sqrt(intg, sqrt_n)


if __name__ == "__main__":
    print(show_sqrt(math.sqrt(2)/2))
    print(show_sqrt(3*math.sqrt(2)))
