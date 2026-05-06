n = int(input())                  # number of teams
teams = input().split()           # team names
teams.sort()

points = [0] * n                  # points table
valid = True

for _ in range(3):                # number of matches
    t1, t2, p1, p2 = input().split()
    
    if t1 == t2:
        print("Invalid Input")
        valid = False
        break
    
    points[teams.index(t1)] += int(p1)
    points[teams.index(t2)] += int(p2)

# sorting teams based on points
if valid:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if points[i] < points[j]:
                points[i], points[j] = points[j], points[i]
                teams[i], teams[j] = teams[j], teams[i]

    print(teams)
