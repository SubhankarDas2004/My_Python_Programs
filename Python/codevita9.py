n = int(input())

five = n // 5
remaining = n % 5

two = remaining // 2
one = remaining % 2

total_coins = five + two + one

print(total_coins, five, two, one)
