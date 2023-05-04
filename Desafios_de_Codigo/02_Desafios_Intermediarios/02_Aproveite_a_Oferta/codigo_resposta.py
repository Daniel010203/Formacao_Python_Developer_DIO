T = int(input())
while T > 0:
  T -= 1
  N, K = input().split()
  N = int(N)
  K = int(K)
  total = int(int(N % K) + int(N / K))
   
  print(total)