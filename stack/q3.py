class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_time = [0] * n
        time = 0
        is_time_proceed = True
        end_time = int(logs[-1].split(":")[2])

        while time <= end_time:
            head = logs[0]
            head_id = head.split(":")[0]
            head_event = head.split(":")[1]
            head_time = int(head.split(":")[2])

            if time == head_time and head_event == "start":
                stack.append(int(head_id))
                if is_time_proceed:
                    exclusive_time[stack[-1]] += 1
                logs.pop(0)
            elif time == head_time and head_event == "end":
                if is_time_proceed:
                    exclusive_time[stack[-1]] += 1
                stack.pop()
                logs.pop(0)
            else:
                if is_time_proceed:
                    exclusive_time[stack[-1]] += 1

            if len(logs) != 0:
                next_time = int(logs[0].split(":")[2])
                if next_time > time:
                    is_time_proceed = True
                    time += 1
                else:
                    is_time_proceed = False
            else:
                is_time_proceed = True
                time += 1

        return exclusive_time


if __name__ == "__main__":
    n = 2
    # n = 1
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    # logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    # logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    # logs = ["0:start:0", "0:end:100000000"]
    print(logs, "\n")
    solution = Solution()
    result = solution.exclusiveTime(n, logs)
    print(result)
