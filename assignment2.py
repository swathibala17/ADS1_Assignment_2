# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_file(file):
    """
    function to read csv file as datafreame and transpose it
    """ 
    df = pd.read_csv(file)
    df_transposed = pd.DataFrame.transpose(df)
    #Header
    header = df_transposed.iloc[0].values.tolist()
    df_transposed.columns = header

    #Cleaning the dataframe
    df_transposed = df_transposed.iloc[1:]
    df_transposed = df_transposed.iloc[4:66]
    df_transposed.index = df_transposed.index.astype(int)
    df_transposed = df_transposed[df_transposed.index>1959]
    df_transposed = df_transposed[df_transposed.index<2021]
    return(df, df_transposed)

def choose_countries(df,countries):
    """
    function to filter dataframe with selected countries
    """ 
    df_countries=df.loc[df['Country Name'].isin(countries)]
    return df_countries

# bar chart
def barchart(df_data,x_values,columns,xlabel,ylabel,title,file):
    """
    creates a bar graph of selected countries
    """ 
    x_axis = np.arange(len(x_values))
    x_width=0.1
    plt.figure()
    # start with first column
    plt.bar(x_axis - x_width , df_data[columns[0]], width=0.1, label=columns[0])
    plt.bar(x_axis, df_data[columns[1]], width=0.1, label=columns[1])
    for i in range(2, len(columns)):
            plt.bar(x_axis + (i-1) * x_width , df_data[columns[i]], 
                    width=0.1, label=columns[i])
    plt.xticks(x_axis, x_values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()    
    plt.savefig(file + ".png")
    plt.show()

countries=["Australia","Japan","Belgium","Hungary","India","France"] 
years=["1970","1980","1990","2000","2010","2020"]

#calling to plot CO2 Emission bar graph
df,df_transposed=read_file("CO2 emissions.csv")
df_co2emmision=choose_countries(df,countries)
x_values = df_co2emmision["Country Name"]
xlabel="Country Name"
ylabel="CO2 Emission(%)"
title=ylabel +" in Countries"
barchart(df_co2emmision,x_values,years,xlabel,ylabel,title,"co2emission")

#calling to plot population growth bar graph
df,df_transposed=read_file("Population growth.csv")
df_popualation=choose_countries(df,countries)
x_values = df_popualation["Country Name"]
xlabel="Country Name"
ylabel=df_popualation.iloc[0]["Indicator Name"]
title=ylabel +" in Countries"
barchart(df_popualation,x_values,years,xlabel,ylabel,title,"population")

#calling to plot Mortality rate line plot
df,df_mortalityrate=read_file("Mortality rate.csv")
plt.figure()
for i in range(0, len(countries)):
     plt.plot(df_mortalityrate.index, df_mortalityrate[countries[i]])
plt.xlim(1970,2020)
plt.xlabel("Year")
plt.ylabel("Mortality rate %")
plt.legend(countries)
plt.title("Mortality rate (% of land area)")
plt.savefig("Mortality_rate.png", dpi = 300, bbox_inches='tight')
plt.show()

#calling to plot mean of agricultural land in pie chart
df,df_agriland=read_file("Agricultural land.csv")
agrimean = np.mean(df_agriland[countries])
plt.figure()
plt.pie(agrimean, autopct = "%1.1f%%")
plt.legend(bbox_to_anchor=(0,1), labels = countries)
plt.title("Agricultural land (% of land area)")
plt.savefig("agricultural_land.png", dpi = 300, bbox_inches='tight')
plt.show()






    
