class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        s = s.toLowerCase().split("").sort().join("")
        t = t.toLowerCase().split("").sort().join("")
        console.log(s)
        console.log(t)

        return s === t;
    }
}
