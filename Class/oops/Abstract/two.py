from abc import ABC,abstractmethod
import csv
class DataProcessor(ABC):
    @abstractmethod
    def read_data(self):
        pass
    @abstractmethod
    def write_data(self):
        pass
class CSVProcessor(DataProcessor):
    def __init__(self,file_path):
        d=[]
        with open(file_path,'r') as file:
            data=csv.reader(file,delimiter=' ')
            d.append(list(data))
        self.data=d    
    def read_data(self):
        for i in self.data[0]:
            print(i)
    def write_data(self):
        print('write')
csv=CSVProcessor(r'C:\Users\tarun\Downloads\industry.csv')
csv.read_data()
csv.write_data()