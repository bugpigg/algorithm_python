from sys import stdin

n,m = list(map(int,stdin.readline().split()))
x,y,direction = list(map(int,stdin.readline().split()))
field = [list(map(int,stdin.readline().split())) for _ in range(n)]

been = [[0]*m for _ in range(n)]
been[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
been = []
while True:
    # turn Left
    turnLeft()
    fx = x + dx[direction]
    fy = y + dy[direction]
    if been[fx][fy] ==0 and field[fx][fy] == 0:
        been[fx][fy] = 1
        x = fx
        y = fy
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        fx = x - dx[direction]
        fy = y - dy[direction]
        if field[fx][fy] == 0:
            x = fx
            y = fy
            turn_time = 0
        else:
            break
print(cnt)