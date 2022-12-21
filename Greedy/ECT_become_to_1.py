N, K = input().split()

cnt1 = N - 1

if (N % K != 0):
    print(cnt1)
else:
    cnt2 = N // K
    if(cnt1 >= cnt2):
        print(cnt2)
    else:
        print(cnt1)
        