from .hr import HR
from .company import Company

class CEO(HR, Company):
    def __init__(self, name, salary, boss) -> None:
        super().__init__(name, salary)
        self.boss = boss
        
        
    def get_boss(self):
        return self.boss
    
    
    def __str__(self) -> str:
        return super().__str__() + f" - {self.boss}"