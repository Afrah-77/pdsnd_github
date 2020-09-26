#import required python libraries
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
    while True:

        city = input("Please enter a valid city name from the following: \n chicago, new york city, washington:\n").lower()

        if city in ['chicago', 'new york city', 'washington']:

            break

        else:

            print("Invalid input! Please try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        month = input("\nPlease enter one of the following months:\n january, february, march, april, may, june OR enter all:\n ").lower()

        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:

            break

        else:

            print(" Invalid input! Please try again ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        day = input("\nPlease enter one of the following days:\n monday, tuesday, wednesday, thursday, friday, saturday, sunday OR enter all:\n ").lower()

        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:

            break

        else:

            print("invalid input. Please enter a valid input")


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
    df['Start Time'] =pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time (similar to practice 1)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter data by day
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]

# filter data by month
    if month != 'all':
        month_name = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_name.index(month) + 1

        df = df[df['month'] == month]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # first we need to extract month from Start Time (similar to practice 1)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    print("Most Common Month To Travel Is:", common_month )

    # TO DO: display the most common day of week
    # first we need to extract day from Start Time (similar to practice 1)
    df['day_of_week'] = pd.to_datetime(df['Start Time'])
    common_day = df['day_of_week'].mode()[0]

    print("Most Common Day To Travel Is:", common_day )

    # TO DO: display the most common start hour
    # first we need to extract hour from Start Time (similar to practice 1)
    df['hour'] = df['Start Time'].dt.hour
    common_str_hour= df['hour'].mode()[0]

    print("Most Common Start Hour Is: ", common_str_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_str_station=df['Start Station'].mode()[0]
    print("The Most Commonly Used Start Station Is:", common_str_station )

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("The Most Commonly Used End Station Is:", common_end_station )


    # TO DO: display most frequent combination of start station and end station trip
    common_both_station= df[['Start Station','End Station']] .mode().loc[0]
    print("The Most Commonly Used Start & End Station Is:", common_both_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The Total Travel Time Is:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The Mean Travel Time Is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type= df['User Type'].value_counts()
    print("The Count Of Each User Type: \n", count_user_type )

    # TO DO: Display counts of gender
    #I apply try & except block to handle exception when the information is not availble for selected city
    try:
        Count_gender= df['Gender'].value_counts()
        print("\nThe Count Of Gender Type: \n", Count_gender )

    except:
        print("\nIt seems that no gender Information available for the selected city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    #I apply try & except block to handle exception when the information is not availble for selected city
    try:
        earliest_DOB = int(df['Birth Year'].min())
        print("\nThe Earliest Year Of Birth Is:", earliest_DOB)

        most_recent_DOB = int(df['Birth Year'].max())
        print("\nThe Most Recent Year Of Birth Is:", most_recent_DOB)

        most_commn_DOB = int(df['Birth Year'].mode())
        print("\nThe Most Common Year Of Birth Is:", most_commn_DOB)
    except:
        print("\nIt seems that no birth year information available for the selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Below script prompts the user if they want to see 5 lines of raw data, display that data if the answer is 'yes',
#and continue these prompts and displays until the user says 'no'    
def data_display(df):
    x=0
    answer=input("Would you like to see 5 lines of raw data, Please enter yes or no.\n").lower()
    while True:
        if answer == 'yes':
           x=x+5
           print(df.head(x))
        else:
           break
           continue
        answer=input("Would you like to see 5 lines of raw data, Please enter yes or no.\n").lower()
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
