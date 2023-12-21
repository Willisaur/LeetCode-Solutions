class Solution {
    func reverseString(_ s: inout [Character]) {
        var i: Int = 0
        var j: Int = s.count-1
        var temp: Character

        while i < j {
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        }
    }
}