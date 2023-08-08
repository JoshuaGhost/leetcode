class Solution:
    def search_smallest_team(self) -> int:
        team = {0: (0, 0)}
        new_team = deepcopy(team)
        for i, b_person_skill in enumerate(self.people):
            for b_team_skill, (n_people, b_team) in team.items():
                b_new_team_skill = b_team_skill | b_person_skill
                if b_new_team_skill in new_team:
                    if new_team[b_new_team_skill][0] > n_people + 1:
                        new_team[b_new_team_skill] = (n_people + 1, b_team | (1 << i))
                else:
                    new_team[b_new_team_skill] = (n_people + 1, b_team | (1 << i))
            team = deepcopy(new_team)
        return team[self.req_skills][1]

    def convert_bin_to_list(self, bin_num: int) -> List[int]:
        ret = []
        for i in range(len(self.people)):
            if bin_num & 1 << i != 0:
                ret.append(i)
        return ret

    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        self.bitmap = {}
        self.dp = {}
        self.bitmap = {skill: 1 << i for i, skill in enumerate(req_skills)}
        self.req_skills = 0
        for skill in req_skills:
            self.req_skills |= self.bitmap[skill]
        self.people = []
        for person in people:
            self.people.append(0)
            for skill in person:
                self.people[-1] |= self.bitmap[skill]
        return self.convert_bin_to_list(self.search_smallest_team())