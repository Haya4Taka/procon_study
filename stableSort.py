import copy
n = int(input())
o_cards = input().split()
cards = copy.copy(o_cards)
s_cards = copy.copy(o_cards)

orders = {}
for i in range(n):
    for j in range(n-1, i, -1):
        if int(cards[j][1]) < int(cards[j-1][1]):
            cards[j], cards[j-1] = cards[j-1], cards[j]

print(*cards)
print("Stable")

orders_s = {}
for i in range(n):
    mini = i
    for j in range(i+1, n):
        if int(s_cards[mini][1]) > int(s_cards[j][1]):
            mini = j

    s_cards[i], s_cards[mini] = s_cards[mini], s_cards[i]

print(*s_cards)
if cards == s_cards:
    print("Stable")
else:
    print("Not stable")
