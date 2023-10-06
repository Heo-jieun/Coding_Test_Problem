from collections import Counter
def solution(array):
    counts = Counter(array)
    m_c = counts.most_common(2)
    answer = m_c[0][0]
    if len(m_c) > 1:
        if m_c[1][1] == m_c[0][1] :
            answer = -1
    return answer