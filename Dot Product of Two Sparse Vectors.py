# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.vec[i] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for index in self.vec:
            if vec.vec.get(index, 0):
                res += self.vec[index] * vec.vec[index]
        return res

    # Return the dotProduct of two vectors if only one vector was sparse
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        if len(self.vec) > len(vec.vec):
            v1, v2 = vec.vec, self.vec
        else:
            v1, v2 = self.vec, vec.vec

        for index in v1:
            if v2.get(index, 0):
                res += v1[index] * v2[index]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)