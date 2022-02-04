import matplotlib.pyplot as plt
import numpy as np

barWidth = 0.5
fig = plt.subplots(figsize =(12, 8))

Installed = np.array([0, 833, 0, 0, 10, 293, 73, 24, 66, 3378, 1880, 136, 218, 22, 2712, 120, 0, 1839, 6890, 0, 0, 10, 0, 2896, 378, 56, 1781, 1086, 20, 1492, 901, 901, 3374, 448, 897])
Operational = np.array([0, 853, 0, 0, 631, 293, 73, 24, 104, 3378, 1880, 155, 222, 639, 2712, 120, 0, 1924, 9819, 0, 0, 10, 0, 2896, 378, 59, 1781, 1195, 30, 1492, 901, 8, 3374, 515, 1202])
Actual = np.array([0, 443, 0, 0, 0, 271, 73, 24, 44, 3358, 1880, 99, 93, 22, 1922, 114, 0, 684, 6366, 0, 0, 0, 0, 2715, 55, 56, 1601, 783, 18, 1492, 842, 8, 3224, 345, 337])


br1 = np.arange(len(Installed))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, Installed, color='r', width = barWidth, edgecolor = 'grey', label ='Installed')
plt.bar(br2, Operational, color='b', width = barWidth, edgecolor = 'grey', label = 'Operational')
plt.bar(br3, Actual, color = 'g', width = barWidth, edgecolor = 'grey', label = 'Actual')

plt.xlabel('Sewage Treatment Plants', fontweight = 'bold', fontsize = 15)
plt.ylabel('Capacity in MLD', fontweight = 'bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Installed))], ['A&N Islands','Andhra Pradesh', 'Arunachal Pradesh','Assam', 'Bihar','Chandigarh','Chattisgarh','D&N Haveli', 'Goa','Gujarat','Haryana','H. Pradesh','J&K','Jharkand','Karnataka','Kerala','Lakshadweep','M. Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','NCT Delhi', 'Orissa','Pondicherry','Punjab','Rajasthan','Sikkim','TamilNadu','Telangana','Tripura','U. Pradesh','Uttarkhand','West Bengal'],rotation ='vertical')

plt.legend(framealpha = 1, frameon = True)
plt.show()