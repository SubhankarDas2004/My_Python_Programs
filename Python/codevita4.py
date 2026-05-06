# Read input as a string
st = input()

# Split the input using comma
values = st.split(",")

# Convert input values to integers
n = int(values[0])
k = int(values[1])

# List to store all factors of n
factors = []

# Loop from 1 to n
for i in range(1, n + 1):
    # Check if i is a factor of n
    if n % i == 0:
        factors.append(i)

# Check if n has less than k factors
if len(factors) < k:
    print(1)
else:
    # Print the kth largest factor
    print(factors[-k])
