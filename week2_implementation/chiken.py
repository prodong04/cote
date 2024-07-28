import itertools


def distance(lst1, lst2):
    lst = [ai - bi for ai, bi in zip(lst1, lst2)]
    return abs(lst[0]) + abs(lst[1])    


hou, mar = map(int, input().split())
lst = []
for i in range(hou):
    lst.append(input().split())

chiken = []
house = []

### lst로 받았다고 가정하고, 위치부터 먼저 찾자. 
for i in range(hou):
    for j in range(hou):
        if int(lst[i][j]) == 1:
            house.append([i, j])
        elif int(lst[i][j]) == 2:
            chiken.append([i, j])
#최단거리 초기화
# chiken과 house의 위치를 받았으니, 이제 거리를 계산하자.
# maximum size가 이미 크면 문제가 안됨. 
if mar >= len(chiken):
    answer = 0
    for i in range(len(house)):
        dist = 1e9
        for j in range(len(chiken)):
            if distance(chiken[j], house[i]) < dist:
                dist = distance(chiken[j], house[i])
        answer += dist
    min_awswer = answer

# maximum size가 작으면, m개의 치킨집을 선택해야함.
elif mar < len(chiken):
    min_awswer = 1e9
    # 치킨 집의 경우의 수에 대하여 조합을 구하자.
    for i in itertools.combinations(chiken, mar):
        answer = 0
        # 각 집마다 제일 가까운 치킨집을 찾는다. 
        for k in range(len(house)):
            temp = 1e9
            for p in range(mar):
                if distance(i[p], house[k]) < temp:
                    temp = distance(i[p], house[k])
            
            answer += temp
        if answer < min_awswer:
            min_awswer = answer
                    
            
print(min_awswer)
    
    
    
            
        
    