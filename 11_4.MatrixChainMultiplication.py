# if __name__ == '__main__':
#     n = int(input())
#     p = [0]*n*2
#     m = [[ None for j in range(n) ] for i in range(n)]
#     for i in range(n):
#         m[i][i] = 0
#     for i in range(n):
#         p[i*2], p[i*2+1] = map(int, input().split())
#     # print(p)
#
#     for l in range(1,n-1):
#         for i in range(n-l):
#             j = i + l
#             m[i][j] = 1000000000
#             for k in (i,j-1):
#                 m[i][j] = min([m[i][j], m[i][k] + m[k+1][j] + p[i-1] * p[k]] * p[j])
#
#     print(m[0][n-1])


N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

INF = 10**18
dp = [[INF]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])