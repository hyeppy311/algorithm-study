'''
버블 정렬 
두 개의 인접 데이터를 비교, 앞에 있는 데이터가 뒤 보다 크면 자리를 바꾸는 것

조건체크(크기비교)와 턴(위치변경)은 데이터의 길이에서 -1 만큼 

턴은 밖에서 돌고 
조건 체크는 안에서 

for index range(데이터 길이 -1 ):   (턴)
 for index2  range(데이터 길이  -1):  (조건체크)
	if 앞 데이터 > 뒤 데이터 :
		swap(앞 데이터, 뒤 데이터) 


데이터가 정렬이 되어있다면 ?(Swap이 한번도 안일어난다면 ?)
flag를 넣는다 

알고리즘 분석 
반복문이 두 개 O(n^2)
최악의 경우, n(n-1)/2 
완전 정렬이 되어있는 상태의 최선 O(n)
'''

import random

# 기본 버블 정렬
def bubblesort(data):
    for index in range(len(data)-1):
        for index2 in range(len(data)-1):
            if data[index2] > data[index2 + 1] :
                data[index2], data[index2 + 1] = data[index2 + 1] , data[index2] #swap
    return data

data_list = random.sample(range(100),20)

print(bubblesort(data_list))
# [1, 4, 5, 10, 16, 17, 20, 25, 27, 37, 45, 47, 66, 67, 77, 78, 84, 89, 91, 95]


# 정렬이 되있는 부분 넘어가기 (조건체크 횟수 줄이기)  

def bubblesort_1(data):
    for index in range(len(data)-1):
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2 + 1] :
                data[index2], data[index2 + 1] = data[index2 + 1 ] , data[index2] 
    return data

data_list_1 = random.sample(range(100),20)

print(bubblesort_1(data_list_1))


# 정렬이 필요없는 경우 (정렬이 이미 되어 있는 경우)
'''
1.swap = 0 (교환이 일어나는지 확인하는 변수)
2.반복문 안에서 for index in range(len(data)-num-1)
3.정렬을 할 때마다 +=1 
4.반복문 안에서 if swap == 0, break
'''
def bubblesort_2(data):
    for index in range(len(data)-1):
        swap = False   # 턴 시작시 swap 초기화 (조건체크 밖에서 선언) , swap = 0 
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2 + 1] :
                data[index2], data[index2 + 1] = data[index2 + 1 ] , data[index2] 
                swap = True   # swap 있는 경우 , swap += 0
        if swap == False :   # 조건체크를 다 확인 후 바꿀게 없으면 체크 중단, 턴 다시 시작
            break 
        
    return data
    
data_list_2 = [1,2,3,7,8,9,5,6,4] 
print(data_list_2)
print(bubblesort_2(data_list_2))

# [19, 76, 29, 40, 48, 95, 64, 46, 77, 61, 23, 0, 27, 1, 65, 90, 53, 51, 74, 5]
# [0, 1, 5, 19, 23, 27, 29, 40, 46, 48, 51, 53, 61, 64, 65, 74, 76, 77, 90, 95]

# [1, 2, 3, 7, 8, 9, 5, 6, 4]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



# 정렬과정 보기

# from typing import MutableSequence

# def bubble_sort_verbose(a : MutableSequence) -> None :
#     """ 버블 정렬(과정 출력)"""
#     c_cnt = 0 # 비교 횟수
#     s_cnt = 0 # 교환 횟수
#     n = len(a)
#     for i in range(n-1) :
#         print(f'패스 {i+1}')
#         for j in range(n-1, i, -1) :
#             for m in range(0, n-1) :
#                 print(f'{a[m]:2}') + (" " if ) 
