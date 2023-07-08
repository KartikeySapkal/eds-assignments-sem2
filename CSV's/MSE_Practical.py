import csv
from collections import Counter
from statistics import mean

f1 = open("CSV's/dataset7.csv", "r")

home_win = []
teams = []
home_matches = []
Home_win_percentage = []
away_win = []

while (True):
    data = f1.readline()
    if not data:
        break;
    # print(data)
    data = data.replace("\n", "")
    temp = data.split(",")
    # print(temp)
    home_win.append(temp[1])
    teams.append(temp[0])
    home_matches.append(temp[3])
    Home_win_percentage.append(temp[5])
    away_win.append(temp[2])


del away_win[0]
# print(away_win)
# print(Home_win_percentage)

# print(home_matches)
del home_matches[0]

# print(teams)
del teams[0]
# print(teams)

# print(home_win)
del home_win[0]
del Home_win_percentage[0]
# print(home_win)

home_win_list = []
home_matches_list = []
HomePercent = []
away_win_list = []

for i in range(len(away_win)):
    away_win_list.append(int(away_win[i]))

# print("\n\n\n\nAwayWin: ",away_win_list)


for i in range(len(home_win)):
    home_win_list.append(int(home_win[i]))
    HomePercent.append(float(Home_win_percentage[i]))

# print("\n\n\nHomePercent",HomePercent)

for i in range(len(home_matches)):
    home_matches_list.append(int(home_matches[i]))

# print(home_win_list)


home_win_dict = {}
home_matches_dict = {}
for i in range(len(teams)):
    home_win_dict.update({teams[i]: home_win_list[i]})

for i in range(len(teams)):
    home_matches_dict.update({teams[i]: home_matches_list[i]})
# print(home_matches_list)
# print(home_win_dict)

HomeDict = Counter(home_win_dict)

# print(HomeDict)

HomeList = sorted(HomeDict.items(), key=lambda x: x[1], reverse=True)

# print(HomeList)

print(
    f"Query:1\nTeam Who won most matches in thier home city is: {HomeList[0][0]}")
print(f"They Have Won {HomeList[0][1]} matches\n\n")

print("Query:2\nAverage away win matches for all teams is: ",
      mean(away_win_list), "\n\n")

# print(home_matches_dict)

matches_dict = Counter(home_matches_dict)

# print(matches_dict)

MatchesList = sorted(matches_dict.items(), key=lambda x: x[1], reverse=True)
# print(MatchesList)

print(
    f"Query:3\nTeams Who has played most Home Matches is: {MatchesList[0][0]}\nThey Have Played {MatchesList[0][1]} matches\n\n")

PercentDict = {}

for i in range(len(HomePercent)):
    PercentDict.update({teams[i]: HomePercent[i]})

# print(PercentDict)

PercentCounter = Counter(PercentDict)

PercentList = sorted(PercentCounter.items(), key=lambda x: x[1], reverse=False)

# print(PercentList)

print(
    f"Query:4\nTeam Who Have minimum home win matches in percentage is {PercentList[0][0]}\nTheir won percentage are: {PercentList[0][1]}\n")
