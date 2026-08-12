if __name__ == '__main__':
    N = int(input())
    arr =[]
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        if cmd_type == 'insert':
            i = int(command[1])
            e = int(command[2])
            arr.insert(i, e)
        elif cmd_type =='print':
            print(arr)
        elif cmd_type == 'remove':
            e = int(command[1])
            arr.remove(e)
        elif cmd_type == 'append':
            e = int(command[1])
            arr.append(e)
        elif cmd_type == 'sort':
            arr.sort()
        elif cmd_type == 'pop':
            arr.pop()
        elif cmd_type == 'reverse':
            arr.reverse(