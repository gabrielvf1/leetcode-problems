class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result_list = [0]
        for index, value in enumerate(nums):
             result_list.append(value + result_list[index])
        return result_list[1:]

# Time Submitted   | Status     | Runtime | Memory  |  Language
# 08/08/2022 09:02 | Accepted	|  46 ms  | 13.6 MB |   python