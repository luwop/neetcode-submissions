func twoSum(nums []int, target int) []int {
    comp := map[int]int{}

	for indx, val := range nums {

		if _, found := comp[val]; found {
			return []int{comp[val], indx}
		}
		comp[target - val] = indx
	}
	
	return []int{-1, -1}
}
