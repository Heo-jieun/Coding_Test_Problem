def solution(ineq, eq, n, m):
    sign = ineq
    if eq == "=":
        sign += eq
    exp = str(n)+sign+str(m)
    return int(eval(exp))