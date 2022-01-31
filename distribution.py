"""
digunakan untuk mencari sebuah distribusi pada nilai dalam data frame yang dapat di manifestasikan ke dalam
histogram,kde plot, kde plot 2d,
"""
#setup notebook
import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns
#load the data
file_path="Visualisasi_data\iris.csv"
data_iris=pd.read_csv(file_path,index_col='Id')
#examine data
print(data_iris.head(10))
"""
data pada tumbuhuan iris terdapat sebuah 150 tanaman yang mana
terdiri atas 50 tanamanan di setiap spesies
"""
#histogram
plt.figure(figsize=(10,6))
sns.distplot(a=data_iris['Petal Length (cm)'],kde=False)
plt.show()

#kde plot
sns.kdeplot(data=data_iris['Petal Length (cm)'],shade=True)
#shade=colors the area below the curve
#data=data yang ditunjukan
plt.show()
"""
desinity mengetahui kepadatan penyebaran dari setiap value yang ada pada data frame
"""
#2d kde plot
sns.jointplot(x=data_iris['Petal Length (cm)'], y=data_iris['Sepal Length (cm)'],kind='kde')
plt.show()
