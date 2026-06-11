func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	freq := make(map[rune]int, len(s))

	for _, ch := range s {
		freq[ch] = freq[ch] + 1
	} 

	for _, ch := range t {
		freq[ch] = freq[ch] - 1
		if freq[ch] < 0 {
			return false
		}
	} 

	return true
}
