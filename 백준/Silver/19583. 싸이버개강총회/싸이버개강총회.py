import sys
input = sys.stdin.readline

START, END, STREAMING_END = input().split()

attendance = {}
for chat in sys.stdin:
    # temp = input()
    if (chat == "\n"):
        break
    else:
        chat = list(chat.split())
        # START 이하 채팅 친 사람 기록
        # END ~ STREAMING_END 사이 채팅 친 사람 기록
        # 둘 다 있으면 기록.
        if chat[0] <= START:
            attendance[chat[1]] = 0
        elif END <= chat[0] <= STREAMING_END and chat[1] in attendance.keys():
            attendance[chat[1]] = 1

# print(attendance)
print(sum(attendance.values()))
