# 문제: 인덱스 m에서 n까지를 역순으로 변경. m은 1부터 시작

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head or m == n:
        return head
    
    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(m-1):
        start = start.next
    end = start.next
    
    # 노드 뒤집기
    ## 1. 풀어쓰기
    # for _ in range(n - m):
    #     tmp = start.next
    #     start.next = end.next
    #     end.next = end.next.next
    #     start.next.next = tmp

    ## 2. 다중 할당
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next
