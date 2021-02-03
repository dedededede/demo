# -*- encoding: utf-8 -*-


def conflict(pos, state):
	# 行互相减 == 列互相减 ，判断对角线
	# 列互相减 == 0
	# 行互相减 i - length
	# 列互相减 state[i] - pos
	length = len(state)
	for i in range(length):
		if abs(i-length) == abs(state[i] - pos) or abs(state[i] - pos) == 0:
			return True
	return False

def conflict(state, col):
	row = len(state)
	for line in range(row):  # 遍历每一行，判断是否和要插入的row + 1 冲突
		if abs(state[line] - col) in (0, row - line):  # 判断是否处于同一列或者处于对角线位置
			return True
	return False


def queens(num, state=()):
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num - 1:  # 说明已经到倒数第二行了
				yield (pos, )
			else:
				for result in queens(num, state + (pos,)):
					yield (pos,) + result


for solution in list(queens(4)):
	print solution
