class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hashset = new Set();

        for (let i = 0; i < nums.length; i += 1) {
            const value = nums[i];
            if (hashset.has(value)) return true;

            hashset.add(value)
        }

        return false;
    }

}
