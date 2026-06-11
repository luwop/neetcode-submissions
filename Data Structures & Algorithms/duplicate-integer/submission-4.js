class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashset = new Set(nums);

        return hashset.size !== nums.length;
    }
}
