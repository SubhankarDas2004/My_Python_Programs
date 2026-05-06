n, k = map(int, input().split())

parcel = list(map(int, input().split()))

minimum = min(parcel)
maximum = max(parcel)
kth_value = parcel[k - 1]

# calculate effort using twice efforts
effort = (kth_value * minimum) + (kth_value * minimum) + (maximum * minimum)

print(effort)
