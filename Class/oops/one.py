class Car:
    def __init__(self,name,color,car_no) -> None:
        self.name=name
        self.color=color
        self.car_no=car_no
car=Car('Wagnor',"Red","AP-16-EC-1704")
print(car.color,car.name,car.car_no)   