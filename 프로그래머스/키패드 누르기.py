# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.



def solution(numbers, hand):
    answer = ''

    keypad = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            '*':[3,0], 0:[3,1], '#':[3,2]
        }

    left_hand = '*'
    right_hand = '#'
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_hand = num

        if num in [3, 6, 9]:
            answer += 'R'
            right_hand = num

        if num in [2, 5, 8, 0]:
            current = keypad[num] # num = 5 -> current = [1, 1]
            current_left = keypad[left_hand] # current_left = 4 -> [1, 0]
            current_right = keypad[right_hand] # current_right = 3 -> [0, 2]
            
            # 절대값을 구하는 함수인 abs로 계산
            left_pos = abs(current_left[0] - current[0]) + abs(current_left[1] - current[1]) # 0 + 1
            right_pos = abs(current_right[0] - current[0]) + abs(current_right[1] - current[1]) # 1 + 1

            if left_pos > right_pos:
                answer += 'R'
                right_hand = num
            if right_pos > left_pos:
                answer += 'L'
                left_hand = num
            if left_pos == right_pos:
                if hand == 'right':
                    answer += 'R'
                    right_hand = num
                if hand == 'left':
                    answer += 'L'
                    left_hand = num

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))