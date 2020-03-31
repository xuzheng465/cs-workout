


def sortArray(nums):
        if len(nums)==0:
            return []
        else:
            x = nums.pop()
            return sortArray([a for a in nums if a<=x])+[x]+ sortArray([a for a in nums if a > x])


print(sortArray([5,2,3,1]))