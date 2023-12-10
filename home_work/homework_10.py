########Task code#######
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
#print(lst)
data = pd.DataFrame({'whoAmI': lst})
########################

uniqueValues = set(lst);
for uniqueValue in uniqueValues:
    data.insert(1, uniqueValue, [1 if val == uniqueValue else 0 for val in lst ])

#Ниже закомменчено удаление начального столбца, для удобной проверки
#data.drop(['whoAmI'], axis = 1, inplace=True)

print(data)


