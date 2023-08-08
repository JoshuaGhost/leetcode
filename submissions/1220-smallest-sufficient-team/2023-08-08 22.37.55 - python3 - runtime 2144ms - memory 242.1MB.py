class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        self.dp = {}
        bit_p = []
        for p in people:
            bit_p.append(0)
            for s in p:
                bit_p[-1] |= 1 << req_skills.index(s)
        ls = len(req_skills)
        np = len(people)

        def search(i, mask) -> List[int]:
            if self.dp.get((i, mask), None) is not None:
                return self.dp[(i, mask)]
            if mask == (1 << ls) - 1:
                return []

            if i == np:
                return [0] * 1000

            if bit_p[i] | mask == mask:
                self.dp[(i, mask)] = search(i + 1, mask)
                return self.dp[(i, mask)]

            self.dp[(i, mask)] = min(
                search(i + 1, mask), [i] + search(i + 1, mask | bit_p[i]), key=len
            )
            return self.dp[(i, mask)]

        return search(0, 0)