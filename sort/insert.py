'''
插入排序
'''
def insert_sort(nums):
	length=len(nums)
	for i in range(1,length):
		flag=nums[i]
		for j in range(i-1,-1,-1):
			if nums[j]>flag:
				nums[j+1]=nums[j]
				nums[j]=flag
	return nums





