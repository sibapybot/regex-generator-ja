import re



def regex_ja_match(text,regex):
    #半角スペースはサポート外です
    return re.match(regex,text.replace(" ",""))