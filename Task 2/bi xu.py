def inputList():
    with open('bi_xu_raw.txt', 'r') as fh:
        raw = fh.read().split('more')
    lines = []
    for i in raw:
        i = i.replace('\n', '').replace('\t', '')
        lines.append(i)