class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(n):
            t = i + 1
            if t % 15 == 0:
                a.append("FizzBuzz")
            elif t % 3 == 0:
                a.append("Fizz")
            elif t % 5 == 0:
                a.append("Buzz")
            else:
                a.append(f"{t}")
        return a