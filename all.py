L = ["私（わたし）がリンゴを食べます。", "彼（かれ）が本を読みます。", "私（わたし）が友達を見ます。", "彼女（かのじょ）が花を買います。", "私（わたし）が犬を飼います。", "田中さんが車を運転します。", "あなたが手紙を書きます。", "子供がお菓子を食べます。", "あなたが問題を解決します。", "友達がプレゼントを持ってきます。", "彼が日本語を話します。", "先生が質問に答えます。", "私が夕食を作ります。", "彼女がピアノを弾きます。", "あなたが助けを求めます。", "子供が遊びます。 ", "先生が新しい言葉を教えます。", "私がお茶を飲みます。", "彼がボールを投げます。"]

def extract_subj(sentence):
    sentence = sentence.replace("ます。", "")
    sm = sentence.index('が')
    subj = sentence[0:sm]
    return subj

def extract_v(sentence):  
    sentence = sentence.replace("ます。", "")
    sm = sentence.index('が')
    if 'を' in sentence:
        om = sentence.index('を')
        verb = sentence[om+1:]
    elif 'に' in sentence:
        om = sentence.index('に')
        verb = sentence[om+1:]
    else:
        verb = sentence[sm+1:]
    return verb

def extract_obj(sentence):  
    sentence = sentence.replace("ます。", "")
    sm = sentence.index('が')
    if 'を' in sentence:
        om = sentence.index('を')
        obj = sentence[sm+1:om]
    elif 'に' in sentence:
        om = sentence.index('に')
        obj = sentence[sm+1:om]
    else:
       obj = "No object"
    return obj
    

for sentence in L:
    print(f"{sentence}\nsubject:{extract_subj(sentence)}\nobject:{extract_obj(sentence)}\nverb:{extract_v(sentence)}\n")     