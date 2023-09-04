impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut ret: String = "".to_string();
        for (a, b) in word1.chars().zip(word2.chars()) {
            ret.push(a);
            ret.push(b);
        };
        if word1.len() < word2.len(){
            ret.extend(word2[word1.len()..].chars());
        } else {
            ret.extend(word1[word2.len()..].chars());
        }
        ret
    }
}