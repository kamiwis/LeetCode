class Solution:
    def numberOfSteps(self, num: int) -> int:
        number = num
        count = 0
        while number > 0:
            if number % 2 == 0:
                number /= 2
                count += 1
            else:
                number -= 1
                count += 1
        return count
        