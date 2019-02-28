import time
import pandas as pd
import numpy as np
import re




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
'''
How could I preoload each csv file from the dictionary as a loop?
Err: 'too many values to unpack (expected 2)'

for city in CITY_DATA.keys():
    pd.read_csv(city)
    #data[['Start Time','End Time']] = data[['Start Time','End Time']].apply(pd.to_datetime)
print(CITY_DATA['washington'])
'''
head_num = 99999999999999999
city_input = 'x'
month_input = 'x'
raw_day_input = []
valid_day_input = []
days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
calander_months = ['January','February','March','April','May','June','July','August','September','October','November','December','all']


def show_raw_data():
    data_request = input('Would you like to see some of the raw data? ')
    row_numbers = 0
    while data_request != 'no':

        row_numbers += 5
        print(df.head(row_numbers))
        data_request = input('Would you like more raw data? Yes or no. ')




def get_filters():
    #Are these global commands proper? I could not find another solution.
    global city_input
    global month_input
    global raw_day_input
    global valid_day_input
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Start a loop that will run until the user enters 'quit'.


    while city_input not in (CITY_DATA.keys()):
        city_input = input('Would you like data for Washington, New York City, or Chicago?\n').lower()
        if city_input == 'nyc' or 'new york':
            city_input = 'new york city'
        if city_input not in (CITY_DATA.keys()):
            print('Hmmmmm, we dont have data for that city yet.')
        else:
            print("\nGreat! You have chosen {}.".format(city_input.title()))
            city_input = city_input
    # get user input for month (all, january, february, ... , june)
    while month_input not in calander_months:
        month_input = input('\nWhat month of the year would you like? You could choose "ALL" as an option\n').lower()
        if month_input[:3] in ('jan','01','1'):
            month_input = 'January'
        elif month_input[:3] in ('feb','02','2'):
             month_input = 'February'
        elif month_input[:3] in ('mar','03','3'):
             month_input = 'March'
        elif month_input[:3] in ('apr','04','4'):
             month_input = 'April'
        elif month_input[:3] in ('may','05','5'):
             month_input = 'May'
        elif month_input[:3] in ('jun','06','6'):
             month_input = 'June'
        elif month_input[:3] in ('jul','07','7'):
             month_input = 'July'
        elif month_input[:3] in ('aug','08','8'):
             month_input = 'August'
        elif month_input[:3] in ('sep','09','9'):
             month_input = 'September'
        elif month_input[:3] in ('oct','10'):
             month_input = 'October'
        elif month_input[:3] in ('nov','11'):
             month_input = 'November'
        elif month_input[:3] in ('dec','12'):
             month_input = 'December'
        elif month_input == 'all':
             month_input = 'all'
        else:
            print('\nThat does not seem to be a month. Try a different format.')

    if month_input in calander_months[:12]:
        print('\nNice, we will use {}\'s data.\n'.format(month_input))
    elif month_input == 'all':
        print('\nOk, we will use all the months" data.\n')




    # get user input for day of week (all, monday, tuesday, ... sunday)

    raw_day_input = input('There is one last question we have. Which day/s of the week would you like the data from? You may choose "ALL"\n').lower()
    raw_day_input = re.sub(r'[^\w\s]','',raw_day_input).split()

    for day in raw_day_input:
        if day == 'all':
            valid_day_input.append(day)
        elif day in days_of_week:
            valid_day_input.append(day.title())

    if 'all' in valid_day_input:
        print('\nWe will use all days of the week.')
    elif (len(valid_day_input)) == 1:
        print('\nThe day you have chosen is {}.'.format(str(valid_day_input).strip("['']")))
    else: #There has to be a better way and the comma usage is still wrong maybe a for loop?
        print('\nThe days you have chosen are',', '.join((valid_day_input[:-1])),'&',str(valid_day_input[-1]).strip("['']"))





    print('-'*40)
    #return city_input, month_input, valid_day_input

#Below print call is for testing

get_filters()
"""
print("Your city variable is:",city_input)
print("Your month variable is:",month_input)
print("Your chosen day/s is:",valid_day_input)
"""

###########################################################


def load_data(city,month,day):

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
    """ To load the selected city csv file based on user input """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    """ To convert start time into standard time """
    df['month'] = df['Start Time'].dt.month
    """ To get the month value from start time of original csv"""
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    """ To get the day_of_week value from start time of original csv"""


    for d in day:
        if d != 'all':
            """ If selected day is not none in choice then this function will trigger """
            df = df[df['day_of_week'].isin(day)]
            """ This line filters the day_input that are TRUE with day_of_week """
    if month != 'all':
        """ If selected month is not none in choice then this function will triggers """
        month = calander_months.index(month)+1
        """ This assigns a numerical month value to the user input """
        df = df[df['month'] == month]
        """ This line filter the numerical month values that are equal """
    else:
        return df
###??? On second pass, if 'All' is selected as month shows all data ???###

#print(load_data(city_input,month_input,valid_day_input).head(head_num))
print()
print('-'*100)
""" To print a straight line """

df=load_data(city_input,month_input,valid_day_input).head(head_num)
#df
"""This applies the DataFrame Filters from User imput"""
"""Has to be after Funtion so that it can be called"""


###########################################################


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    """give variable for time count """

    # display the most common month
    common_month = df['month'].mode()
    """Returns most common month of filtered DataFrame as Series"""
    common_month = list(common_month.values)
    """Converts to list of Values"""
    for m in range(len(list(common_month))):
        common_month[m] = calander_months[common_month[m]-1]
    """This converts the numberical month to human readable format"""
    """??? Why did I need to convert array to list ???"""
    print('The most common month/s: ',common_month)

    # display the most common day of week
    common_day = list(df['day_of_week'].mode())
    print('The most common day/s: ',common_day)

    # display the most common start hour
    common_hour = list(df['Start Time'].dt.strftime("%I:00%p").mode())
    print('The most common hour/s:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    show_raw_data()

print(time_stats(df))


###########################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = list(df['Start Station'].mode())
    print('The most common start station/s: ',common_start_station)
    # display most commonly used end station

    common_end_station = list(df['End Station'].mode())
    print('The most common end station/s: ',common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start/End'] = df['Start Station'] + ' to ' + df['End Station']
    common_path = list(df['Start/End'].mode())
    print('The most common trip/s: ',common_path)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #show_raw_data()

print(station_stats(df))

###########################################################

def trip_duration_stats(df):
    try:
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        total_travel_time = int(sum(df['Trip Duration'])/60/60)
        print('Total Time: {} hours'.format(total_travel_time))

        # display mean travel time
        mean_trip_time = df['Trip Duration'].mean()/60
        print('\nThe average trip was {:.2f} minutes long.'.format(mean_trip_time))
        print('\nThe average trip was ',
                str(mean_trip_time).split('.')[0],
                'minutes and ',
                int(60 * float('.'+(str(mean_trip_time).split('.')[1]))),
                'seconds long.'
                )

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        #show_raw_data()
    except:
        print('Hmmm, something is wrong with our data, call 555-555-5555 for help')


print(trip_duration_stats(df))


###########################################################

def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        print('Below are the user types of your selected data:')
        print(df['User Type'].dropna(axis=0).value_counts())
        print()
        # Display counts of gender
        print('Below are the gender counts of your selected data:')
        print(df['Gender'].dropna(axis=0).value_counts())
        print()
        # Display earliest, most recent, and most common year of birth
        print('Earliest Year of Birth:',
                int(min(df['Birth Year'].dropna(axis=0))))
        print('Latest Year of Birth:',
                int(max(df['Birth Year'].dropna(axis=0))))
        print('Most Common Year/s of Birth:',
                list(df['Birth Year'].dropna(axis=0).mode()))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Hmmm, looks like some data is missing. Please call 555-555-5555')
    #show_raw_data()

print(user_stats(df))


###########################################################



def reset_user_input():
    global city_input
    global month_input
    global raw_day_input
    global valid_day_input

    city_input = 'x'
    month_input = 'x'
    raw_day_input = []
    valid_day_input = []


def main():
    print('\n\n\n')
    print('Thanks for using our program!')
    u = input('Would you like to restart? ')
    if u == 'yes':
        print(reset_user_input())
        print(get_filters())
        print(load_data(city_input, month_input, valid_day_input))
        print(time_stats(df))
        print(station_stats(df))
        print(trip_duration_stats(df))
        print(user_stats(df))
        print(main())



if __name__ == "__main__":
	main()
