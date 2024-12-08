from itertools import product


def helper(nums, ops):
    result = nums[0]
    for op, num in zip(ops, nums[1:]):
        if op == "+":
            result += num
        elif op == "*":
            result *= num

    return result


count = 0
with open("input.txt", "r") as file:
    for line in file:
        if ":" not in line:
            continue
        target, numbers = line.strip().split(":")
        target = int(target)
        nums = [int(num) for num in numbers.strip().split()]
        for ops in product(["+", "*", "||"], repeat=len(nums) - 1):
            res = nums[0]
            for i, op in enumerate(ops):
                if op == "+":
                    res += nums[i + 1]
                if op == "*":
                    res *= nums[i + 1]
                if op == "||":
                    res_s = str(res) + str(nums[i + 1])
                    res = int(res_s)
            if res == target:
                count += target
                break
print(count)
