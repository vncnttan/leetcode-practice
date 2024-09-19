class Solution:
    def compute(self, a: int, b: int, expression: str):
        if expression == "+":
            return a + b
        if expression == "-":
            return a - b
        if expression == "*":
            return a * b
        
    def searchNext(self, current_numbers, current_operators, position, ):
        leftNum = current_numbers[position][1]
        rightNum = current_numbers[position+1][1]
        current_numbers[position] = (
            (current_numbers[position][0], current_numbers[position+1][0]),
            self.compute(leftNum, rightNum, current_operators[position])
        )

        current_numbers.pop(position + 1)
        current_operators.pop(position)

        if current_operators == []:
            print(current_numbers)
            if not current_numbers[0][0] in self.memo:
                self.answers.append(current_numbers[0][1])
                self.memo.append(current_numbers[0][0])

            return

        for i in range(len(current_operators)):
            self.searchNext(current_numbers.copy(), current_operators.copy(), i)

    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.expression = expression

        extracted_numbers = expression.replace('+', ',').replace('-', ',').replace('*', ',').split(",")
        extracted_numbers = [int(n) for n in extracted_numbers]
        operators = []
        
        self.memo = []

        for idx, n in enumerate(extracted_numbers):
            extracted_numbers[idx] = (idx, n)

        for sym in expression:
            if sym == "+" or sym == "-" or sym == "*":
                operators.append(sym)
        
        if len(operators) == 0:
            return [int(expression)]

        self.answers = []
        for idx, o in enumerate(operators):
            current_num = extracted_numbers
            self.searchNext(extracted_numbers.copy(), operators.copy(), idx)
            
        return self.answers