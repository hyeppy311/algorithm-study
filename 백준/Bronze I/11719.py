

while True :
  try :                # try 예외처리 시작
    print(input())      # input() 함수에서 파일이 끝날때 에러 발생
  except EOFErrorr :    # End Of File (파일의 끝)을 만났을때 생기는 에러 
    break               # except에서 빠져나오기 
