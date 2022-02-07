import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('/Users/vishalpaudel/Library/CloudStorage/OneDrive-PlakshaUniversity/CS_Project_Sem1/Data/state_population_2020.csv')

lst_population = data['Total Population (Projected 2020)']
lst_generated = data['Sewage Generation (in MLD)']
lst_installed_capacity = data['Installed Capacity (in MLD)']
lst_treatment_capacity = data['Total Treatment Capacity (in MLD) including planned / proposed']

state_labels = data['State Name']


def per_person(temp_lst_input):
    global lst_population

    return [temp_lst_input[index] / lst_population[index] for index in range(0, len(lst_population))]


capacity_per_person = per_person(lst_treatment_capacity)
max_ipp = max(capacity_per_person)

generation_per_person = per_person(lst_generated)
max_gpp = max(generation_per_person)
percent_generation = [100 * generation_per_person[index]/max_gpp for index in range(0, len(generation_per_person))]

fig1, ax1 = plt.subplots(figsize=(12, 10))
ax1.pie(percent_generation, labels=state_labels, shadow=True, radius=1800)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig1.suptitle('Sewage generation per Person', fontsize=32)

plt.show()

index = 0
lst_difference = []
while index in range(0, len(state_labels)):

    lst_difference.append(capacity_per_person[index] - generation_per_person[index])
    index = index + 1


def bubble_sort(temp_lst_main, temp_lst_side, bool_mute=False):
    """
    This function is the normal replication of bubble sort algorithm. <wiki_link>.
    (list, bool=False) --> list

    :param temp_lst_main: The list that you want to sort
    :param temp_lst_side: The list you want to manipulate side by side
    :param bool_mute: Pass True if you don't want to see print statements
    :return: temp_lst_main: A deep copy of your list only sorted ascending order
    """
    temp_lst_main = list(temp_lst_main)
    temp_lst_side = list(temp_lst_side)

    int_outer_index = 0
    int_swap_count = 0
    while int_outer_index < (len(temp_lst_main)):

        int_inner_index = 0
        while int_inner_index < (len(temp_lst_main) - int_outer_index - 1):

            if temp_lst_main[int_inner_index] > temp_lst_main[int_inner_index + 1]:
                """
                New swapper found!
                """

                temp_lst_main[int_inner_index], temp_lst_main[int_inner_index + 1] = temp_lst_main[int_inner_index + 1], \
                                                                                     temp_lst_main[int_inner_index]
                temp_lst_side[int_inner_index], temp_lst_side[int_inner_index + 1] = temp_lst_side[int_inner_index + 1], \
                                                                                     temp_lst_side[int_inner_index]
                if not bool_mute:
                    print('|\nSwap Happened\n|', temp_lst_main, sep='\n')
                int_swap_count += 1

            int_inner_index += 1
            if not bool_mute:
                print('|\nCounter shifted\n|', temp_lst_main, sep='\n')

        if int_swap_count == 0:
            if not bool_mute:
                print('|\nThe List was already Sorted !\n')
            break

        int_outer_index += 1

    if not bool_mute:
        print('\n' + str(int_swap_count), 'time swaps')

    return temp_lst_main, temp_lst_side


lst_difference, state_labels = bubble_sort(lst_difference, state_labels)

fig1, ax1 = plt.subplots(figsize=(12, 20))
ax1.bar(state_labels, lst_difference)
fig1.suptitle('Discrepancy: More Positive == The better', fontsize=32)
plt.xticks(rotation=90)
plt.xlabel('State Names')
plt.ylabel('Total Treatment Capacity minus Sewage production PER PERSON')

plt.show()
