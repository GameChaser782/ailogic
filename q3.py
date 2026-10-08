def swap(nums, i, j):
    a = nums[j]
    nums[i]=nums[j]
    nums[j]=a
    return nums

def solve(nums):
    i = 0
    for i in range(len(nums)-1):
        if nums[i+1]<nums[i]:
            break
        else:
            i = i + 1

    if i!=len(nums)-1:
        swap(nums, i, i+1)
        solve(nums[i+1:])
    else:
        nums.sort()

    return nums

def main():
    nums = [1,2,3]
    solve(nums)
    print(nums)
    return nums
    