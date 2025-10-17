# Program #1: Rainfall
#Henry Forst
#10/16/25
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
months = 12
def main():
    month_names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    rainfall = [0] * months
    print("Enter the amount of rainfall (inches) in each month ")
    for index in range(len(rainfall)):
        rainfall[index] = float(input(f'{month_names[index]}:'))
    #Display enrty
    total = sum(rainfall)
    #print total
    print('The total rainfall for the year was:',total , 'inches')
    average = total / months
    #Print avg
    print(f'The average rainfall per month was: {round(average,): .2f}  inches')
    #Print least amt of rain
    minRain = min(rainfall)
    minMonth = month_names[rainfall.index(minRain)]
    print(f'The least amount inches of rain in a month was: {minRain} inches in {minMonth}')
    #print most amt of rain
    maxRain = max(rainfall)
    maxMonth = month_names[rainfall.index(maxRain)]
    print(f'The least amount inches of rain in a month was: {maxRain} inches in {maxMonth}')
if __name__ == '__main__':
    main()