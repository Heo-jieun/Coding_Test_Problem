def solution(rsp):
    rsp_win = {"2":"0", "0":"5", "5":"2"}
    return ''.join(rsp_win[i] for i in rsp)