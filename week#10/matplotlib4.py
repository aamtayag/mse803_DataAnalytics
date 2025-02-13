

import matplotlib.pyplot as plt
categories = ['A','B', 'C','D']
values = [3,7,1,8]
mylabels = ['A', 'B', 'C', 'D']
#plt.bar(categories,values, color='skyblue')
plt.scatter( values,categories)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Scatter Chart Example')
plt.savefig('fig4.png')
plt.show()

