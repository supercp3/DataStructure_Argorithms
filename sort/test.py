import time
import bubble
import select
import insert
import quick
import merge
'''
n=1:冒泡排序
n=2:选择排序
n=3:插入排序
n=4:快速排序
n=5:归并排序
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

if __name__=="__main__":
	testlist=[7,2,3,8,10,9,2]
	run(1,testlist)
	run(2,testlist)
	run(3,testlist)
	run(4,testlist)
	run(5,testlist)