#12??36*1
for i in range(1200361, 10**8):
    if i%273==0 and str(i)[:2]=='12' and str(i)[4:6]=='36' and str(i)[-1]=='1':
        print(i,i//273)