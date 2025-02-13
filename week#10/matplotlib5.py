
# using matplotlib with data

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/Users/aamtayag/Desktop/MSE/MSE803-DA/Week#10/Sample_Data_for_Activity.csv')
a = data['Normal_Distribution']
b = data['Uniform_Distribution']
c = data['Exponential_Distribution']
d = data['Poisson_Distribution']
#x=[1,2,3,4,5]
#y=[10,20,25,30,40]
#plt.hist( data['Exponential_Distribution'])
#plt.hist(data)

plt.subplot(2,2,1)
plt.plot(a)
plt.title('Normal_Distribution')
#plt.savefig('fig5.png')

plt.subplot(3, 2, 2)
plt.plot(b)
plt.title('Uniform_Distribution')


plt.subplot(3, 2, 5)
plt.plot(c)
plt.title('Exponential_Distribution')


plt.subplot(3, 2, 6)
plt.plot(d)
plt.title('Poisson_Distribution')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')



plt.show()
#plt.close()


