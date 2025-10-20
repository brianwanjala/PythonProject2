nums = [1,9,5,3,8,6]
pos = 0
n = 1
def sort(nums):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[j],nums[i] = nums[i], nums[j]
    return nums
sort(nums)
print(f'new list is: {nums}')

def search(nums, n):
    l = 0
    u = len(nums)-1
    while l <= u:
        mid_index = (l+u)//2
        if nums[mid_index] == n:
            globals()["pos"] = mid_index +1
            return True
        else:
            if nums[mid_index] < n:
                l = mid_index + 1
            else:
                u = mid_index - 1
    return False
if search(sort(nums), n):
    print(f"found at {pos}")
else:
    print("not found")