import sys

input = sys.stdin.readlines
n = input()
print(*n, sep='')   ## 리스트에서 꺼내서 공백없이 출력


## readline : 한 줄씩 읽음
## readlines : 읽은 것을 리스트에 개행문자(\n) 포함해서 담음
