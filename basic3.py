ame = 2000
cafe = 3000
capu = 3500
ame1 =int(input("아메리카노 판매 개수 : "))
cafe1 =int(input("카페라떼 판매 개수 : "))
capu1 =int(input("카푸치노 판매 개수 : "))
sales=ame*ame1
sales=sales+cafe*cafe1
sales=sales+capu*capu1
print("총 매출은",sales,"입니다.")

#bmi
kg =float(input("몸무게를 kg 단위로 입력하시오 : "))
m =float(input("키를 미터 단위로 입력하시오 : "))
print("당신의 BMI = ",kg/(m**2))


money = int(input("투입한 돈 : "))
price = int(input("물건값 : "))
change=money-price
print("거스름돈 : ",change)
coin500won = change//500
change=change%500 #큰 잔돈부터 순서대
coin100won = change//100
change=change%100
coin50won = change//50
change=change%50
coin10won = change//10
print("500원 동전의 개수 : ",coin500won)
print("100원 동전의 개수 : ",coin100won)
print("50원 동전의 개수 : ",coin50won)
print("10원 동전의 개수 : ",coin10won)