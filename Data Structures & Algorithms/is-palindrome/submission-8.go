func isPalindrome(s string) bool {
	i, j := 0, len(s) - 1
	runes := []rune(s)

	for i < j {

		if !unicode.IsDigit(runes[i]) && !unicode.IsLetter(runes[i]) {
			i++
			continue
		}

		if !unicode.IsDigit(runes[j]) && !unicode.IsLetter(runes[j]) {
			j--
			continue
		}

		if unicode.ToLower(runes[i]) != unicode.ToLower(runes[j]) {
			return false
		}
		i++
		j--
	}


	return true
}
