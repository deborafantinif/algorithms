def find_duplicate(nums):
    if type(nums) is not list or len(nums) < 2 or type(nums[0]) is not int:
        return False
    for number in nums:
        if number < 0:
            return False
    return False
