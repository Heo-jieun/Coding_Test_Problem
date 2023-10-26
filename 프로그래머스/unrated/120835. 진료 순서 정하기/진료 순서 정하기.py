def solution(emergency):
    emergency_score = sorted(emergency, reverse = True)# 점수가 높은순으로 reverse = True (내림차순) 정렬
    # emergency_score 리스트에서 값이 처음으로 나타나는 위치(인덱스)를 찾는 것을 의미
    ranks = [emergency_score.index(s) + 1 for s in emergency] # 등수는 1부터 시작되니까 + 1 넣어줌
    return ranks