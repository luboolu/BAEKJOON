#BAEKJOON 1157번

s = input().upper()
sSet = list(set(list(s)))
count_result = []
for i in sSet:
    count_result.append(s.count(i))

if len(count_result) == 1 or sorted(count_result)[0] != sorted(count_result)[1]:
    print(str(sSet[count_result.index(max(count_result))]))
else:
    print("?")