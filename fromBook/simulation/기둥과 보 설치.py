import copy as cp

def check(cmd,progress,n):
    x,y,typ = cmd
    # 기둥 설치인 경우
    if typ == 0:
        # 땅위에 설치하는 경우이거나, 밑에 기둥이 있거나, 보 위에 세우는 경우 일 때
        if (y==0) or ([cmd[0],cmd[1]-1,0] in progress):
            return True
        elif (x > 0) and ([x-1,y,1] in progress):
            return True
        elif (x < n-1) and ([x,y,1] in progress):
            return True
        else:
            return False               
    # 보 설치인 경우
    else:
        if y >= 1 and x < n-1:
            # 한쪽 끝부분이 기둥위에 있거나, 양 끝 부분이 보에 연결되어 있을때
            if ([x,y-1,0] in progress) or  ([x+1,y-1,0] in progress):
                return True
            elif ([x+1,y,1] in progress) and ([x-1,y,1] in progress):
                return True
            else:
                return False
        else:
            return False



def solution(n, build_frame):
    progress = []
    for cmd in build_frame:
        # 설치인 경우
        if cmd[3] == 1:
            # 이미 있다면
            if cmd[:-1] in progress:
                continue
            if check(cmd[:-1],progress,n):
                progress.append(cmd[:-1])
        # 삭제인 경우
        else:
            temp_progress = cp.deepcopy(progress)
            try:
                temp_progress.remove(cmd[:-1])
            except:
                continue
            for t in temp_progress:
                temp_progress2 = cp.deepcopy(temp_progress)
                temp_progress2.remove(t)
                if check(t,temp_progress2,n):
                    pass
                else:
                    continue
            progress = temp_progress
    return sorted(progress)
