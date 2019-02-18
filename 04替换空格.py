'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 简单代码替换
    # 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
    def replaceSpace(self, s):
        #在class下的函数入参需要有self
        if type(s) != str:
            return
            
        return s.replace(' ', '%20')
s = 'we are happy'
test = Solution()
print(test.replaceSpace(s))