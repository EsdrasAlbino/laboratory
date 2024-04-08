valueOne = int(input())
valueTwo = int(input())
valueThree = int(input())
hours = int(input())

NumberI = (valueOne + valueTwo+ (abs(valueOne-valueTwo)))/2
valueMax = (NumberI + valueThree+ (abs(NumberI-valueThree)))/2
numberOfDiamonds = valueMax*hours

print(f"{numberOfDiamonds:.0f}")


