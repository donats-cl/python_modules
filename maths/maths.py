import math

rtd = lambda x: x*180/math.pi
dtr = lambda x: x*math.pi/180

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

    # if x < 0: return Sqrt(float(str(x)[:10]), None)

    # num = arn(x**2)
    intg = 1
    sqrt_n = 1
    is_found = False

    for i in range(1, 100):
        for j in range(-100, 100):
            for k in range(-100, 100):
                if j == 0: continue
                if abs(k*math.sqrt(i)/j-x) < 0.0000001:
                    intg = k/j
                    sqrt_n = i
                    is_found = True
                    break
                else:
                    intg = 0
                    sqrt_n = 0
            if is_found: break
        if is_found: break

    if intg == 1 and not sqrt_n == 1:
        return Sqrt(None, arn(sqrt_n))
    elif sqrt_n == 1:
        return Sqrt(intg, None)
    else:
        if math.sqrt(sqrt_n) % 1 == 0:
            return Sqrt(intg*math.sqrt(sqrt_n), None)
        else:
            return Sqrt(intg, arn(sqrt_n))


if __name__ == "__main__":
    print(show_sqrt(math.sqrt(2)/2))
    print(show_sqrt(3*math.sqrt(2)))
