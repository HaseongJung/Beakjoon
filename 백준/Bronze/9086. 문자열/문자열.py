T = int(input())

for _ in range(T):
  word = input()
  word = list(word)
  print(word[0] + word[-1])