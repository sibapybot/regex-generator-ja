from textwrap import fill
from typing import Optional, List
from proces import (disassembly_text, 
                    max_word, 
                    pading, 
                    left_sift, 
                    comparison_save_patten,
                    comparison_patten,
                    word_len_sum)
from dataclass import DecomposedString, WordDescription, AllText 
from dataclass import REPEAT, STRING, TOP, END
import itertools


def run(texts:List):
    patten:str = ""
    all_pattern_list:list[str] = []
    text_data:List[DecomposedString] = []
    
    for text in texts:
        text_data.append(disassembly_text(text=text))
    
    all_data = AllText()
    all_data.max_len = max(map(len, texts))
    all_data.min_len = min(map(len, texts))
    word_lens = sorted([teda.word_len for teda in text_data])
    all_data.max_len = word_lens[-1]
    all_data.min_len = word_lens[0]
    all_data.str_several = len(texts)

    for two_node in itertools.combinations(text_data,2):
        all_pattern:str = "" 
        save_patten_a:list[WordDescription] = []
        save_patten_b:list[WordDescription] = []

        maxword = max_word(two_node=two_node)
        a:list[WordDescription] = pading(two_node[0].word_quantity,maxword)
        b:list[WordDescription] = pading(two_node[1].word_quantity,maxword)

        for z in range(maxword):
            for y in range(maxword):
                leftsift_b = left_sift(b,y)

                content_chack = a[z].word==leftsift_b[z].word and a[z].description==leftsift_b[z].description
                duplicate_check = a[z] not in save_patten_a and leftsift_b[z] not in save_patten_b 
                if content_chack and duplicate_check:
                    save_patten_a.append(a[z])
                    save_patten_b.append(leftsift_b[z])

        save_patten_a.sort(key=lambda x:x.string_position)
        save_patten_b.sort(key=lambda x:x.string_position)
        #print("".join([f"{str(i.word)}" for i in save_patten_b]))
        #print("".join([f"{str(i.string_position)}," for i in save_patten_a]))
        com_patten,filler=comparison_patten(save_patten_a,save_patten_b,two_node)

        all_pattern += TOP

        for z,com in enumerate(com_patten):
            all_pattern += "".join([f"{str(i.word)}" for i in com])
            if filler[z]:
                all_pattern += f".{{{filler[z][0]},{filler[z][1]}}}"

        all_pattern += STRING
        all_pattern +=  END

        all_pattern_list.append(all_pattern)
    
    for i in range(len(all_pattern_list)):
        if len(all_pattern_list)-i == 1:
            patten += all_pattern_list[i]
        else:
            patten += all_pattern_list[i]+"|"
    return patten


        


if __name__ == "__main__":
    texts = ["testだあああああああ！！！agfnl545sad testだあああああああ！！！arf testだあああああああ！！！","testだあああああああ！！！testだあああああああ！！！testだあああああああ！！！","testだあああああああ！！！a testだあああああああ！！！arf  adfs testだあああああああ！！！"]
    print(run(texts=texts))