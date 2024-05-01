import re

#讀取檔案，並回傳 raw list
def inputList():
    with open('bi_xu_raw.txt', 'r') as fh:
        #刪去整個txt檔中的\n\t，並以'more'區分
        raw = fh.read().replace('\n', '').replace('\t', '').split('more')
    return raw
    
#輸入並處理raw list、回傳processed list
def process(raw):
    processed = []
    for line in raw:
        pattern = '，|。|！|？|；'
        #把每一行依照標點符號(pattern)分成段（類似子句）
        parts = re.split(pattern, line,)
        for part in parts:
            #選取含有"必須"的片段，並append到processed lsit
            if "必須" in part:
                processed.append(part)
    #轉成集合已刪除重複句，再轉回list
    processed = list(set(processed))
    return processed

def process2(raw):
    processed = []
    for line in raw:
        if "必須" in line:
            p = '，|。|！|？|；'
            pattern = f"([^{p}]*必須[^{p}]*)"
            matches = re.findall(pattern, line)
            for match in matches:
                processed.append(match)
    processed = list(set(processed))
    return processed
    
#呈現processed list
def show(processed):
    for s in processed:
        print(f'{s}')

#將processed list輸出txt檔
def save(processed):
    with open('bi_xu_processed.txt', 'w') as fh:
        sentence = [f'{s}\n' for s in processed]
        fh.writelines(sentence)
        
                


raw_list = inputList()
processed_list = process(raw_list)
show(processed_list)
save(processed_list)