import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key=lambda x: x[1])
        end_points = [0]
        max_values = [[0] + [float("-inf")] * k]
        for st, ed, v in events:
            p_before = bisect.bisect_left(end_points, st)
            if p_before == len(end_points):
                end_points.append(ed)
                new_values = [0]
                for current_k in range(1, k + 1):
                    new_values.append(
                        max(
                            max_values[-1][current_k], max_values[-1][current_k - 1] + v
                        )
                    )
                max_values.append(new_values)
                continue
            elif end_points[p_before] >= st:
                p_before -= 1
            if ed == end_points[-1]:
                new_values = [0]
                for current_k in range(1, k + 1):
                    new_values.append(
                        max(
                            max_values[p_before][current_k],
                            max_values[p_before][current_k - 1] + v,
                            max_values[-1][current_k],
                        )
                    )
                max_values[-1] = new_values
            else:
                end_points.append(ed)
                new_values = [0]
                for current_k in range(1, k + 1):
                    new_values.append(
                        max(
                            max_values[p_before][current_k],
                            max_values[p_before][current_k - 1] + v,
                            max_values[-1][current_k],
                        )
                    )
                max_values.append(new_values)
        return max(max_values[-1])