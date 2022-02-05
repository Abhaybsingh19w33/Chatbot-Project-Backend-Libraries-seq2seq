import keras.backend as K

print("Keras Backend is set tensorflow as default")
# if K.backend() == 'tensorflow':
if True:
	from .tensorflow_backend import *
	rnn = lambda *args, **kwargs: K.rnn(*args, **kwargs) + ([],)
elif K.backend() == 'theano':
	from .theano_backend import *
else:
	raise Exception(K.backend() + ' backend is not supported.')
