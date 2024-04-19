def count_occurences(lst,target):
    count=0
    for i in lst:
        if i==target:
            count+=1
    return count
if __name__=="__main__":
    lst=eval(input('Enter the list:'))
    target=int(input('Enter the target value:'))
    print(f'The count of {target} is {count_occurences(lst,target)}')