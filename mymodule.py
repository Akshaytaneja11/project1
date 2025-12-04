def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add(a, b):
    return a + b

class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        return f"Student name: {self.name}"
    
if __name__ == "__main__":
    # This part runs only if mymodule.py is executed directly
    print("Running mymodule.py directly!")
    print(greet("Direct Run"))
    print("Sum:", add(3, 4))
    s = Student("Test Student")
    print(s.show())
