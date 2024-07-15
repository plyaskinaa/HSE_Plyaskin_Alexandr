def is_monotonic(nums):

    if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
        return True
    if all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)):
        return True
    return False

if __name__ == "__main__":
    user_input = input("Введите последовательность чисел, разделенных пробелом: ")
    nums = list(map(int, user_input.split()))
    result = is_monotonic(nums)
    print(f"Последовательность {nums} является монотонной: {result}")