class Company():

    def get_name(self) -> str:
        raise NotImplementedError("Must override this method")
    
    def get_salary(self) -> int:
        raise NotImplementedError("Must override this method")
    
    def get_boss(self):
        raise NotImplementedError("Must override this method")
    