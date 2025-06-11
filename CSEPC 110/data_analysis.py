user_year = int(input("Enter the year of interest: "))
with open("CSEPC 110/life_expectancy.csv") as life_expectancy:
    next(life_expectancy)
    total_expectancy = 0
    average_expectancy = 0
    count_rows = 0

    lowest_expectancy  = 9999999999999999999999999
    highest_expectancy = -1

    lowest_expectancy_user  = 9999999999999999999999999
    highest_expectancy_user = -1
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

        ###############################################

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
        
    print(f"The overall max life expectancy is: {highest_expectancy} from {highest_expectancy_country} in {highest_expectancy_year}")
    print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_expectancy_country} in {lowest_expectancy_year}")

    print(f"For the year {user_year}:")
    average_expectancy = total_expectancy / count_rows
    print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
    print(f"The max life expectancy was in {highest_expectancy_user_country} with {highest_expectancy_user}")
    print(f"The min life expectancy was in {lowest_expectancy_user_country} with {lowest_expectancy_user}")
