# Read the number of participants
n = int(input())

# Read the scores as a list of integers
scores = list(map(int, input().split()))

# Remove duplicates and sort the list in descending order
unique_scores = sorted(set(scores), reverse=True)

# Print the second highest score
print(unique_scores[1])
