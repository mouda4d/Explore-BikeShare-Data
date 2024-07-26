# US Bikeshare Data Analysis

This project explores the US bikeshare data from three cities: Chicago, New York City, and Washington. It allows users to filter the data by city, month, and day of the week to gain insights into the bikeshare usage.

## Project Structure

The main functions in this project are:

1. `get_filters()`: Asks the user to specify a city, month, and day to analyze.
2. `load_data(city, month, day)`: Loads data for the specified city and filters by month and day if applicable.
3. `time_stats(df_list_filtered)`: Displays statistics on the most frequent times of travel.
4. `station_stats(df_list_filtered)`: Displays statistics on the most popular stations and trip.
5. `trip_duration_stats(df_list_filtered)`: Displays statistics on the total and average trip duration.
6. `user_stats(df_list_filtered)`: Displays statistics on bikeshare users.
7. `raw_data(df_list_filtered)`: Allows the user to see raw data in chunks of 5 rows.
8. `main()`: The main function that ties all the functionalities together.

## How to Run

To run the project, ensure you have the necessary CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as the script. Then execute the script:

```bash
python bikeshare.py
