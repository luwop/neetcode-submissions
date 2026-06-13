type Stack struct {
	vals []rune
}

func (st *Stack) Push(val rune) {
	st.vals = append(st.vals, val)
}

func (st *Stack) Pop() (rune, bool) {
	if len(st.vals) == 0 {
		return 0, false
	}

	top := st.vals[len(st.vals)-1]
	st.vals = st.vals[:len(st.vals)-1]

	return top, true
}

func (st Stack) Empty() bool {
	return len(st.vals) == 0
}

func isValid(s string) bool {
	stack := Stack{}
	dict := map[rune]rune{')': '(', ']': '[', '}': '{'}

	for _, ch := range s {
		if ch == '(' || ch == '[' || ch == '{' {
			stack.Push(ch)
		} else {
			top, ok := stack.Pop()
			if !ok || top != dict[ch] {
				return false
			}
		}
	}

	return stack.Empty()
}