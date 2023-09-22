import director
print("welcome play what is your name")
name = director.giveName(input())
print("good to meet you " + name)
print(f"it is troubling time {name} \nwould you like to go left or right?(L or R)")
director.firstChoice(input().upper(), name)
