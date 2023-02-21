from .hr import HR
from .ceo import CEO

class ShopForeman(CEO, HR):
    def __init__(self, name, salary, boss) -> None:
        super().__init__(name, salary, boss)
        
        
        
    def __str__(self) -> str:
        return super().__str__()