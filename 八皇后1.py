# -*- encoding: utf-8 -*-

res = [None] * 8


# 行互相减 == 列互相减 ，判断对角线
# 列互相减 == 0


def is_ok(row, column):  # 判断row行column是否合适
	left_up = column - 1
	right_up = column + 1
	for i in range(row -1, -1, -1):

		if res[i] == column:  # 第i行的column列有棋子吗？
			return False
		if left_up >=0 and res[i] == left_up:  # 考察左上对角线：第i行leftup列有棋子吗？
			return False
		if right_up < 8 and res[i] == right_up:  #  考察右上对角线：第i行rightup列有棋子吗？
			return False

		left_up -= 1
		right_up += 1

	return True


def queens(row):

	if row == 8:
		print "res:", res
		return

	for column in range(8):

		if is_ok(row, column):  # 第row行的棋子放到了column列
			res[row]= column
			queens(row + 1)

queens(0)
