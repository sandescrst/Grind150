def search( nums, target: int) -> int:
        l, r = 0, len(nums) -1

        while l <=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1
print(search([3,4,5,6,7,8,9], 6))