from sys import stdin
input = stdin.readline
N, M = map(int, input().split())

sings_dict = {}


for _ in range(N):
    new_input = input().strip().split()
    num = new_input[0]
    name = new_input[1]
    code = "".join(new_input[2:])
    sings_dict[code] = name

for _ in range(M):
    get_code = input().replace(" ", "").strip()
    sings_list = []

    for code, name in sings_dict.items():
        if get_code in code and code.index(get_code) == 0:
            sings_list.append(name)
        else:
            continue
        
    if len(sings_list) == 1:
        print(sings_list[0])

    elif len(sings_list) > 1:
        print("?")

    else:
        print("!")

        
        


