

val_2 = '0b' + input()     ## 2진수앞에 문자 붙여주고


val_10 = int(val_2, 2)    ## 2진수 -> 십진수로 변환

val_8 = format(val_10, 'o')   ## 10진수 8진수로 변환
print(val_8)
