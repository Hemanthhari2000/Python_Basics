
# ======================= Problem =======================

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

# ======================= Test Case =======================
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

# ======================= Solution =======================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 5 1 2 -> 2 1 5

def getCount(node_1):
    temp = node_1
    count = 0
    while temp:
        count += 1
        temp = temp.next
    return count


fnode_1 = ListNode(val=2)
fnode_2 = ListNode(val=4)
fnode_3 = ListNode(val=3)

fnode_1.next = fnode_2
fnode_2.next = fnode_3


snode_1 = ListNode(val=3)
snode_2 = ListNode(val=4)
snode_3 = ListNode(val=2)

snode_1.next = snode_2
snode_2.next = snode_3


fake = ListNode(0)
p = fake

p1 = fnode_1
p2 = snode_1

carry = 0

while p1 != None or p2 != None:
    runningSum = carry
    if (p1 != None):
        runningSum += p1.val
        p1 = p1.next
    if (p2 != None):
        runningSum += p2.val
        p2 = p2.next

    if (runningSum > 9):
        carry = 1
        runningSum -= 10
    else:
        carry = 0

    new_node = ListNode(val=runningSum)
    p.next = new_node
    p = p.next

if carry > 0:
    carry_node = ListNode(val=carry)
    p.next = carry_node

print(fake.val)
print(fake.next.val)
