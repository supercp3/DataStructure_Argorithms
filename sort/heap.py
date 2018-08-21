'''
堆排序
'''
#调整位置
def adjust_heap(nums,i,size):
	lchild=2*i+1
	rchild=2*i+2
	max=i
	if i<size/2:
		if lchild<size and nums[lchild]>nums[max]:
			max=lchild
		if rchild<size and nums[rchild]>nums[max]:
			max=rchild
		if max!=i:
			nums[max],nums[i]=nums[i],nums[max]
			adjust_heap(nums,max,size)
#找出第一个非叶子节点，然后进行比较
def build_heap(nums,size):
	for i in range(0,int(size/2))[::-1]:
		adjust_heap(nums,i,size)

def heap_sort(nums):
	size=len(nums)
	build_heap(nums,size)
	for i in range(0,size)[::-1]:
		nums[0],nums[i]=nums[i],nums[0]
		adjust_heap(nums,0,i)
	return nums
		