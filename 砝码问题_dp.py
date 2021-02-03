def main():
    sum = 0
    ma = [1, 1, 1, 1, 1, 1]
    weigth = [1, 2, 3, 5, 10, 20]
    dp = [0 for i in range(1001)]
    for i in range(6):
        sum += ma[i] * weigth[i]
    dp[0] = 1
    for i in range(6):
        for j in range(ma[i]):
            z = sum
            while z >= weigth[i]:
                if dp[z - weigth[i]] == 1:
                    dp[z] = 1
                z -= 1

    print dp

def main1():
    total = 10
    name = ['a', 'b', 'c', 'd', 'e']
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    list = []
    for i in range(len(name)):
        a = []
        for i in range(10):
            a.append(0)
        list.append(a)

    for i in range(1, 10 + 1):
        for j in range(0, len(name)):
            if weight[j] > i:
                if j == 0:
                    list[j][i] = 0
                else:
                    list[j][i] = list[j-1][i]
            else:
                item_in_bag = 0
                if j == 0:
                    list[j][i] = value[j]
                    continue
                else:
                    item_in_bag = list[j-1][i - weight[j]] + value[j]

                if list[j - 1][i] > item_in_bag:
                    list[j][i] = list[j - 1][i]
                else:
                    list[j][i] = item_in_bag

    print list


main1()

