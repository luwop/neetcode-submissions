func isSubsequence(s string, t string) bool {
	x := len(s)
	y := len(t)
	if x > y || y == 0 {
		return false
	}

	if x == 0 {
		return true
	}

	pos := 0

	for indx := 0; indx < y; indx++ {
		if t[indx] == s[pos] {
			fmt.Println(t[indx], s[pos])
			pos++
		}

		if pos == x {
			return true
		}
	}

	return false
}
