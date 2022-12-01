def find_duplicate(nums):
    if type(nums) is not list or len(nums) < 2 or type(nums[0]) is not int:
        return False
    for number in nums:
        if number < 0:
            return False
        for next_number in range(nums.index(number) + 1, len(nums)):
            if number == nums[next_number]:
                return True
    return False


print(find_duplicate([1,2]))
