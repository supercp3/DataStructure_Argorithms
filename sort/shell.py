'''
希尔排序
'''
#思想为直接插入排序的改变
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    #计算每次的增量
    group = int(count / step)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group =int(group/ step)
    return lists
