'''
选择排序
'''
def select_sort(nums):
	length=len(nums)
	for i in range(0,length-1):
		min=i
		for j in range(i+1,length):
			if nums[j]<nums[min]:
				min=j
		nums[i],nums[min]=nums[min],nums[i]
	return nums

