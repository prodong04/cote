def expand_star(output: list) -> list:
    # 가로축에 별 추가
    for x in range(len(output)):
        output[x].insert(0, " ")
        output[x].insert(0, "*")
        output[x].append(" ")
        output[x].append("*")
    # 세로축에 별 추가
    output.insert(0, [" " for _ in range(len(output[0]))])
    output.insert(0, ["*" for _ in range(len(output[0]))])
    output.append([" " for _ in range(len(output[0]))]) 
    output.append(["*" for _ in range(len(output[0]))])
    output[1][0] = "*"
    output[2][-2] = "*"
    output[-2][0] = "*"
    output[-2][-1] = "*"
    return output

def star_printing(x: int) -> list:
    if x == 1:
        return [['*']]
    elif x == 2:
        return [
            ["*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " "],
            ["*", " ", "*", "*", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*"],
        ]
    elif x >= 3:
        expanded_star = expand_star(star_printing(x - 1))
        return expanded_star

def main():
    n = int(input())
    output = star_printing(n)
    result = "\n".join("".join(row).rstrip() for row in output)
    print(result)

if __name__ == "__main__":
    main()
