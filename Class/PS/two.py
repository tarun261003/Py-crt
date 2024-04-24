def check_vehicle(Num):
    if any(i in list('AEIOUY') for i in Num):
        return False
    for i in range(len(Num)):
        try:
            j=i+1
            if  Num[i].isalpha() or Num[j].isalpha() or Num[i]=='-' or Num[j]=='-':
                continue
            if (int(Num[i])+int(Num[j]))%2!=0:
                return False
        except Exception as e:
            pass
        return True
vehicle_number=input('Enter the vehicle number:')
result="Valid" if check_vehicle(vehicle_number) else "Invalid"
print(result)          