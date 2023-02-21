from .hr import HR
from .buyer_foreman import BuyerForeman

class Buyer(BuyerForeman, HR):
    def __init__(self, name, salary, boss) -> None:
        super().__init__(name, salary, boss)
        
        
    def __str__(self) -> str:
        return super().__str__()