def is_valid(target, nums):
    if len(nums) == 1:
        return target == nums[0]
    if is_valid(target, [nums[0] + nums[1]] + nums[2:]):
        return True
    if is_valid(target, [nums[0] * nums[1]] + nums[2:]):
        return True
    return False


ans = 0
with open("input.txt", "r") as file:
    for line in file:
        if ":" not in line:
            continue
        target, numbers = line.strip().split(":")
        target = int(target)
        nums = [int(num) for num in numbers.strip().split()]

        if is_valid(target, nums):
            ans += target
print(ans)
