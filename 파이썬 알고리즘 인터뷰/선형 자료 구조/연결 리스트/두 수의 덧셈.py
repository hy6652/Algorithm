# 문제: 역순으로 저장된 연결 리스트의 숫자를 더하라
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 자료형 변환
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    
    # 연결 리스트를 파이썬 리스트를 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        # 최종 계산 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


# 2. 전가산기 구현
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # root는 더미 값, head는 첫 값을 설정
    root = head = ListNode(0)

    # 노드에 담긴 수는 한 자리수만 가능, 따라서 두 자리 수가 되면 10으로 나눈 몫을 저장할 곳이 필요
    # 예를 들어 그냥 덧셈에서도 15+17을 하면 처음 일의 자리 수가 5+7로 12가 된다.
    # 여기서 2만 남기고 1은 십의 자리 수로 넘어가는데, 이 경우와 똑같다.
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next
