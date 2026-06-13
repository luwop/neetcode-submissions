func replaceElements(arr []int) []int {
    maxSoFar := -1

    for i := len(arr) - 1; i >= 0; i-- {
        current := arr[i]
        arr[i] = maxSoFar

        if current > maxSoFar {
            maxSoFar = current
        }
    }

    return arr
}