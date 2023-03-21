a=0.125
b=0.25
n=int(input('n=',))
devrtt=40
estimatedrtt=200
samplertt=20
for i in range(n):
    estimatedrtt=(1-a)*estimatedrtt + a*samplertt
    devrtt=(1-b)*devrtt+b*abs(samplertt-estimatedrtt)
    timeoutinterval=estimatedrtt + 4*devrtt
    print('n=',i+1,end='')
    print('timeoutinterval =',timeoutinterval)


