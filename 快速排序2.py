# -*- encoding: utf8 -*-
def quick_sort(b):
    """快速排序"""
    if len(b) < 2:
        return b
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = b[len(b) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    b.remove(mid)
    for item in b:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)

a = [2,4,7,5,6,1,1]
print quick_sort(a)