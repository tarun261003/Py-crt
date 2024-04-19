from collections import Counter
def return_ans(d):
    d=list(d.keys())
    return d[-1]
def return_substring(sen):
    return sorted([sen[i:j] for i in range(len(sen)+1) for j in range(i+1,len(sen)+1)],key=len)
sen=input('Enter the string:')
d=Counter(return_substring(sen))
d1={}
for i in d:
    if d[i]>=2:
        d1[i]=d[i]
print(f'The longest repeating substring is :{return_ans(d1)}')