# 문제: 연결 리스트를 입력받아 페어 단위로 스왑
## TODO: 다시 풀어보기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 값만 교환
def swapPairs(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


# 2. 반복 구조로 스왑
def swapPairs(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b
        
        # 다음 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    
    return root.next


# 3. 재귀 구조로 스왑
def swapPairs(head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값을 리턴 받음
        head.next = swapPairs(p.next)
        p.next = head
        return p
    return head
