while 1 :
    a,b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    else :
        print(a + b)
        
        #변수가 2개인 점 주의 
        # map 으로 받아준다!
        #while 1 은 True 와 같음
