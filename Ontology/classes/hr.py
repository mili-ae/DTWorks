from .company import Company

class HR(Company):
    def __init__(self, name, salary) -> None:
        super().__init__()
        self.name = name
        self.salary = salary
        
        
    def get_name(self) ->str:
        return self.name

    def get_salary(self) -> int:
        return self.salary
    
    def get_boss(self):
        return None
        
    def __str__(self) -> str:
        return f"{self.name} - {self.salary}"