
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # return nums.sort()
        i, low, high = 0, 0, len(nums) - 1

        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1

        return nums


#  two pass O(m+n) space
# void sortColors(int A[], int n) {
#     int num0 = 0, num1 = 0, num2 = 0;

#     for(int i = 0; i < n; i++) {
#         if (A[i] == 0) ++num0;
#         else if (A[i] == 1) ++num1;
#         else if (A[i] == 2) ++num2;
#     }

#     for(int i = 0; i < num0; ++i) A[i] = 0;
#     for(int i = 0; i < num1; ++i) A[num0+i] = 1;
#     for(int i = 0; i < num2; ++i) A[num0+num1+i] = 2;
# }

# one pass in place solution
# void sortColors(int A[], int n) {
#     int n0 = -1, n1 = -1, n2 = -1;
#     for (int i = 0; i < n; ++i) {
#         if (A[i] == 0)
#         {
#             A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
#         }
#         else if (A[i] == 1)
#         {
#             A[++n2] = 2; A[++n1] = 1;
#         }
#         else if (A[i] == 2)
#         {
#             A[++n2] = 2;
#         }
#     }
# }
