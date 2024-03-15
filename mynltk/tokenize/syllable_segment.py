#-*- coding:utf-8 -*-
"""
Last updated: 21 July 2016
Written by Ye Kyaw Thu, Visiting Researcher, Waseda University
Homepage:https://sites.google.com/site/yekyawthunlp/

Reference of Myanmar Unicode: http://unicode.org/charts/PDF/U1000.pdf
"""
import re

myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
aThat = r'်'

# global delimiter

#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
break_pattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)


# def syllable(line):
#     return break_pattern.sub(delimiter + r"\1", line)


def segment(text: str) -> list[str]:
    if not text or not isinstance(text, str):
        return []
    
    segemented_text = break_pattern.sub(" " + r"\1", text)
    # remove the first space in front of the first segmented syllable
    segemented_text = segemented_text.strip()

    return segemented_text.split(" ")
    

    
    