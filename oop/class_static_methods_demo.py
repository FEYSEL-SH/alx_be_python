class Calculator:
    calculation_type = "Arithmetic Operations"
    def __init__(self):
        pass

    @classmethod
    def  multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    @staticmethod
    def add( self, a, b):
        self.a = a
        self.b = b

        return a * b

