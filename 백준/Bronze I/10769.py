
# 문자열 내 특정 문자 개수 세기 

s = input()

smile = s.count(":-)")
sad = s.count(":-(")

if smile == 0 and sad == 0 :
    print("none")
elif smile >sad : 
    print("happy")
elif smile == sad : 
    print("unsure")
elif smile < sad  : 
    print("sad")
    
    
    
# 정규식 써야 되나했는데 그럴 필요없었음.. 
# 다른코드의 경우 ":" 뒤의 ")"와 "("의 개수를 저장해서 비교한 후 단어 출력 
# count 함수가 저렇게 뭉텅이?로 개수를 세주는지 몰랐음. 

