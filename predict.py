import args
import chainer.links as L
import chainer
import data_handler as dh
import model as cntn
import numpy as np
from chainer import Chain, optimizers, serializers, Variable
from itertools import izip
from util import key2value

###load arguments
arg = args.process_command()
testing_url = arg.predict
doc_len = arg.dlen
word_len = arg.wlen
word_dim = arg.wdim
n_units = arg.hdim
n_label = arg.label
filter_length = arg.flen
filter_width = word_len
filter_height = word_dim
output_channel = arg.channel
batch_size = arg.batch
n_epoch = arg.epoch
model_url = arg.model

###load dataset
testing = open(testing_url).readlines()[0]
dataset = dh.load_corpus(testing, doc_len, word_len )

x = dataset['source']
keyword = dataset['keyword']
org_word = dataset['org']

###load model
print '###\tload model\t:{}'.format( model_url )
print '###\tpredicted txt\t:{}'.format( testing_url )

model = cntn.CNTN(output_channel, filter_length, filter_width, filter_height, n_units, n_label)
cf = L.Classifier(model)
optimizer = optimizers.Adam()
optimizer.setup(cf)
serializers.load_npz(model_url, model)


###predict
print '###\tpredict'

learned_y = []

slen = lambda a, b, c: c if a-b > c else a-b

N = len(keyword)
for i in xrange(0,  N, batch_size ):
	_ = slen(N, i, batch_size)
 
	x = chainer.Variable(np.asarray(x).astype(np.float32)).reshape(-1, 1, doc_len, word_len, word_dim)
	w = chainer.Variable(np.asarray(keyword[i:i+_]).astype(np.float32)).reshape(-1, 1, doc_len, word_len, word_dim)
	y = model(x, w)	
	learned_y.extend(y.data)

###write file	
print '###\toutput Keywords\t:{}'.format(testing_url+'.key')
predicted = [np.argmax(learned_y[i]) for i in xrange(len(learned_y))]
with open( testing_url+'.key', 'wb' ) as f:
	for i in izip(predicted, org_word):
		if i[0] == 1:
			f.write( '{}\n'.format(i[1]) )
