# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius + 273.15, celsius * 1.8 + 32]