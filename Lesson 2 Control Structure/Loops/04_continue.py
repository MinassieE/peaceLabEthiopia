# Example 1
for i in range(1, 6):
    if i == 3:
        # print("Skipping number 3.")
        continue
    print(i)

# Example 2
count = 0
while count < 5:
    count += 1
    if count == 3:
        # print("Skipping number 3.")
        continue
    print(count)