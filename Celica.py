class Car:
    '''Вывод информации о машине на консоль'''

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f'Car brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}')

my_car = Car('Toyota', 'Celica', '2002', 'red')
my_car.display_info()