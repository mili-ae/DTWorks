from abc import ABC, abstractmethod

class Company():

    def get_name(self) -> str:
        raise NotImplementedError("Must override this method")