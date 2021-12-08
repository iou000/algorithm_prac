def solution(name):
    answer = 0

    cur = 0
    next = 0

    for i in range(0,len(name)):
        if name[i] != 'A':
            name[i] = 'A'
            if(ord(name[i]) - ord('A') > 13):
                answer += 26 - ord(name[i]) - ord('A')
            else:
                answer+= ord(name[i]) - ord('A')
            cur = i

    
    return ord('J')-ord('A') + ord('N')-ord('A')+1

print(solution("JAN"))