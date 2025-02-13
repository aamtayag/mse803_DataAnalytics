
# using matplotlib with data

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/Users/aamtayag/Desktop/MSE/MSE803-DA/Week#10/Sample_Data_for_Activity.csv')
#x=[1,2,3,4,5]
#y=[10,20,25,30,40]
#plt.hist( data['Exponential_Distribution'])
plt.hist( data)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Using Histogram')
plt.savefig('fig5.png')
plt.show()

#plt.close()


# I believe the best plot type to use here is a Histogram
