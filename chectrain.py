import re
import chec
import svm_tag
import sys

sentences = []
sentences.extend(chec.Reader().read('new1.xml'))

#o = open('test.txt', 'w')
#print(chec.Reader().read('new.xml'), file = o)
#o.close()
#sentences.extend(rnc.Reader().read('tmp/media2.xml'))
#sentences.extend(rnc.Reader().read('tmp/media3.xml'))

re_pos = re.compile('([\w-]+)'.format('|'.join(svm_tag.tagset)))
print(re_pos)
tagger = svm_tag.Tagger()

#print('|'.join(svm_tag.tagset))

sentence_labels = []
sentence_words = []
#o = open('sentence1t.txt', 'w')
#print(sentences[0], file = o)
#o.close()
for sentence in sentences:
    labels = []
    words = []
    for word in sentence:
        gr = word[1]['v']
        print(gr)
        m = re_pos.match(gr)
        if not m:
            print(gr, file = sys.stderr)

        pos = m.group(1)

        label = tagger.get_label_id(pos)
        #if not label:
         #   print(gr, file = sys.stderr)

        labels.append(label)

        body = word[0]
        words.append(body)

    sentence_labels.append(labels)
    sentence_words.append(words)
#tagger.train(sentence_words, sentence_labels, True)
#print('Начал')
#tagger.train(sentence_words, sentence_labels)
#tagger.save('tmp/svm.model', 'tmp/ids.pickle')
#print('Закончил')

o = open('labels.txt', 'w')
print(sentence_labels, file = o)
o.close()

o = open('words.txt', 'w')
print(sentence_words, file = o)
o.close()