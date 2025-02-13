

import matplotlib.pyplot as plt
categories = ['A','B', 'C','D']
values = [3,7,1,8]
mylabels = ["A", "B", "C", "D"]
#plt.bar(categories,values, color='skyblue')
plt.pie(values, labels=mylabels)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Pie Chart Example')
plt.savefig('fig3.png')
plt.show()

