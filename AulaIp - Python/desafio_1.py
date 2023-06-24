import math

packsNumberCurrent = int(input('Digite o número de packs:'))
packDividerToVillageNumber = math.floor(packsNumberCurrent/3)
packDiscartNumber = packsNumberCurrent%3
print(packDividerToVillageNumber)
print(packDiscartNumber)
