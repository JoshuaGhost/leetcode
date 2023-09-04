impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
       let mut ret: u8 = 0;
       for c in s.chars() {
           ret ^= c as u8;
       }
       for c in t.chars() {
           ret ^= c as u8;
       }
       ret as char
    }
}