import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
f = open('/Users/jyothivaidyanathan/Downloads/Home_and_Kitchen_5.json', 'r',encoding='iso-8859-1')

true,false,none=0,0,0
i=0
for lines in f:
    if i!=0:
        if "\"verified\": true" in lines:
            true+=1
        elif "\"verified\": false" in lines:
            false+=1
        else:
            none+=1
    
    i+=1
print("True",true,"False",false,"None",none)
"""
#Plotting the graph
fig = plt.figure(figsize = (12, 7))
# creating the bar plot
plt.barplot(["True","False","None"], [true,false,none], color ='skyblue', 
        width = 0.4)
 
plt.xlabel("Values")
plt.ylabel("Count")

plt.title("Distribution of verified values")
plt.show()
"""

data = [true,false,none]
df = pd.DataFrame(data, columns=['values'])
x_labels=["true","false","none"]
plt.bar(x_labels,df['values'])
plt.yticks([])
for i, value in enumerate(df['values']):
    plt.text(i, value + 1, str(value), ha='center')

plt.xlabel('Verified Status')
plt.ylabel('Count')
plt.title('Verified reviews vs Count')
plt.show()