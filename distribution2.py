#set up notebook
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
untuk mengetahui perbedaan diantara setiap spesies maka di fngsikan untuk  menerapkan
coloring pada plot

"""
#path the files
path_sentosa='Visualisasi_data\iris_setosa.csv'
path_versicolor='Visualisasi_data\iris_versicolor.csv'
path_virginica='Visualisasi_data\iris_virginica.csv'
#read the files into  variabels
iris_set_data=pd.read_csv(path_sentosa,index_col='Id')
iris_ver_data=pd.read_csv(path_versicolor,index_col='Id')
iris_vir_data=pd.read_csv(path_virginica,index_col='Id')

print(iris_set_data.head(10))
# Histograms for each species
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

# Add title
plt.title("Histogram of Petal Lengths, by Species")

# Force legend to appear->cant, used show 
plt.show()




# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")
plt.show()