#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    first_char = sentence[0]
    if not sentence:
        return (len_sen, None)
    else:
        return (len_sen, first_char)
