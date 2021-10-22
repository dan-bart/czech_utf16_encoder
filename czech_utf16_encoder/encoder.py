import pandas as pd
SIGN_DICT = pd.DataFrame({'znak': ["Á","Č","Ď","É","Ě","Í","Ň","Ó","Ř","Š","Ť","Ú","Ů","Ý","Ž","á","č","ď","é","ě","í","ň","ó","ř","š","ť","ú","ů","ý","ž"],
                        'hex': ["\\u00C1", "\\u010C", "\\u010E", "\\u00C9", "\\u011A", "\\u00CD", "\\u0147", "\\u00D3", "\\u0158","\\u0160", "\\u0164", 
                        "\\u00DA", "\\u016E", "\\u00DD", "\\u017D", "\\u00E1", "\\u010D", "\\u010F", "\\u00E9","\\u011B", "\\u00ED", "\\u0148", "\\u00F3", 
                        "\\u0159", "\\u0161", "\\u0165", "\\u00FA", "\\u016F", "\\u00FD", "\\u017E"]}).set_index("znak")['hex'].to_dict()
class Czech_Hex_Encoder():
    def __init__(self):
        pass
    def hex_encode(self,text):
        lines = text.splitlines()
        res = []
        for line in lines:
            for znak, hex in SIGN_DICT.items():
                line = line.replace(znak,hex)
            res.append(line)
        res = ("\n").join(res)
        return res
            
if __name__ == "__main__":
    text = input()
    cz_hex_encoder = Czech_Hex_Encoder(text)
    res = cz_hex_encoder.hex_encode()