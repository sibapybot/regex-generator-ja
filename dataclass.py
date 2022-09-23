from dataclasses import dataclass
from typing import Optional, List

@dataclass
class WordDescription():
    #分解した単語
    word:Optional[str] = None
    #分解した単語の品詞、読み
    description:Optional[List[str]] = None
    #文字列の場所
    string_position:int = None 

@dataclass
class DecomposedString():
    #文章
    string:Optional[str]= None
    #MeCabで分解した単語の数
    word_quantity:Optional[WordDescription] = None 
    #文字列の長さ
    str_len:int = None 
    #単語の数
    word_len:int = None
    #一致した文字列の数
    matched_len:int = None 
    #一致した文字列
    matched_set_words:Optional[str] = None 
    #一致した単語の場所
    match_words:Optional[List[int]] = None

@dataclass
class AllText():
    #すべてのテキストの数
    str_several:int = 0
    #最大の文字列
    max_len:int = 0
    #最大の単語数
    max_word_len:int = 0
    #最小の文字列
    min_len:int = 0
    #最小の単語数
    min_word_len:int = 0




REPEAT = lambda n,m:f'{{{n}-{m}}}'
STRING = ".*"
TOP = "^"
END = "$"
