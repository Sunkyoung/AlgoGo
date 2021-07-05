# new code
def solution(phone_book):
    phone_book.sort() # 효율성 8,9번 통과의 핵심
    min = len(phone_book[0])
    prefix = []
    for i,p in enumerate(phone_book):
        if min >= len(p):
            prefix.append(phone_book.pop(i))
    for i in range(len(prefix)):
        for p in phone_book:
            if p.startswith(prefix[i]) :
                return False
    return True
    
# old code
def solution(phone_book):
    answer = False
    min_length = 0
    min_content = phone_book[0]
    for i in phone_book:
        if min_length > len(i):
            min_length = len(i)
            min_content = i
    for i in phone_book :
        if i[:min_length] == min_content :
            answer = False
        else:
            answer = True
    return answer