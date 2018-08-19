'''
归并排序
'''
def merge_sort(nums,low,high):
	if low<high:
		mid=int((low+high)/2)
		merge_sort(nums,low,mid)
		merge_sort(nums,mid+1,high)
		merge(nums,low,mid,high)
	return nums

def merge(nums,low,mid,high):
	i=low
	j=mid+1
	temp=[]
	while i<=mid and j<=high:
		if nums[i]<nums[j]:
			temp.append(nums[i])
			i+=1
		else:
			temp.append(nums[j])
			j+=1
	while i<=mid:
		temp.append(nums[i])
		i+=1
	while j<=high:
		temp.append(nums[j])
		j+=1
	nums[low:high+1]=temp

