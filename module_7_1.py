class Product():
    def __init(self,name,weight,category):
        self.name=name
        self.weight=weight
        self.category=category

    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'


class Shop():
