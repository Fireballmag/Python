class MathProblemTraine:
    def __init__(self, task) -> None:
        self.task = task
        self._answer = task
        self.complete = True
    
    def check(self, _answer):
        if(self._answer == _answer):
            self._complete = True
        else:
            self._complete = False
        return self._complete
    
    def task_return(self): #используется в обоих дочерних классах
        return self.task
    
class AdditionTrainer(MathProblemTraine):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1 + number2)
        self.task = str(number1) + "+" + str(number2)
    
class Trainer_multiplication(MathProblemTraine):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1 * number2)
        self.task = str(number1) + "*" + str(number2)


obj1 = MathProblemTraine(5*7)
obj2 = MathProblemTraine(12+8)

print(obj1.check(7), obj1.check(35), obj2.check(5), obj2.check(20))

obj3 = AdditionTrainer(5, 7)
obj4 = Trainer_multiplication(2, 5)

print(obj3.check(12), obj3.check(4), obj4.check(10), obj4.check(20))

print(obj1.task_return())
