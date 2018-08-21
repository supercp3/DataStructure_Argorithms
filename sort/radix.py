'''
基数排序
'''
import math

def radix_sort(nums,radix=10):
	#计算最大的整数有几位
	k=math.ceil(math.log(max(nums),radix))
	if max(nums)%10==0:
		k=k+1
	bucket=[[] for i in range(radix)]
	for i in range(1,k+1):
		for val in nums:
			bucket[int(val%(radix**i)/(radix**(i-1)))].append(val)
		del nums[:]
		for z in bucket:
			nums+=z
			del z[:]
	return nums
