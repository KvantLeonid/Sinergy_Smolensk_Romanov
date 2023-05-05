for i in range(2023, 10**10, 2023):
    S=str(i)
    if S[0]=='1' and S[2:6]=='2139' and S[-1]=='4':
        print(i, i//2023)
