#포맷 코드와 숫자 함께 사용하기
#2. 소수점 표현하기
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234
#소수점 네 번째 자리만 표시하는 것

#format 함수를 사용한 포매팅
#숫자 바로 대입하기
"I eat {0} apples.".format(3)
"I eat {0} corn".format(1)
"I eat {0} apples.".format("five")
number  = 3
"I eat {0} apples.".format(number)
#2개 이상의 값 넣기
number= 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
#이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
#인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=4)