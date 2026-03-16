class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        pointer = 0
        current_time = 0
        stack = []
        exclusive_time = [0] * n

        # logsを一つずつ処理していく。
        while pointer < len(logs) - 1:
            current_arr = logs[pointer].split(":")
            next_arr = logs[pointer + 1].split(":")

            current_time = int(current_arr[2])
            current_event = current_arr[1]

            # 今のlogがstartであればstackにPush、endであればPopする
            # 追加する値は関数のID
            if current_event == "start":
                stack.append(int(current_arr[0]))
            else:
                stack.pop()

            next_time = int(next_arr[2])
            time_proceeds = next_time - current_time

            next_event = next_arr[1]
            # 今と次のイベントによってexclusive timeを変化させる値を調整する。
            # start -> endの場合時間差に１を足す
            if current_event == "start" and next_event == "end":
                # stackのトップのIDをインデックスとしてexclusive_timeに値を足す
                exclusive_time[stack[-1]] += time_proceeds + 1
            # end -> startの場合時間差から１を引く
            elif current_event == "end" and next_event == "start":
                # stackの要素が1つのときにendになるとstackが空になってしまうので確認
                if len(stack) != 0:
                    exclusive_time[stack[-1]] += time_proceeds - 1
            else:
                exclusive_time[stack[-1]] += time_proceeds

            pointer += 1

        return exclusive_time


if __name__ == "__main__":
    n = 3
    # n = 2
    # n = 1
    # logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    # logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    # logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    # logs = ["0:start:0", "0:end:100000000"]
    # logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]
    logs = ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"]
    print(logs, "\n")
    solution = Solution()
    result = solution.exclusiveTime(n, logs)
    print(result)
