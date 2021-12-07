import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)


# sort() => 정렬된값 저장 시간효율0
# set => 정렬된값 저장 x. 시간효율 x
#readline 과  input 비교 했을떄 10배가까이 시간차이남
#/n줄로 받는 readline 출력오류 해결하기위해 .strip() 추가
