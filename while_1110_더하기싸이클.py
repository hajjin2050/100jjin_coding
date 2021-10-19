num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)

## //연산과 % 연산 주의 :
  // => 몫 | % => 나머지 반환함
   10으로 나눈 몫(//) => 10의 자릿수
   10으로 나눈 나머지(%) => 1의 자릿수
