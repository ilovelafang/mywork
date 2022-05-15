
def replace_space(data: str) -> str:
    if not data:
        return ''
    res = ''
    for i in data:
        # print(i)
        if i == ' ':
            res += '%20'
        else:
            res += i
    return res


if __name__ == '__main__':
    print('start')
    data = 'we are happy'
    r = replace_space(data)
    print(r)
    c = data.replace(' ', '%20')
    print(c)
