class Solution:
    dp_best_score_1 = {(): (0, 0)}
    dp_best_score_2 = {(): (0, 0)}

    def search_best_for_player_two(
        self,
        nums,
    ):
        key = tuple(nums)
        if key in self.dp_best_score_2:
            return self.dp_best_score_2[key]
        if len(nums) == 1:
            self.dp_best_score_2[key] = 0, nums[0]
            return 0, nums[0]
        scores = [
            self.search_best_for_player_one(nums[1:]),
            self.search_best_for_player_one(nums[:-1]),
        ]
        scores = [
            [scores[0][0], nums[0] + scores[0][1]],
            [scores[1][0], nums[-1] + scores[1][1]],
        ]
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        self.dp_best_score_2[key] = scores[0]
        return self.dp_best_score_2[key]

    def search_best_for_player_one(self, nums):
        key = tuple(nums)
        if key in self.dp_best_score_1:
            return self.dp_best_score_1[key]
        if len(nums) == 1:
            self.dp_best_score_1[key] = nums[0], 0
            return nums[0], 0
        scores = [
            self.search_best_for_player_two(nums[1:]),
            self.search_best_for_player_two(nums[:-1]),
        ]
        scores = [
            [nums[0] + scores[0][0], scores[0][1]],
            [nums[-1] + scores[1][0], scores[1][1]],
        ]
        scores = sorted(scores, key=lambda x: x[0], reverse=True)
        self.dp_best_score_1[key] = scores[0]
        return self.dp_best_score_1[key]

    def PredictTheWinner(self, nums: List[int]) -> bool:
        score1, score2 = self.search_best_for_player_one(nums)
        return score1 >= score2