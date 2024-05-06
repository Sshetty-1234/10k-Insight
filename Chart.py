# Loads in the dataset and plots it

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Charts/APPL_Overall_Expenditures.csv")

df2 = pd.read_csv("Charts/DELL_Overall_Expenditures.csv")

## print(df.tail())

# Dropping rows with NaN values in specific columns 
df = df.dropna()

'''
print(" \n"
      "------------------------------------------------------ \n"
         "              After Values dropped \n")
'''

# Takes values such as millions and billions and converts them to their numeric form
def convert(value):
    if 'million' in value:
        return float(value.replace(' million', '')) * 1e6
    elif 'billion' in value:
        return float(value.replace(' billion', '')) * 1e9
    else:
        return float(value)

df['Total Expenditure'] = df['Total Expenditure'].apply(convert)


# Sorts the values
df= df.sort_values(by='Total Expenditure', ascending=True)

#print(df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Total Expenditure'] / 1e9, marker='o')  
plt.xlabel('Year')
plt.ylabel('Total Expenditure (Billion $)')
plt.title('Apple Overall Expenditure Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

##plt.savefig('APPL_expenditure_chart.png')
plt.show()



df2['Total Expenditure'] = df2['Total Expenditure'].apply(convert)

df2= df2.sort_values(by='Total Expenditure', ascending=True)

print(df2)

plt.figure(figsize=(10, 6))
plt.plot(df2['Year'], df2['Total Expenditure'] / 1e9, marker='o')  
plt.xlabel('Year')
plt.ylabel('Total Expenditure (Billion $)')
plt.title('Apple Overall Expenditure Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
#plt.savefig('DELL_expenditure_chart.png')
#plt.show()

'''
Q - Why would a potential investor care about this information?

"Understanding a company's overall expenditure plan is crucial because it shows a \n "
            "commitment to optimal resource and fund allocation. Furthermore, investors love this \n" 
            "approach since it shows a company's unwavering pursuit of growth and expansion, \n"
            "and not settling for anything less."
'''