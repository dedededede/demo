# -*- encoding: utf8 -*-
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #遇1  +1,遇0  -1,每次看看和第一次出现总和的起点的距离
        result=0
        start=0
        traj={0:-1}
        # print traj
        for i ,one in enumerate(nums):
            if one==1:
                start+=1
            elif one==0:
                start-=1
                
            if start in traj:
                result=max(i-traj[start], result)
            else:
                traj[start]=i
            # print result,traj,start
        return result

data_list = [0, 0, 1, 1, 0]
obj = Solution()
print "结果:", obj.findMaxLength(data_list)



