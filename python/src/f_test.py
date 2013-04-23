import theano
theano.config.blas.dflags='-lopenblas'
x=theano.tensor.vector('x')
y=theano.tensor.vector('y')
f=theano.function(inputs=[x,y],outputs=x+y*2)
print f([1,2],[3,4])


#zhe shi wo gai de 
print" ni he bing xia wo kankan "
