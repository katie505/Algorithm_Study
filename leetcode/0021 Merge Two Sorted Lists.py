#!/usr/bin/env python
# coding: utf-8

# In[9]:


#정렬되어 있는 두 연결 리스트를 합쳐라


# In[10]:


#풀이1
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def my_print(l1: ListNode, l2:ListNode):

    print("l1 : ", end="")
    while l1 is not None:
        print(f'{l1.val} -> ', end="")
        l1 = l1.next
    print()

    print("l2 : ", end="")
    while l2 is not None:
        print(f'{l2.val} -> ', end="")
        l2 = l2.next
    print()


i = 0

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        global i
        i+=1
        print()
        print(f'{i}번째 mergeTowLists')


        if (not l1) or (l2 and l1.val > l2.val): # l1에 객체가 없거나 l2에 객체가 존재하고, l1, l2노드를 비교했을 때 l1의 value가 더 컸을 때 실행
            print("첫번째 조건문")
            l1, l2 = l2, l1
            my_print(l1, l2)

        if l1:
            print("두번째 조건문")
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


l1 = ListNode(1)
l1.next= ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s = Solution()
answer = s.mergeTwoLists(l1, l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

