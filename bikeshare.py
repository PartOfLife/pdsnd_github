# Import necessary libraries
import time
import pandas as pd
import numpy as np

# Define the dictionary of city data
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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to analyze? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from chicago, new york city, washington.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Which month? (january, february, ... , june, or all): ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please choose from january, february, ... , june, or all.")
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Which day? (monday, tuesday, ... sunday, or all): ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please choose from monday, tuesday, ... sunday, or all.")
    
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    df['hour'] = df['Start Time'].dt.hour
    common_month = df['month'].mode()[0]
    print("Most Common Month:", common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week:", common_day)
    
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour:", common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most Commonly Used Start Station:", common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most Commonly Used End Station:", common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + " to " + df['End Station']
    common_station_combination = df['Station Combination'].mode()[0]
    print("Most Frequent Combination of Start Station and End Station Trip:", common_station_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time:", total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time:", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:\n", user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:\n", gender_counts)
    else:
        print("\nGender data not available.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("\nEarliest Year of Birth:", earliest_year)
        print("Most Recent Year of Birth:", most_recent_year)
        print("Most Common Year of Birth:", most_common_year)
    else:
        print("\nBirth Year data not available.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        
        # Load the data from the CSV file
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Prompt the user if they want to see 5 lines of raw data
        show_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if show_raw_data.lower() == 'yes':
            row_index = 0
            while True:
                print(df.iloc[row_index:row_index+5])
                row_index += 5
                show_next = input('\nWould you like to see the next 5 lines of raw data? Enter yes or no.\n')
                if show_next.lower() != 'yes' or row_index >= len(df):
                    break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
