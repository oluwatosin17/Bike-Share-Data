import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to filter by?')
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        
        else:
            print("Sorry, you provided an invalid response.")


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month do you want to filter by? Make sure it's within the first six months, or just select all.")
        month = month.lower()
        if month in ["january","february", "march", "april","may", "june", "all"]:
            
            break
            
        else:
            print("Sorry, you provided an invalid input")
        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day to filter by, or just type in all to see everything.")
        day = day.lower()
        if day in ["monday", "tuesday", "wednessday", "thursday", "friday", "saturday", "sunday", "all"]:
            
            break
        
        else: 
            print("Sorry, you provided an invalid response")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular start month:', popular_month)

    # display the most common day of week
    day_of_week = df['day_of_week'].mode()[0]
    print('The most popular start day of the week:', day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print('The most popular start hour:', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_max = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is:", start_station_max)


    # display most commonly used end station
    end_station_max = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is:", end_station_max)


    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+ " " + df['End Station']
    combination_station_max = df['combination'].value_counts().idxmax()
    print("The most commonly used start station and end station is:", combination_station_max)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travels = sum(df["Trip Duration"])
    print("The total travel time is:", total_travels/604800, "weeks")
    
    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is:", mean_travel_time/60, "minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types 
    user_type = df['User Type'].value_counts()
    print("The counts of user types are:", user_type)
    
    print("------------------------------------")

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print("The counts of gender are:", gender)


    # Display earliest, most recent, and most common year of birth
    print("The earliest year is:", int(df["Birth Year"].min()))
    print("The most recent year is:", int(df["Birth Year"].max()))
    print("The most common year is:", int(df["Birth Year"].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def more_descriptive_stats(df):
    while True:
        discover = input('Do you want to see any more descriptive characteristics ? yes or no')
        discover = discover.lower()
        if discover == 'yes':
            print(df.describe())
        else:
            print('Finish')
        break
        
    print('-'*40)

        
def display_data(df):
    i = 0
    data = input("Do you want to see 5 rows of data? Accepted responses are yes or no ")
    data = data.lower()
    
    while True:
        if data == "no":
            break
        print(df[i:i+5])
        data = input("Do you wish to see the next 5 rows of data? yes or no")
        data = data.lower()
        
        i += 5
            
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_descriptive_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
   

if __name__ == "__main__":
	main()
