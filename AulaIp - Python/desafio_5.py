dayConstructorInRealLife = int(input())
numberOfHome = int(input())

ticksPerDayConstructor = 12000
totalTicksConstructor = ticksPerDayConstructor * (9 *dayConstructorInRealLife)
ticksConstructorPerHome = totalTicksConstructor/numberOfHome

print(f"{ticksConstructorPerHome:.0f}")