class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int ret = 0;
        int n = mat.size();
        for (int i = 0; i < n; i++) {
            ret += mat[i][i] + mat[i][n-i-1];
        }
        if (n % 2 == 1) {
            ret -= mat[int(n / 2)][int(n / 2)];
        }
        return ret;
    }
};