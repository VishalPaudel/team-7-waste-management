import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('/Users/vishalpaudel/Library/CloudStorage/OneDrive-PlakshaUniversity/CS_Project_Sem1/Data/state_population_2020.csv')

lst_population = data['Total Population (Projected 2020)']
lst_generated = data['Sewage Generation (in MLD)']
lst_installed_capacity = data['Installed Capacity (in MLD)']

state_labels = data['State Name']


def per_person(temp_lst_input):
    global lst_population

    return [temp_lst_input[index] / lst_population[index] for index in range(0, len(lst_population))]


generation_per_person = per_person(lst_generated)
max_gpp = max(generation_per_person)
percent_generation = [100 * generation_per_person[index]/max_gpp for index in range(0, len(generation_per_person))]

fig1, ax1 = plt.subplots(figsize=(12, 10))
ax1.pie(percent_generation, labels=state_labels, shadow=True, radius=1800)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig1.suptitle('Sewage generation per Person', fontsize=32)

plt.show()

installed_per_person = per_person(lst_installed_capacity)
max_ipp = max(installed_per_person)
percent_generation = [100 * installed_per_person[index]/max_ipp for index in range(0, len(installed_per_person))]

fig1, ax1 = plt.subplots(figsize=(12, 10))
ax1.pie(percent_generation, labels=state_labels, shadow=True, radius=1800)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig1.suptitle('Installed capacity per Person', fontsize=32)

plt.show()

