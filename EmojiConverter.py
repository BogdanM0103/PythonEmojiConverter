import sys

emojiDictionary = {
    "A": [':regional_indicator_a:'],
    "B": [':regional_indicator_b:'],
    "C": [':regional_indicator_c:'],
    "D": [':regional_indicator_d:'],
    "E": [':regional_indicator_e:'],
    "F": [':regional_indicator_f:'],
    "G": [':regional_indicator_g:'],
    "H": [':regional_indicator_h:'],
    "I": [':regional_indicator_i:'],
    "J": [':regional_indicator_j:'],
    "K": [':regional_indicator_k:'],
    "L": [':regional_indicator_l:'],
    "M": [':regional_indicator_m:'],
    "N": [':regional_indicator_n:'],
    "O": [':regional_indicator_o:'],
    "P": [':regional_indicator_p:'],
    "Q": [':regional_indicator_q:'],
    "R": [':regional_indicator_r:'],
    "S": [':regional_indicator_s:'],
    "T": [':regional_indicator_t:'],
    "U": [':regional_indicator_u:'],
    "V": [':regional_indicator_v:'],
    "W": [':regional_indicator_w:'],
    "X": [':regional_indicator_x:'],
    "Y": [':regional_indicator_y:'],
    "Z": [':regional_indicator_z:'],
    "0": [':zero:'],
    "1": [':one:'],
    "2": [':two:'],
    "3": [':three:'],
    "4": [':four:'],
    "5": [':five:'],
    "6": [':six:'],
    "7": [':seven:'],
    "8": [':eight:'],
    "9": [':nine:'],
}

def EmojiConverter(input):
    word = []
    for ch in input:
        upper_ch = ch.upper()
        if upper_ch in emojiDictionary:
            word.append(emojiDictionary[upper_ch])
    print(word)

    
EmojiConverter("Hella");
