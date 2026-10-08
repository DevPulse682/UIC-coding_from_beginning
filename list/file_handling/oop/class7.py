'''
check if number is even make a static method that checks if a number is even
'''


class Number:
    @staticmethod
    def is_even(num):
        return num % 2 == 1


print(Number.is_even(3))