class Power:
    def pow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result

p = Power()
print(f"Output: {p.pow(2, 3)}")  # Output: 8.0
print(f"Output: {p.pow(2, -3)}")  # Output: 0.125
print(f"Output: {p.pow(3, 4)}")  # Output: 81.0

 