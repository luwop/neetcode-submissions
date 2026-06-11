func getConcatenation(nums []int) []int {
    ans := make([]int, len(nums)*2)
    fmt.Println(ans)

    copy(ans, nums)
    fmt.Println(ans)

    copy(ans[len(nums):], nums)
    fmt.Println(ans)

    return ans
}