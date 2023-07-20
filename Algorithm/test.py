a = ["0123456789", "9876543210", "9999999999999"]
answer = []
for i in a:
    if int(i[5:11]) > 50000:
        answer.append(int(i[5:10]))
print(answer)
