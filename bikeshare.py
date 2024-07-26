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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in ["chicago", "new york city", "washington","all"]:
        print('-'*40)
        print("the three cities are Chicago, new york city and washington")
        print('-'*40)
        city = input("Please write the city you want to explore or type 'all' to select all of them: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("Please write the month or type 'all' to select all of them: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
        day = input("Please write the day or type 'all' to select all of them: ").lower()


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
    cities = ["chicago", "new york city", "washington"]
    months = ["january", "february", "march", "april", "may", "june"]
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    df_list = []
    df_list_filtered = []
   
   # if city == "all":
   #     df.append(cities[0])
   # if month == "all":
   #     df.append(months)
   # if day == "all":
   #     df.append(days)
    # load data file into a dataframe
    if city != 'all':
        df_list.append(pd.read_csv(CITY_DATA[city]))
    else:
        for city_m in cities: 
            df_list.append(pd.read_csv(CITY_DATA[city_m]))
            #df.head()
    # convert the Start Time column to datetime
    for df in df_list:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
            # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
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
        df_list_filtered.append(df)
    return df_list_filtered

def time_stats(df_list_filtered):
    """Displays statistics on the most frequent times of travel."""
    for df in df_list_filtered:
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        print("most common month is: ", df['month'].mode()[0])

        # TO DO: display the most common day of week
        print("most common day is: ", df['day_of_week'].mode()[0])

        # TO DO: display the most common start hour
        print("most common start hour is: ", df['Start Time'].mode()[0])

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df_list_filtered):
    """Displays statistics on the most popular stations and trip."""
    for df in df_list_filtered:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        print("most common start station is: ", df['Start Station'].mode()[0])

        # TO DO: display most commonly used end station
        print("most common end station is: ", df['End Station'].mode()[0])

        # TO DO: display most frequent combination of start station and end station trip
        print("most frequent combination of start station and end station trips is: " + df[['Start Station', 'End Station']].mode().loc[0])

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df_list_filtered):
    """Displays statistics on the total and average trip duration."""
    for df in df_list_filtered:
        
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        print("total travel time is ", df['Trip Duration'].sum()) 

        # TO DO: display mean travel time
        print("mean travel time is ", df['Trip Duration'].mean()) 

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df_list_filtered):
    """Displays statistics on bikeshare users."""
    for df in df_list_filtered:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print("user types are ", df['User Type'].count())

        # TO DO: Display counts of gender
        try: 
            print("genders are ", df['Gender'].count())
        except:
            print("city has no gender data")
        # TO DO: Display earliest, most recent, and most common year of birth
        try:
              print("earliest: ", df['Birth Year'].min())
              print("most recent: ", df['Birth Year'].max())
              print("most common: ", df['Birth Year'].mode()[0])
        except:
              print("city has no birthyear data")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df_list_filtered):
    for df in df_list_filtered:
        while True:
            confirm = input("Would you like to see raw data? write 'yes' if so:").strip().lower()
            if confirm == "yes":
                print(df.sample(5))
            else:
                break
                
def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
