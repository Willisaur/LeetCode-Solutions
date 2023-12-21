class Solution {
    func reverseString(_ s: inout [Character]) {
        for i in 0..<s.count/2 {
            var temp = s[i]
            s[i] = s[s.count-1-i]
            s[s.count-1-i] = temp
        }
    }
}