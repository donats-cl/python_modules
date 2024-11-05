import math


class Sqrt:
    def __init__(self, real, sqrt):
        self.real = real
        self.sqrt = sqrt

        self.have_real = False
        self.have_sqrt = False

        if real is not None and sqrt is not None:
            self.value = real * math.sqrt(self.sqrt)
            self.have_real = True
            self.have_sqrt = True
        elif sqrt is not None:
            self.value = math.sqrt(self.sqrt)
            self.have_sqrt = True
        elif real is not None:
            self.value = self.real
            self.have_real = True

    def __str__(self):
        res = f"{self.real}*sqrt({self.sqrt})" if self.have_sqrt and self.have_real else f"sqrt({self.sqrt})" if self.have_sqrt and not self.have_real else f"{self.real}" if self.have_real and not self.have_sqrt else "NOTHING"
        return res
    
def arn(x):
    return int(x) if x % 1 < 0.5 else int(x)+1
    
def show_sqrt(x):

    num = arn(x**2)
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

    if intg == 1 and not sqrt_n == 1:
        return Sqrt(None, arn(sqrt_n))
    elif sqrt_n == 1:
        return Sqrt(intg, None)
    else:
        return Sqrt(intg, arn(sqrt_n))


if __name__ == "__main__":
    print(show_sqrt(math.sqrt(2)/2))
    print(show_sqrt(3*math.sqrt(2)))
