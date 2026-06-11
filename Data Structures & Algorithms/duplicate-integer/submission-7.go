func hasDuplicate(nums []int) bool {
    set := map[int]bool{}

	for _, num := range nums {
		
		if set[num] {
			return true
		}
		set[num] = true
	}

	return false
}
