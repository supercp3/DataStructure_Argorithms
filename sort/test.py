import time
import bubble
import select
import insert
import quick
import merge
import shell
import heap
import radix
'''
n=1:冒泡排序 稳定   O(n^2)
n=2:选择排序 不稳定 O(n^2)
n=3:插入排序 稳定   O(n^2)
n=4:快速排序 不稳定 O(nlogn)
n=5:归并排序 稳定   时间复杂度 O(nlogn),空间复杂度O(n)
n=6:希尔排序 不稳定 O(n^3/2)-O(n^2)
n=7:堆排序   不稳定 O(nlogn)
n=8:基数排序 稳定   O(nlog(r)m)
'''
def run(n,testlist):
	if n==1:
		start=time.clock()
		res_bubble=bubble.bubble_sort(testlist)
		end=time.clock()
		print("result:",res_bubble)
		print("bubble_runtime:",end-start)
	if n==2:
		start=time.clock()
		res_select=select.select_sort(testlist)
		end=time.clock()
		print("result:",res_select)
		print("select_runtime:",end-start)
	if n==3:
		start=time.clock()
		res_insert=insert.insert_sort(testlist)
		end=time.clock()
		print("result:",res_insert)
		print("insert_runtime:",end-start)
	if n==4:
		start=time.clock()
		res_quick=quick.quick_sort(testlist,0,len(testlist)-1)
		end=time.clock()
		print("result:",res_quick)
		print("quick_runtime:",end-start)
	if n==5:
		start=time.clock()
		res_merge=merge.merge_sort(testlist,0,len(testlist)-1)
		end=time.clock()
		print("result:",res_merge)
		print("merge_runtime:",end-start)
	if n==6:
		start=time.clock()
		res_shell=shell.shell_sort(testlist)
		end=time.clock()
		print("result:",res_shell)
		print("shell_runtime:",end-start)
	if n==7:
		start=time.clock()
		res_heap=heap.heap_sort(testlist)
		end=time.clock()
		print("result:",res_heap)
		print("heap_runtime:",end-start)
	if n==8:
		start=time.clock()
		res_radix=radix.radix_sort(testlist)
		end=time.clock()
		print("result:",res_radix)
		print("radix_runtime:",end-start)
if __name__=="__main__":
	testlist=[7,2,3,8,10,9,2]
	run(1,testlist)
	run(2,testlist)
	run(3,testlist)
	run(4,testlist)
	run(5,testlist)
	run(6,testlist)
	run(7,testlist)
	run(8,testlist)