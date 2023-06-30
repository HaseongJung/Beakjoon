H1, M1, S1 = map(int, input().split(':'))
H2, M2, S2 = map(int, input().split(':'))

t = H2*3600+M2*60+S2 - (H1*3600+M1*60+S1)

if t<0:
    t += 60 * 60 * 24
    
h = t // 3600
m = (t % 3600) // 60
s = t % 60

print("%02d:%02d:%02d" % (h,m,s))