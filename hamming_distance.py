class Solution(object):
    def hammingDistance(self, x, y):
        res = x ^ y
        setBits = 0
  
        while (res > 0) :
            setBits += res & 1
            res >>= 1
        return setBits

if __name__ == '__main__':
        print Solution().hammingDistance(1, 4)