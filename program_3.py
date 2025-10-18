#Henry Forst
#10/16/25
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    all_entered_values = []

    # Now have the user enter a year. 
    while True:
        year = input("Enter a year (or stop to be finished): ")
        if year == 'stop':
            break 
        state = input("Enter a state: ")
        population = int(input("Enter the population of the state: "))
        all_entered_values.append([year, state, population])
    findYear = input("Enter a year to view the population from that year:")
    for info in all_entered_values:
        if info[0] == findYear:
            print(f'The population in {info[1]} was : {info[2]} people')
    total = sum_population_for_year(all_entered_values, findYear)
    print(f'The total population for year number {findYear}: {total} people')


    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
def sum_population_for_year(data, year):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population
    total = 0
    for info in data:
        if info[0] == year:
            total += info[2]
    return total

# Call the main function.
if __name__ == '__main__':
    main()