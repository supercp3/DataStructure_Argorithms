# DataStructure_Argorithms
第一章节：排序<br>
===
一冒泡排序<br>
---
冒泡排序算法的原理如下：
1、比较相邻的元素。如果第一个比第二个大，就交换他们两个;
2、对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数;
3、针对所有的元素重复以上的步骤，除了最后一个;
4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较;
冒泡排序总的平均时间复杂度为O(n^2),是一种稳定的排序算法
优化：
针对问题：
	数据的顺序排好之后，冒泡算法仍然会继续进行下一轮的比较，直到arr.length-1次，后面的比较没有意义的。
方案：
	设置标志位flag，如果发生了交换flag设置为true；如果没有交换就设置为false。
	这样当一轮比较结束后如果flag仍为false，即：这一轮没有发生交换，说明数据的顺序已经排好，没有必要继续进行下去

二、选择排序<br>
---
选择排序（Selection sort）是一种简单直观的排序算法;
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置,
直到全部待排序的数据元素排完。 选择排序是不稳定的排序方法。
平均时间复杂度 O(n^2)

三、插入排序<br>
---
算法描述：
⒈ 从第一个元素开始，该元素可以认为已经被排序;
⒉ 取出下一个元素，在已经排序的元素序列中从后向前扫描;
⒊ 如果该元素（已排序）大于新元素，将该元素移到下一位置;
⒋ 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置;
⒌ 将新元素插入到下一位置中;
⒍ 重复步骤2~5
优化：
如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。该算法可以认为是插入排序的一个变种，称为二分查找排序。
算法适用于少量数据的排序，时间复杂度为O(n^2)，是稳定的排序方法

四、快速排序<br>
---
基本思想：（分治）
1、先从数列中取出一个数作为key值；
2、将比这个数小的数全部放在它的左边，大于或等于它的数全部放在它的右边；
3、对左右两个小数列重复第二步，直至各区间只有1个数。
算法平均时间复杂度为O(nlogn),不稳定的排序算法

五、归并排序<br>
---
归并操作的工作原理如下：
第一步：申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
第二步：设定两个指针，最初位置分别为两个已经排序序列的起始位置
第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
重复步骤3直到某一指针超出序列尾
将另一序列剩下的所有元素直接复制到合并序列尾
归并排序的比较次数小于快速排序的比较次数，移动次数一般多于快速排序的移动次数
速度仅次于快速排序，为稳定排序算法
时间复杂度 O(nlogn),空间复杂度O(n),稳定的排序算法

六、希尔排序<br>
---
希尔排序也是一种插入排序，它是简单插入排序的一个高级版本，也称为缩小增量排序
基本思想：
希尔排序是按下标的一定增量进行分组，对每组使用直接插入排序，随着增量的减小，
每组包含的关键词越来越多，当增量减小到1时，整个序列被分为一组，算法停止。
时间复杂度为
希尔增量时间复杂度为O(n²)，而Hibbard增量的希尔排序的时间复杂度为O(n^3/2)
不稳定的排序算法

七、堆排序<br>
---
堆排序是利用堆这种数据结构而设计的一种排序算法，堆排序是一种选择排序，它的最坏，最好，平均时间复杂度均为O(nlogn)，它也是不稳定排序。
堆结构：
堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  
小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
简单总结下堆排序的基本思路：
a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
时间复杂度为O(nlogn),不稳定排序算法

八、基数排序<br>
---
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
基数排序法是属于稳定性的排序，其时间复杂度为O(nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。
***********
值得参考的网上资源：https://www.cnblogs.com/hokky/p/8529042.html

