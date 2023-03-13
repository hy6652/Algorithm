# 문제: 연결 리스트 뒤집기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 재귀 구조
def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)


# 2. 반복 구조
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev


# 3. 풀어쓰기
# 블로그 참고, 링크는 노션에 있음
def reverseList(head: ListNode) -> ListNode:
    node = head
    prev = None

    while node:
        temp = node.next
        
        if temp == None:
            head = node
        
        node.next = prev
        prev = node
        node = temp
    
    return node
