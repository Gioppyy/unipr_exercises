def all_below(nums: list, limit: int):
    if len(nums) == 0:
        return True

    head = nums[0]
    tail = nums[1::]
    if head > limit:
        return False

    return all_below(tail, limit)

def main():
    print(all_below([4, 5, 6, 7, 8], 10))

if __name__ == "__main__":
    main()
