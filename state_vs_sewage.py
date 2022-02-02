import matplotlib.pyplot as m_plt
import matplotlib.ticker as ticker
import pandas
import numpy as np

sewage_data = pandas.read_csv('/Users/vishalpaudel/Library/CloudStorage/OneDrive-PlakshaUniversity/CS_Project_Sem1/Data/Sewage_Original.csv')
population_data = pandas.read_csv('/Users/vishalpaudel/Library/CloudStorage/OneDrive-PlakshaUniversity/CS_Project_Sem1/Data/state_population_2020.csv')

lst_state_name = list(sewage_data['States / UTs'])[:-2]
lst_sewage_generation = list(sewage_data['Sewage Generation (in MLD)'])[:-2]

lst_population = list(population_data['Total Population (Projected 2020)'])[:-2]
lst_population = [500 * int(population)/int(max(lst_population)) for population in lst_population]

fig, state_vs_sewage = m_plt.subplots(1,1)
state_vs_sewage.scatter(lst_state_name, lst_sewage_generation, s=lst_population, c=lst_population)
fig.set_figwidth(10)
m_plt.ylabel('MLD')
m_plt.xlabel('States')
m_plt.xticks(rotation=90)

y_sample = [2, 5, 10, 17]
x_sample = [1, 2, 3, 4]

m_plt.show()
