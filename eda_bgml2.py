import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
f = open('/Users/jyothivaidyanathan/Downloads/ProductwiseReviews.txt', 'r',encoding='iso-8859-1')
import seaborn as sns
true,false,none=0,0,0
i=0
hashmap={}
for lines in f:
    line=lines.split("- 	")
    product_id=line[0]
    reviews=line[1].count("%#%")
    hashmap[product_id]=hashmap.get(product_id,0)+reviews

print(max(hashmap.values()))

# Convert dictionary to list of lists
plot_list= []
for key, value in hashmap.items():
    plot_list.append([key, value])

# Create Pandas DataFrame
df = pd.DataFrame(plot_list, columns=['key', 'value'])

plt.figure(figsize=(12, 8))
# Create line plot with Seaborn
sns.lineplot(x='key', y='value', data=df)
plt.show()

"""
plt.scatter(list(hashmap.keys()),list(hashmap.values()))
plt.xticks([])
plt.xlabel('Verified Status')
plt.ylabel('Count')
plt.title('Verified reviews vs Count')
plt.show()
"""