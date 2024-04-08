import math
currentSteveX = int(input())
currentSteveZ = int(input())

village = ["Hogsmeade","Kakariko","Solitude"]
valuesXY = [{"X":34, "Z":220},{"X":0,"Z":0},{"X":140,"Z":456}]

for index,i in enumerate(village):
    distance = float(math.sqrt(((valuesXY[index]["X"] - currentSteveX)*(valuesXY[index]["X"]-currentSteveX))+((valuesXY[index]["Z"]-currentSteveZ)*(valuesXY[index]["Z"]-currentSteveZ))))
    print(f"Distancia para {i} {distance:,.2f}")

