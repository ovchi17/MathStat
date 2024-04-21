import csv
import matplotlib.pyplot as plt

count = 0 # количество машин
carsType = {} # типы машин + их количество
carsAndPower = [] # тип машины + лошадиные силы
with open('pythonWorks/cars93.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if(count != 0):
            carsAndPower.append((row[2], row[12]))
            if (row[2] in carsType):
                carsType[row[2]] += 1
            else:
                carsType[row[2]] = 1
        count += 1
count -= 1
carsType = {k: v for k, v in sorted(carsType.items(), key=lambda item: item[1])}
carsAndPower = sorted(carsAndPower, key=lambda x: int(x[1]))
print("-------------------------------------------------------------------------------")
print("ТИПЫ АВТОМОБИЛЕЙ:")
for type in carsType.keys():
    print(type)
print("-------------------------------------------------------------------------------")
print("САМЫЙ РАСПРОСТАРНЕННЫЙ ТИП: " + list(carsType.keys())[-1])
print("НАИМЕНЕЕ РАСПРОСТАРНЕННЫЙ ТИП: " + list(carsType.keys())[0])
print("-------------------------------------------------------------------------------")
print("ДЛЯ ВСЕХ АВТОМОБИЛЕЙ")  
sm = 0 # сумма мощностей
for i in carsAndPower:
    sm += int(i[1])
sampleAverage = sm / count # выборочное среднее !
dispersionSum = 0 # квадратная сумма разностей значения и среднего
for i in carsAndPower:
    dispersionSum += (int(i[1]) - sampleAverage)**2
sampleDispersion = dispersionSum / count # выборочная дисперсия !
if(count % 2 == 1):
    sampleMedian = int(carsAndPower[count // 2][1]) # выборочная медиана !
    if(count // 2 % 2 == 1):
        firstKvantil = int(carsAndPower[count // 2 // 2][1]) # первый квантиль
        secondKvantil = int(carsAndPower[(count // 2 // 2) + (count // 2) ][1]) # второй квантиль
    else:
        firstKvantil = (int(carsAndPower[count // 2 // 2][1]) + int(carsAndPower[count // 2 // 2 - 1][1])) // 2 # первый квантиль
        secondKvantil = (int(carsAndPower[(count // 2 // 2) + (count // 2)][1]) + int(carsAndPower[(count // 2 // 2 - 1) + (count // 2)][1])) // 2 # второй квантиль
else:
    sampleMedian = (int(carsAndPower[count // 2 - 1][1]) + int(carsAndPower[count // 2][1])) // 2 # выборочная медиана !
    if((count // 2 - 1) % 2 == 1):
        firstKvantil = int(carsAndPower[(count // 2 - 1) // 2][1]) # первый квантиль
        secondKvantil = int(carsAndPower[((count // 2 - 1) // 2) + (count // 2) ][1]) # второй квантиль
    else:
        firstKvantil = (int(carsAndPower[(count // 2 - 1) // 2][1]) + int(carsAndPower[(count // 2 - 1) // 2 - 1][1])) // 2 # первый квантиль
        secondKvantil = (int(carsAndPower[((count // 2 - 1) // 2) + (count // 2)][1]) + int(carsAndPower[((count // 2 - 1) // 2 - 1) + (count // 2)][1])) // 2 # второй квантиль
print("Выборочное средние: " + str(sampleAverage))
print("Выборочная диспресия: " + str(sampleDispersion))
print("Выборочная медиана: " + str(sampleMedian))
print("Межквартильный размах мощности: " + str(secondKvantil - firstKvantil))
print("-------------------------------------------------------------------------------")
for type in carsType.keys():
    print("ДЛЯ " + type)
    typePower = []
    typeCount = 0
    for car in carsAndPower:
        if car[0] == type:
            typePower.append(car)
            typeCount += 1
    sm = 0 # сумма мощностей
    for i in typePower:
        sm += int(i[1])
    sampleAverage = sm / typeCount # выборочное среднее !
    dispersionSum = 0 # квадратная сумма разностей значения и среднего
    for i in typePower:
        dispersionSum += (int(i[1]) - sampleAverage)**2
    sampleDispersion = dispersionSum / typeCount # выборочная дисперсия !
    if(typeCount % 2 == 1):
        sampleMedian = int(typePower[typeCount // 2][1]) # выборочная медиана !
        if(typeCount // 2 % 2 == 1):
            firstKvantil = int(typePower[typeCount // 2 // 2][1]) # первый квантиль
            secondKvantil = int(typePower[(typeCount // 2 // 2) + (typeCount // 2) ][1]) # второй квантиль
        else:
            firstKvantil = (int(typePower[typeCount // 2 // 2][1]) + int(typePower[typeCount// 2 // 2 - 1][1])) // 2 # первый квантиль
            secondKvantil = (int(typePower[(typeCount // 2 // 2) + (typeCount // 2)][1]) + int(typePower[(typeCount // 2 // 2 - 1) + (typeCount // 2)][1])) // 2 # второй квантиль
    else:
        sampleMedian = (int(typePower[typeCount // 2 - 1][1]) + int(typePower[typeCount // 2][1])) // 2 # выборочная медиана !
        if((typeCount // 2 - 1) % 2 == 1):
            firstKvantil = int(typePower[(typeCount // 2 - 1) // 2][1]) # первый квантиль
            secondKvantil = int(typePower[((typeCount // 2 - 1) // 2) + (typeCount // 2) ][1]) # второй квантиль
        else:
            firstKvantil = (int(typePower[(typeCount // 2 - 1) // 2][1]) + int(typePower[(typeCount // 2 - 1) // 2 - 1][1])) // 2 # первый квантиль
            secondKvantil = (int(typePower[((typeCount // 2 - 1) // 2) + (typeCount // 2)][1]) + int(typePower[((typeCount // 2 - 1) // 2 - 1) + (typeCount // 2)][1])) // 2 # второй квантиль
    print("Выборочное средние: " + str(sampleAverage))
    print("Выборочная диспресия: " + str(sampleDispersion))
    print("Выборочная медиана: " + str(sampleMedian))
    print("Межквартильный размах мощности: " + str(secondKvantil - firstKvantil))
    print("-------------------------------------------------------------------------------")

powerListAll = []
powerList = []
powerCount = []

for power in carsAndPower:
    powerListAll.append(int(power[1]))
    if int(power[1]) not in powerList:
        powerList.append(int(power[1]))
        powerCount.append(1)
    else:
        powerCount[len(powerList) - 1] += 1

for i in range(len(powerCount)):
    powerCount[i] = powerCount[i] / count
for i in range(1, len(powerCount)):
    powerCount[i] += powerCount[i - 1]

plt.plot(powerList, powerCount, marker='o')
plt.xlabel('Значения')
plt.ylabel('Вероятность')
plt.title('Эмпирическая функция распределения для всех автомобилей')
plt.grid(True)
plt.show()
plt.hist(powerListAll)
plt.title('Гистограмма для всех автомобилей')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()
plt.boxplot(powerListAll)
plt.title('Box-plot для всех автомобилей')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()


for type in carsType.keys():
    powerListAll = []
    powerList = []
    powerCount = []
    countType = 0

    for power in carsAndPower:
        if power[0] == type:
            countType += 1
            powerListAll.append(int(power[1]))
            if int(power[1]) not in powerList:
                powerList.append(int(power[1]))
                powerCount.append(1)
            else:
                powerCount[len(powerList) - 1] += 1

    for i in range(len(powerCount)):
        powerCount[i] = powerCount[i] / countType
    for i in range(1, len(powerCount)):
        powerCount[i] += powerCount[i - 1]

    plt.plot(powerList, powerCount, marker='o')
    plt.xlabel('Значения')
    plt.ylabel('Вероятность')
    plt.title('Эмпирическая функция распределения для ' + type)
    plt.grid(True)
    plt.show()
    plt.hist(powerListAll)
    plt.title('Гистограмма для ' + type)
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.show()
    plt.boxplot(powerListAll)
    plt.title('Box-plot для ' + type)
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.show()