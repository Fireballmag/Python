class MathProblemTraine:
    def __init__(self, task, answer, complete) -> None:
        self.task = task
        self.answer = answer
        self.complete = complete
    
    def check(self, answer):
        if(self.answer == answer):
            self.complete = True
        else:
            self.complete = False
        return self.complete
    

obj1 = MathProblemTraine(5*7, 5*7, True)
obj2 = MathProblemTraine(12+8, 12+8, True)

print(obj1.check(7), obj1.check(35), obj2.check(5), obj2.check(20))
