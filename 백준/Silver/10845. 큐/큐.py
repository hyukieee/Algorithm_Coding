import sys
from collections import deque

input = sys.stdin.read

def main():
    data = input().splitlines()
    n = int(data[0])
    queue = deque()
    result = []

    for i in range(1, n + 1):
        command = data[i].split()

        if command[0] == "push":
            queue.append(int(command[1]))

        elif command[0] == "pop":
            if queue:
                result.append(queue.popleft())
            else:
                result.append(-1)

        elif command[0] == "size":
            result.append(len(queue))

        elif command[0] == "empty":
            result.append(1 if not queue else 0)

        elif command[0] == "front":
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)

        elif command[0] == "back":
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)

    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()
