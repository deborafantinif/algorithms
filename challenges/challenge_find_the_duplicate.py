def count_numbers(nums, number, report_numbers):
    for next_number in range(nums.index(number) + 1, len(nums)):
        if number == nums[next_number]:
            report_numbers[number] += 1


def find_max_repeat(dict_n):
    maxi = [0, 0]
    for key, value in dict_n.items():
        if value > maxi[1]:
            maxi = [key, value]
    return maxi


def find_duplicate(nums):
    report_numbers = {}
    if type(nums) is not list or len(nums) < 2 or type(nums[0]) is not int:
        return False
    for number in nums:
        if number < 0:
            return False
        report_numbers[number] = 1
        count_numbers(nums, number, report_numbers)
    maxi_number = find_max_repeat(report_numbers)
    return maxi_number[0] if maxi_number[1] != 1 else False
