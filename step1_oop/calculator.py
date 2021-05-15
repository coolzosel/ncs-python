class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    def mod(self):
        return self.first % self.second

    @staticmethod
    def execute():
        calculator = Calculator(int(input("첫번째수-> ")), int(input("두번째수-> ")))
        # int(input("뜨는 메세지")) -> int로만 input을 받겠다!
        print(f'첫번째수: {calculator.first}')
        print(f'두번째수: {calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'{calculator.first} - {calculator.second} = {calculator.sub()}')
        print(f'{calculator.first} * {calculator.second} = {calculator.mul()}')
        print(f'{calculator.first} / {calculator.second} = {calculator.div()}')
        print(f'{calculator.first} % {calculator.second} = {calculator.mod()}')

# 아래는 모듈의 시작점!
if __name__ == '__main__':
    Calculator.execute()