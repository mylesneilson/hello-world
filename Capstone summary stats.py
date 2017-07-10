import pandas as pd
import matplotlib.pyplot as plt

#plt.style.use('ggplot')

path ="C:\\Users\\Myles Neilson\\Downloads\\Capstone Project\\train_labels.csv" 
tl = pd.read_csv(path) 
print(tl.s)
#print(df.head())

#print(df.describe())
#
#print(df.median())

#
#fig = plt.figure(figsize=(8,6))
#ax = fig.gca()
#trainlabels['repayment_rate'].plot.hist(ax = ax)
#ax.set_title('Histogram of Repayment Rates')
#ax.set_xlabel('Repayment Rate')
#ax.set_ylabel('Frequency')

#
#plt.show()


path ="C:\\Users\\Myles Neilson\\Downloads\\Capstone Project\\train_values.csv" 
tv = pd.read_csv(path) 
print(tv.shape)

df = pd.merge(tl,tv,how='inner',on='row_id')
print(df.shape)

#print(df.columns)

fig = plt.figure(figsize=(6,6))
ax = fig.gca()
df.plot(kind='scatter',x='admissions__sat_scores_average_overall',y='repayment_rate',ax = ax)
ax.set_title('Scatter plot of Repayment Rates v SAT')
ax.set_xlabel('sat_scores_average_overall')
ax.set_ylabel('Repayment Rate')

fig = plt.figure(figsize=(6,6))
ax = fig.gca()
df.plot(kind='scatter',x='student__demographics_median_family_income',y='repayment_rate',ax = ax)
ax.set_title('Scatter plot of Repayment Rates v median_family_income')
ax.set_xlabel('median_family_income')
ax.set_ylabel('Repayment Rate')


#print(df['repayment_rate'].median.groupby('school__region_id'))
print(df.groupby(['school__region_id']).agg(['median']))

print(df[['repayment_rate']].groupby(['school__region_id']).agg(['median']))
