
a = 'sdfaaaaddfesdfess'
r = ''
cnt = 1
print(a)
for i in range(len(a)):
    if a[i:i+1] == a[i+1:i+2]:
        cnt += 1
    else:
        r += a[i:i+1]
        r += str(cnt) if cnt > 1 else ''
        cnt = 1
print(r)
