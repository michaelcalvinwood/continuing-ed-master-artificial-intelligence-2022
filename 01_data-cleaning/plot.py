import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("../data/bigmart.csv")
print(data.head())

#Checking for Univariate outliers using boxplot

plt.rcParams['figure.figsize']=(16,4)

plt.subplot(1,4,1)
sns.boxplot(data['Item_Weight'])

plt.subplot(1,4,2)
sns.boxplot(data['Item_Visibility'])

plt.subplot(1,4,3)
sns.boxplot(data['Item_MRP'])

plt.subplot(1,4,4)
sns.boxplot(data['Item_Outlet_Sales'])

plt.suptitle("Checking for Univariate Outliers")
plt.show()