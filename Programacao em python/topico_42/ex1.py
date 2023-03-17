class Student:
    def __init__(self, name, note1, note2):
        self.name = name
        self. note1 = note1
        self. note2 = note2
    
    def mean(self):
        return (self.note1+self.note2)/2
    
    def show_info(self):
        print(f'Student name: {self.name}')
        print(f"Student's 1° note: {self.note1}")
        print(f"Student's 2° note: {self.note2}")
    
    def result(self):
        mean = self.mean()
        return mean >= 6
    


aluno1 = Student('Thiago', 5.0, 6)
print(f'média{aluno1.mean()}')
aluno1.show_info()

print(aluno1.result())
        
