class Solution {
    func reverseString(_ s: inout [Character]) {
        var i: Int = 0
        var temp: Character

        while i < s.count/2 {
            temp = s[i]
            s[i] = s[s.count-1-i]
            s[s.count-1-i] = temp
            i += 1
        }
    }
}