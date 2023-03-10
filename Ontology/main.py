from classes import (ceo as CEO,
                     hr as HR,
                     shop_foreman as SF,
                     shopkeeper as SK,
                     buyer_foreman as BF,
                     buyer as B)


def main():
    # Look at me making the worst naming possible :DD
    hr = HR.HR("Jane Doe", 1000)
    ceo = CEO.CEO("John Doe", 2000, None)
    shop_fm = SF.ShopForeman("Richard Doe", 1500, ceo)
    buyer_fm = BF.BuyerForeman("Rick Doe", 1500, ceo)
    shopkeep = SK.Shopkeeper("Marie Doe", 500, shop_fm)
    buyer = B.Buyer("Ann Doe", 500, buyer_fm)
    
    cls_list = [hr, ceo, shop_fm, buyer_fm, shopkeep, buyer]
    cls_map = {
        "hr"            :   hr,
        "ceo"           :   ceo,
        "shopforeman"   :   shop_fm,
        "buyerforeman"  :   buyer_fm,
        "shopkeeper"    :   shopkeep,
        "buyer"         :   buyer
    }
    print("Done creating objects\nClasses used: HR, CEO, ShopForeman, BuyerForeman, Shopkeeper, Buyer\n\n")
    
    print("Choose action:")
    print("0. Display parent(s) of class")
    print("1. Display children of class")
    print("2. Display children of class that have input text in their 'name' field")
    print("3. Display children of class that have salary higher than input")
    print("4. Display children of class that are controlled by this class")
    
    def get_class(cls: str):
        return cls_map[cls.lower()]
    
    match int(input()):
        case 0:
            cls = get_class(str(input())).__class__
            print([c.__name__ for c in cls.__mro__][1:-1])   
        case 1:
            cls = get_class(str(input())).__class__
            print([c.__name__ for c in cls.__subclasses__()])
        # fuck it, im going ham  
        case 2:
            cls = get_class(str(input())).__class__
            text = str(input())
        
            for obj in cls_list:
                if cls in obj.__class__.__bases__:
                    if text in obj.get_name():
                        print(obj.get_name(), " | ", obj.__class__.__name__)  
        case 3:
            cls = get_class(str(input())).__class__
            text = int(input())
        
            for obj in cls_list:
                if cls in obj.__class__.__bases__:
                    if text < obj.get_salary():
                        print(obj.get_salary(), " | ", obj.__class__.__name__) 
        case 4:
            cls = get_class(str(input()))
        
            for obj in cls_list:
                if obj == cls:
                    continue
                elif obj.get_boss() != None and type(obj.get_boss()) == type(cls):
                    print(obj.__class__.__name__)
    
    
if __name__ == "__main__":
    main()