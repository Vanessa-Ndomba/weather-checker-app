# South African Weather Forecast App

A beginner-friendly Python console application that displays the current weather for cities in South Africa using the OpenWeatherMap API.

## Overview

This project allows a user to enter the name of a South African city and view live weather information in a clear, formatted layout.

The app shows:

- weather condition
- temperature
- feels-like temperature
- humidity
- wind speed
- pressure
- extra weather details

It also includes input validation, API error handling, and a loop so the user can check multiple cities in one session.

## Features

- Check current weather for South African cities
- Display temperature in Celsius
- Show feels-like temperature
- Display humidity
- Display wind speed
- Display atmospheric pressure
- Convert weather descriptions into simple conditions with icons
- Handle empty input
- Handle invalid city names
- Handle invalid API key errors
- Handle network and timeout errors
- Allow the user to search again in a loop
- Accept both `yes` / `no` and `y` / `n` as valid responses

## How the Program Works

1. The user enters a South African city
2. The app formats the city name and adds the South Africa country code
3. A request is sent to the OpenWeatherMap API
4. The app reads and extracts weather data from the response
5. The weather information is displayed in a formatted output
6. The user is asked whether they want to check another city
7. The program repeats until the user chooses to exit


## Technologies Used

- Python 3
- `requests` library
- OpenWeatherMap API

## How to Run

Run the program from the terminal:

