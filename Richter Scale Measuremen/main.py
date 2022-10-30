import math
TNT = 4.184 * 10**9

print('Richter \t Joules \t\t\t\t\t TNT')
print(f'1 \t\t{math.pow(10,1.5 + 4.8)}\t\t\t      {(math.pow(10,1.5+4.8)) / TNT}')
print(f'5 \t\t{math.pow(10,(1.5 * 5) + 4.8)} \t\t\t\t{(math.pow(10,(1.5 * 5)+4.8)) / TNT}')
print(f'7 \t\t{math.pow(10,(1.5 * 7) + 4.8)} \t\t\t {(math.pow(10,(1.5 * 7)+4.8)) / TNT}')
print(f'9.1 \t{math.pow(10,(1.5 * 9.1) + 4.8)}  \t  {(math.pow(10,(1.5 * 9.1)+4.8)) / TNT}')
print(f'9.2 \t{math.pow(10,(1.5 * 9.2) + 4.8)}  \t  {(math.pow(10,(1.5 * 9.2)+4.8)) / TNT}')
print(f'9.5 \t{math.pow(10,(1.5 * 9.5) + 4.8)}\t {(math.pow(10,(1.5 * 9.5)+4.8)) / TNT}\n')
richter = float(input("Please enter a Richter Scale Value: "))
energy = math.pow(10,(1.5 * richter) + 4.8)
print(f'Richter scale value: {richter}')
print(f'Equivalence in joules: {energy}')
print(f'Equivalence in tons of TNT {energy / TNT}')
