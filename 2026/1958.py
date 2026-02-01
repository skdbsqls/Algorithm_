"1958 LCS 3"

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

len1, len2, len3 = len(s1), len(s2), len(s3)
dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        for k in range(1, len3 + 1):
            if s1[i-1] == s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len1][len2][len3])

for k in range(len3 + 1):
    print(f"\n===== k = {k} | s3[:{k}] = '{s3[:k]}' =====")

    # 열 헤더 (s2)
    print("    ", end="")
    for j in range(len2):
        print(f"{s2[j]:>3}", end="")
    print()

    for i in range(len1 + 1):
        # 행 헤더 (s1)
        if i == 0:
            print("  ", end=" ")
        else:
            print(f"{s1[i-1]:>2}", end=" ")

        for j in range(1, len2 + 1):
            print(f"{dp[i][j][k]:>3}", end="")
        print()

"""
===== k = 0 | s3[:0] = '' =====
      b  d  e  f  g
     0  0  0  0  0
 a   0  0  0  0  0
 b   0  0  0  0  0
 c   0  0  0  0  0
 d   0  0  0  0  0
 e   0  0  0  0  0
 f   0  0  0  0  0
 g   0  0  0  0  0
 h   0  0  0  0  0
 i   0  0  0  0  0
 j   0  0  0  0  0
 k   0  0  0  0  0
 l   0  0  0  0  0
 m   0  0  0  0  0
 n   0  0  0  0  0

===== k = 1 | s3[:1] = 'e' =====
      b  d  e  f  g
     0  0  0  0  0
 a   0  0  0  0  0
 b   0  0  0  0  0
 c   0  0  0  0  0
 d   0  0  0  0  0
 e   0  0  1  1  1
 f   0  0  1  1  1
 g   0  0  1  1  1
 h   0  0  1  1  1
 i   0  0  1  1  1
 j   0  0  1  1  1
 k   0  0  1  1  1
 l   0  0  1  1  1
 m   0  0  1  1  1
 n   0  0  1  1  1

===== k = 2 | s3[:2] = 'ef' =====
      b  d  e  f  g
     0  0  0  0  0
 a   0  0  0  0  0
 b   0  0  0  0  0
 c   0  0  0  0  0
 d   0  0  0  0  0
 e   0  0  1  1  1
 f   0  0  1  2  2
 g   0  0  1  2  2
 h   0  0  1  2  2
 i   0  0  1  2  2
 j   0  0  1  2  2
 k   0  0  1  2  2
 l   0  0  1  2  2
 m   0  0  1  2  2
 n   0  0  1  2  2

===== k = 3 | s3[:3] = 'efg' =====
      b  d  e  f  g
     0  0  0  0  0
 a   0  0  0  0  0
 b   0  0  0  0  0
 c   0  0  0  0  0
 d   0  0  0  0  0
 e   0  0  1  1  1
 f   0  0  1  2  2
 g   0  0  1  2  3
 h   0  0  1  2  3
 i   0  0  1  2  3
 j   0  0  1  2  3
 k   0  0  1  2  3
 l   0  0  1  2  3
 m   0  0  1  2  3
 n   0  0  1  2  3
"""