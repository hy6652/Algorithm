# 문제: 연결 리스트ㅓ가 팰린드롬 구조인지 판별
import collections
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. 리스트 변환
def isPalindrome(head: ListNode) -> bool:
    # head = ListNode -> 첫 노드를 head로 지정.
    q: List = []

    if not head:
        return True
    
    node = head
    while node is not None:
        # 데이터 추가
        q.append(node.val)
        # next가 노드의 다음 포인터이므로 다음 노드를 node에 저장
        node = node.next
        # 따라서 linked list의 모든 데이터가 q에 저장
    

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True

# 2. 데크 이용
## 리스트 풀이에서 두 부분만 변경
def isPalindrome(head: ListNode) -> bool:
    # 변경 1
    q: Deque =  collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        # 변경 2
        if q.popleft() != q.pop():
            return False

    return True

# 3. 런너 이용
def isPalindrome(head: ListNode):
    rev = None
    slow = fast = head

    # 런너를 이용한 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    
    # 입력값이 홀수일 때 slow 런너 한 칸 더 이동
    if fast:
        slow = slow.next
    
    # 팰린드롬 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev