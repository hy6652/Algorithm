# 문제: 정렬되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# 1. 재귀 구조로 연결
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # l1과 l2에는 빈 리스트가 올 수 있고, 둘 중 하나만 비어있을 수도 있다.
    # 둘 다 비어있으면 빈 값을 리턴하면 되고, 하나만 비어있으면 채워있는 리스트만 리턴하면 된다.
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


# 2. 풀어쓰기 (유튜브 참고, 노션에 링크 있음)
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 두 연결 리스트를 오름차순으로 하나로 합쳐야 함
    if None in (l1, l2):
        return l1 or l2
    
    # from <= to 관계에서 from의 next를 to로 연결시켜야함
    # 따라서 l1.val과 l2.val 중에 작은 값을 처음에 fromPtr로 지정
    ans = None
    if l1.val <= l2.val:
        # fromPtr = l1
        # toPtr = l2
        # ans = fromPtr
        
        # 아래 부분이 위 주석을 정리한 모습
        ans = fromPtr = l1
        toPtr = l2
    else:
        # fromPtr = l2
        # toPtr = l1
        # ans = fromPtr

        # 아래 부분이 위 주석을 정리한 모습
        ans = fromPtr = l2
        toPtr = l1
    
    while fromPtr != None:
        # step 1: fromPtr이 toPtr보다 작다
        if fromPtr.val <= toPtr.val:
            # step 2: from <= to를 만족하는 상태가지 fromPtr을 최대한 전진
            ## 리트코드 조건중에 두 연결 리스트가 non-decreasing order로 정렬되어 있다고 써있다. 즉 다음 노드가 이전 노드보다 작을 일은 없다는 것을 의미한다.
            while fromPtr.next != None and fromPtr.next.val <= toPtr.val:
                fromPtr = fromPtr.next
            
            # step 3: fromPtr의 next를 toPtr로 연결. 바로 연결하면 fromPtr의 현 next 노드의 참조를 잃어버리게 되기 때문에 temp에 먼저 저장
            # temp = fromPtr.next
            # fromPtr.next = toPtr

            # step 4: fromPtr이 temp값, 즉 원래 next 노드 값을 갖게 하여 앞으로 한 칸 전진하게 한다.
            # fromPtr = temp

            # step 3 & step 4
            fromPtr.next, fromPtr = toPtr, fromPtr.next
        
        # step 1-1: 만약 fromPtr이 toPtr보다 작지 않으면, 작은 값에서 큰 값을 가리킬 수 있도록 from과 to의 위치를 변경한다. 이때 기존 from의 next node를 잃지 않기 위해서 temp에 저장한다.
        else:
            # temp = fromPtr
            # fromPtr = toPtr
            # toPtr = temp

            # 위 코드를 정리한 모습
            # 왼쪽 값이 먼저 실행되서 (= 뒤의)toPtr의 값을 (= 앞의)fromPtr에 넣어주고, 원래 있던 fromPtr의 값을 어딘가에 저장해 뒀다가 그 값을 이용해서 (= 뒤의)fromPtr의 값을 (= 앞의)toPtr에 할당한다.
            fromPtr, toPtr = toPtr, fromPtr
    return ans