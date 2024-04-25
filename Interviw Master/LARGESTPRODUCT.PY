def returnMaxProduct(nums):
    max_prod,min_prod,result=nums[0],nums[0],nums[0]
    for i in range(1,len(nums)):
        temp_max=max(nums[i],max_prod*nums[i],min_prod*nums[i])
        temp_min=min(nums[i],max_prod*nums[i],min_prod*nums[i])
        max_prod,min_prod=temp_max,temp_min
        result=max(result,max_prod)
    return result
nums=eval(input())
print(returnMaxProduct(nums))