str1 = 'パトカー'
str2 = 'タクシー'
ans = ''.join([i + j for i, j in zip(str1, str2)])
ans
print(ans)