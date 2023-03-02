from array import array

scores = array('d')
scores.append(10)
scores.append(12)
# scores.append('a') error

print(scores)

arr1 = ['a', 'b']

# arr1.append('a')
# arr1.append('b')
arr1.append('c')
print(arr1)
"""
	arrays  Python包含以下方法:
    1	list.append(obj)
			在列表末尾添加新的对象
		2	list.count(obj)
			统计某个元素在列表中出现的次数
		3	list.extend(seq)
			在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
		4	list.index(obj)
			从列表中找出某个值第一个匹配项的索引位置
		5	list.insert(index, obj)
			将对象插入列表
		6	list.pop([index=-1])
			移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
		7	list.remove(obj)
			移除列表中某个值的第一个匹配项
		8	list.reverse()
			反向列表中元素
		9	list.sort( key=None, reverse=False)
			对原列表进行排序
		10	list.clear()
			清空列表
		11	list.copy()
			复制列表
"""