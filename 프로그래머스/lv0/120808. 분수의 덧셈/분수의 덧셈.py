import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    num = numer1*denom2 + numer2*denom1
    n = math.gcd(denom, num)
    denom /= n
    num /= n
    answer.append(num)
    answer.append(denom)

    return answer