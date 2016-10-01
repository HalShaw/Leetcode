class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = reduce(lambda x, y : x ^ y, nums)#先计算所有元素的异或
        lowbit = xor & -xor #令lowbit = xor & -xor，lowbit的含义为xor从低位向高位，第一个非0位所对应的数字
        a = b = 0#例如假设xor = 6（二进制：0110），则-xor为（二进制：1010，-6的补码，two's complement）则lowbit = 2（二进制：0010）
        for num in nums:
            if num & lowbit:#可知a & lowbit与b & lowbit的结果一定不同，然后就异或分离出a，b
                a ^= num
            else:
                b ^= num
        return [a, b]

    def singleNumber(self, nums):#精简版
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]

    def singleNumber(self, nums):#精简加高效版
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]                