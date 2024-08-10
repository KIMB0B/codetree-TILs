n = int(input());
nums = [i for i in range(1, 10)]

for i in range(0, n*n):
    print(nums[i%9], end = ' ');
    if (i+1) % n == 0:
        print();