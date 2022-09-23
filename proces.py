import MeCab
from typing import Optional, List
from dataclass import WordDescription, DecomposedString


tagger = MeCab.Tagger("-Ochasen")

def disassembly_text(text:str) -> DecomposedString:
    """
    textをDecomposedStringに変換する関数。
    """
    global tagger
    node = tagger.parseToNode(text)

    nodet,s=[],0
    while node:
        nodes = WordDescription()
        nodes.word = node.surface
        nodes.description = node.feature.split(",")
        nodes.string_position = s
        nodet.append(nodes)

        node = node.next
        s+=1
    nodet = list(nodet)[1:-1]

    disassembly_text = DecomposedString()
    disassembly_text.str_len = len(text)
    disassembly_text.word_quantity = nodet
    disassembly_text.word_len = len(nodet)
    disassembly_text.string = text
    return disassembly_text

def max_word(two_node):
    return max([two_node[0].word_len,two_node[1].word_len])

def pading(node,max):
    #リストを同じ長さに揃える
    return node + [WordDescription()]*(max-len(node))

def left_sift(arr:List[WordDescription],n:int):
    #右ずらしをしていく
    return arr[n:] + arr[:n]

def comparison_save_patten(save_patten:list[WordDescription],all_patten:list[WordDescription]):
    position = save_patten[0].string_position
    comparison_save_patten:list = [[save_patten[0]]]
    filler:list = []
    for worddesc in save_patten[1:]:
        if worddesc.string_position == position+1:
            comparison_save_patten[-1].append(worddesc)
            position += 1
        else :
            filler_tmp:list = []
            for i in range(worddesc.string_position-position):
                filler_tmp.append(len(all_patten[i].word))
            filler.append(sum(filler_tmp))

            comparison_save_patten.append([worddesc])
            position = worddesc.string_position

    filler.append(0)
    return comparison_save_patten, filler

def comparison_patten(
                     patten_a:list[WordDescription],
                     patten_b:list[WordDescription],
                     two_node:list[list[DecomposedString]]
                     ):
    all_patten_a:list[WordDescription] = two_node[0].word_quantity
    all_patten_b:list[WordDescription] = two_node[1].word_quantity
    comparison_patten:list[WordDescription] = [[]]
    comparison_patten_a:list[WordDescription] = [[]]
    comparison_patten_b:list[WordDescription] = [[]]
    filler:list = []
    patten_number_a:int = 0
    patten_number_b:int = 0

    def position_len(patten_number,string_position,all_patten):
        string_len:int = 0
        for i in range(string_position-patten_number-1):
            string_len += len(all_patten[patten_number+i].word)
        return string_len


    for i in range(len(patten_a)):
        past_position_a = patten_a[i].string_position == patten_number_a+1
        past_position_b = patten_b[i].string_position == patten_number_b+1
        if past_position_a and past_position_b:

            comparison_patten[-1].append(patten_a[i])
            comparison_patten_a[-1].append(patten_a[i])
            comparison_patten_b[-1].append(patten_b[i])
            patten_number_a += 1
            patten_number_b += 1

        else:
            comparison_patten.append([patten_a[i]])
            comparison_patten_a.append([patten_a[i]])
            comparison_patten_b.append([patten_b[i]])
            #print(patten_a[i].string_position -patten_number_a)
            len_a = position_len(patten_number_a,patten_a[i].string_position,all_patten_a)
            len_b = position_len(patten_number_b,patten_b[i].string_position,all_patten_b)
            filler.append(sorted([len_a,len_b]))
            patten_number_a = patten_a[i].string_position 
            patten_number_b = patten_b[i].string_position 
    filler.append("")
            
    return comparison_patten,filler



    






def word_len_sum(arr:list[WordDescription],filler):
    return sum([len(arr[int(i)].word) for i in filler])


        