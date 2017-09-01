#Diego Aspinwall
#8-31-17
#tipCalculator.py

dollars = float(input('Price of Meal (in dollars): '))
tip = float(input('% to tip: '))
print('You should tip', round((dollars*tip)/100, 2), 'dollars')