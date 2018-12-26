'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
'''
需要两个栈Stack1和Stack2，push的时候直接push进Stack1。
pop需要判断Stack1和Stack2中元素的情况，Stack1空的话，直接从Stack2 pop，
Stack1不空的话，把Stack1的元素push进入Stack2，然后pop Stack2的值。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    # def push(self, node):
    #     self.stack1.append(node)
    # def pop(self):
    #     if len(self.stack2) == 0 and len(self.stack1) == 0:
    #         return
    #     elif len(self.stack2) == 0:
    #         while len(self.stack1) > 0:
    #             self.stack2.append(self.stack1.pop())
    #     return self.stack2.pop()
    def push(self, value):
        self.stack1.append(value)
    
    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) != 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        elif len(self.stack1) == 0:
            raise ValueError('the queue is empty')
        return self.stack2.pop()
        



P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())