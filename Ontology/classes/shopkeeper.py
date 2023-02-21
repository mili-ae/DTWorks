from .hr import HR
from .shop_foreman import ShopForeman

class Shopkeeper(ShopForeman, HR):
    def __init__(self, name, salary, boss) -> None:
        super().__init__(name, salary, boss)
        
        
    def __str__(self) -> str:
        return super().__str__()