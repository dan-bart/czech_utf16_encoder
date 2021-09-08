import pandas as pd

class Czech_Hex_Encoder():
    def __init__(self,text):
        if(".txt" in text):
            path = text
            self.filename = path.split("\\")[-1].replace(".txt","")
            self.path = path.replace("\\"+self.filename+".txt","")
            with open(path, encoding='utf-8') as f:
                self.lines = f.readlines()
            f.close()
            self.new_file= open(self.path+"\\"+self.filename+"_utf16.txt","w+")
        else:
            self.lines = text
            self.new_file= open("new_file_encoded.txt","w+")
    def hex_encode(self):
        hex_dict = pd.DataFrame({'znak': ["Á","Č","Ď","É","Ě","Í","Ň","Ó","Ř","Š","Ť","Ú","Ů","Ý","Ž","á","č","ď","é","ě","í","ň","ó","ř","š","ť","ú","ů","ý","ž"],
                                'hex': ["\\u00C1", "\\u010C", "\\u010E", "\\u00C9", "\\u011A", "\\u00CD", "\\u0147", "\\u00D3", "\\u0158","\\u0160", "\\u0164", 
                                "\\u00DA", "\\u016E", "\\u00DD", "\\u017D", "\\u00E1", "\\u010D", "\\u010F", "\\u00E9","\\u011B", "\\u00ED", "\\u0148", "\\u00F3", 
                                "\\u0159", "\\u0161", "\\u0165", "\\u00FA", "\\u016F", "\\u00FD", "\\u017E"]}).set_index("znak")['hex'].to_dict()

        for line in self.lines:
            for znak, hex in hex_dict.items():
                line = line.replace(znak,hex)
            self.new_file.write(line)
        self.new_file.close()
            
if __name__ == "__main__":
    lines = []
    print("Input full path or txt file")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    cz_hex_encoder = Czech_Hex_Encoder(text)
    cz_hex_encoder.hex_encode()