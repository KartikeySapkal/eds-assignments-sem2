a = int(input())
score = [ ]
score_string = input()
score_list = score_string.split(" ")
print(score_list)
scores = [ ]
for i in range(a):
    scores.append(int(score_list[i]))  

Max = max(scores)
Min = min(scores)
avg = (Max + Min) / 2

sum = Max + Min + avg

print(sum)