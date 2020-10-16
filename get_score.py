import heapq

def get_score(my_stone_num,opp_stone_num):
    """ 남아있는 돌의 수를 바탕으로 점수 계산하는 함수  """
    # my_stone_num -> 남은 우리 돌의 개수 
    # opp_stone_num -> 남은 상대편 돌의 개수

    # 우리 돌을 잃으면 -3, 상대 돌을 까면 +2 => 최종 점수 계산 후 최대값 도출
    my_score = (7 - my_stone_num) * -3 # 떨어진 우리 돌의 개수 * -3
    opp_score = (7 - opp_stone_num) * 2 # 떨어진 상대 돌의 개수 * +2
    total_score = my_score + opp_score # 최종 점수 도출

    return total_score #최종 점수 반환

def get_priority(score_list):
    """ 가장 잘 친 경우 3가지를 반환하는 함수 """
    # score_list -> 점수 정보 모두를 갖고 있는 리스트 

    heap= [] # 힙 생성
    for score in score_list:
        heapq.heappush(heap,int(score)*-1) # 받아온 점수 리스트 힙에 push
        # 내림차순으로 정렬 해야 하기 때문에 -1을 곱하여 푸쉬 한다.   
        #print(heap)

    list = []
    for i in range(0,3): # 3개만 뽑는다
        list.append(-1*heapq.heappop(heap)) # 제일 큰값을 차례대로 뽑는데 

    return list # 큰값 3개 뽑은거 return



""" 테스트용 코드 """

file = open('test_tw.txt', mode='rt', encoding='utf-8')
stone_infos = file.readlines()

score_info = []
for stone_info in stone_infos:
    tmp = stone_info.split(' ') # ' '를 기준으로 나눔
    get_score(int(tmp[0]),int(tmp[1])) # 우리돌 상대돌  집어 넣어서 점수 계산
    score_info.append(get_score(int(tmp[0]),int(tmp[1]))) # 리스트에 추가
priority_list = get_priority(score_info) # 리스트 보내서 3개 불러옴

print("\n"+"최대값 3개")
print(priority_list)
