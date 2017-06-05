import xml.parsers.expat

class Reader:
    def __init__(self):
        self._parser = xml.parsers.expat.ParserCreate()
        self._parser.StartElementHandler = self.start_element
        self._parser.EndElementHandler = self.end_element
    
    def start_element(self, name, attr):
        #self._info.update(attr)
        if name == 'token':
                 attr.pop('id')
                 self._info = attr
        if name == 'l':
                 attr.pop('id')
                
                 self._info.update(attr)
                # print(attr['t'])
        if name == 'g' and attr['v'][0].isupper() and attr['v'][1].isupper() and attr['v'][2].isupper():
                 self._info.update(attr)
        
    def end_element(self, name):
        if name == 'tokens':
            self._sentences.append(self._sentence)
            self._sentence = []
        elif name == 'token':
            text = self._info.pop('text')
            
            self._sentence.append((text,self._info))

    def read(self, filename):
        f = open(filename,encoding = "utf-8")
        content = f.read()
        f.close()
        
        self._sentences = []
        self._sentence = []
        self._cdata = ''
        self._info = {}
        
        self._parser.Parse(content)        
        
        return self._sentences
  
#tmp = Reader()
#o = open('x.txt', 'w')
#print(tmp.read('new.xml'), file = o)
#o.close()

