with open('input.txt') as f:
    lines = f.read().split('\n')

safe_count = 0
for line in lines:
    all_nums = [int(x) for x in line.split()]

    for j in range(len(all_nums)):
        nums = all_nums[:j] + all_nums[j+1:]

        safe_asc = True
        safe_desc = True

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if not (1 <= diff <= 3):
                safe_asc = False
                break

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if not (-3 <= diff <= -1):
                safe_desc = False
                break

        if safe_asc or safe_desc:
            safe_count += 1
            break

print(f'Part 2: {safe_count}')
