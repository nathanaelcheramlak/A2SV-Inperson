# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num != 0:
            self.prefix.append(self.prefix[-1] * num)    
        else:
            self.prefix = [1]   

    def getProduct(self, k):
        """0
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-(k + 1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)