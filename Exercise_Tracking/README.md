
# Exercise Tracker with Nutritionix and Sheety

This app tracks your daily exercises, calculates calories burned using the Nutritionix API, and logs the results into a Google Sheet using Sheety API.

## Features

- Takes natural language input of exercises (e.g. "ran 3 km and cycled 30 minutes")
- Calculates duration and calories using Nutritionix API
- Saves workout data to a Google Sheet via Sheety API

## Technologies

- Python
- Requests
- Nutritionix API
- Sheety API

## Requirements

- Environment variables:
  - `api_key` – your Nutritionix API key
  - `app_id` – your Nutritionix App ID
  - `sheety_token` – your Sheety authentication token

## How to Run

```bash
python exercise_tracker.py
