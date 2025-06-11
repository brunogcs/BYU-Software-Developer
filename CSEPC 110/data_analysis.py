"""
Creativity: Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
"""

user_year = int(input("Enter the year of interest: "))
user_country = input("Enter the country of interest: ")
with open("CSEPC 110/life_expectancy.csv") as life_expectancy:
    next(life_expectancy)

    #for year
    total_expectancy = 0
    average_expectancy = 0
    count_rows = 0

    #for country
    total_expectancy_country = 0
    average_expectancy_country = 0
    count_rows_country = 0

    lowest_expectancy  = 9999999999999999999999999
    highest_expectancy = -1

    lowest_expectancy_user  = 9999999999999999999999999
    highest_expectancy_user = -1

    lowest_expectancy_userCountry  = 9999999999999999999999999
    highest_expectancy_userCountry = -1
    for line in life_expectancy:  
        #read the file and split columns in variables
        line = line.split(",")
        country = line[0]
        country_Code = line[1]
        year = int(line[2])
        expectancy = float(line[3])

        #print(f"The {country}, code {country_Code}, in the {year} year had this life expectancy {expectancy}")
        #exit()

        #find the lowest overall
        if expectancy < lowest_expectancy:
            lowest_expectancy = expectancy
            lowest_expectancy_country = country
            lowest_expectancy_year = year

        #find the highest overall
        if expectancy > highest_expectancy:
            highest_expectancy = expectancy
            highest_expectancy_country = country
            highest_expectancy_year = year

        ###################### YEAR #########################

        #find the expectancy average
        if year == user_year:
            total_expectancy += expectancy
            count_rows += 1

            #find the lowest in the selected year
            if expectancy < lowest_expectancy_user:
                lowest_expectancy_user = expectancy
                lowest_expectancy_user_country = country

            #find the highest in the selected year and year == user_year
            if expectancy > highest_expectancy_user:
                highest_expectancy_user = expectancy
                highest_expectancy_user_country = country
        
        ###################### COUNTRY #########################

        #find the expectancy average
        if country.lower() == user_country.lower():
            total_expectancy_country += expectancy
            count_rows_country += 1

            #find the lowest in the selected year
            if expectancy < lowest_expectancy_userCountry:
                lowest_expectancy_userCountry = expectancy
                lowest_expectancy_user_year = year

            #find the highest in the selected year and year == user_year
            if expectancy > highest_expectancy_userCountry:
                highest_expectancy_userCountry = expectancy
                highest_expectancy_user_year = year
        
    print(f"The overall max life expectancy is: {highest_expectancy:.2f} from {highest_expectancy_country} in {highest_expectancy_year}")
    print(f"The overall min life expectancy is: {lowest_expectancy:.2f} from {lowest_expectancy_country} in {lowest_expectancy_year}")

    print(f"For the year {user_year}:")
    average_expectancy = total_expectancy / count_rows
    print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
    print(f"The max life expectancy was in {highest_expectancy_user_country} with {highest_expectancy_user:.2f}")
    print(f"The min life expectancy was in {lowest_expectancy_user_country} with {lowest_expectancy_user:.2f}")

    print(f"For the country {user_country}:")
    average_expectancy_country = total_expectancy_country / count_rows_country
    print(f"The average life expectancy across all countries was {average_expectancy_country:.2f}")
    print(f"The max life expectancy was in {highest_expectancy_user_year} with {highest_expectancy_userCountry:.2f}")
    print(f"The min life expectancy was in {lowest_expectancy_user_year} with {lowest_expectancy_userCountry:.2f}")