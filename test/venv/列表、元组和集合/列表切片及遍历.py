players = ['charles', 'martina', 'michael', 'florence', 'eli']

#输出前三个队员
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())                   #title()函数首字母大写，其余小写

print("************万恶的分割符************")

#输出后三个队员
print("Here are thr last three players on my team:")
for player in players[-3:]:
    print(player.title())

print("************万恶的分割符************")

#不切片复制列表
like_players = players                  #不切片复制会使两个变量指向同一个列表
like_players.append("ice")
print(players)
del players[-1]

print("************万恶的分割符************")

#切片复制列表
like_players = players[:]                  #切片复制会建造一个副本储存到新变量里
like_players.append("ice")
print(players)

