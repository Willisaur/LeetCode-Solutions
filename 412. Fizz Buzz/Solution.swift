class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var fb = [String]()
        for i in 1...n {
            var out = ""
            if i % 3 == 0 {
                out += "Fizz"
            }
            if i % 5 == 0 {
                out += "Buzz"
            }
            if out == "" {
                fb.append("\(i)")
            } else {
                fb.append(out)
            }
        }
        return fb
    }
}