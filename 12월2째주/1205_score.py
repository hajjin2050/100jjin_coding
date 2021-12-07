n, new ,p = map(int, input().split())
if n == 0 :
    print(1)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new :
        print(-1)
    else :
        res = n + 1
        for i in range(n):
            if score[i] <= new:
                res = i + 1
                break
        print(res)
        
        #n을 기준으로 n==0 인경우 에서의 p n>0인 경우에서의 p n==p인경우에서의 출력값 탐색
