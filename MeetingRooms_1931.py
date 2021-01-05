# 백준 1931

N = int(input())
meeting = []
for i in range(N):
    start, end = map(int,input().split())
    meeting.append((start,end))

meeting = sorted(meeting, key = lambda x:(x[1],x[0]))

e = 0
done_meetings = []
for i in range(len(meeting)):
    if meeting[i][0] >= e:
        e = meeting[i][1]
        done_meetings.append(meeting[i])
print(len(done_meetings))