import requests
from datetime import datetime, timezone, timedelta

def format_month(month):
  match month:
    case '01':
      return 'January'
    case '02':
      return 'February'
    case '03':
      return 'March'
    case '04':
      return 'April'
    case '05':
      return 'May'
    case '06':
      return 'June'
    case '07':
      return 'July'
    case '08':
      return 'August'
    case '09':
      return 'September'
    case '10':
      return 'October'
    case '11':
      return 'November'
    case '12':
      return 'December'

def format_date(date):
  month = format_month(date[5:7])
  day = date[8:10]
  return f'{month} {day}'

def format_time(time):
  utc_time = datetime.strptime(time, '%H:%M:%SZ').replace(tzinfo=timezone.utc)

  # Convert to Eastern Standard Time (UTC-5)
  est_time = utc_time.astimezone(timezone(timedelta(hours=-4)))

  # Format to 12-hour time
  formatted_time = est_time.strftime('%I:%M %p')
  return formatted_time

def fetch_next_race():
  response = requests.get('https://api.jolpi.ca/ergast/f1/current/next/races')
  if response.status_code == 200:
    data = response.json()
    race = data['MRData']['RaceTable']['Races'][0]

    if 'Sprint' in race:
      raceInfo = {
        "season": race['season'],
        "location": race['Circuit']['circuitName'],
        "country": race['Circuit']['Location']['country'],
        "fp1_date": format_date(race['FirstPractice']['date']),
        "qualy_date": format_date(race['Qualifying']['date']),
        "sprint_date": format_date(race['Sprint']['date']),
        "sprint_qualy_date": format_date(race['SprintQualifying']['date']),
        "race_date": format_date(race['date']),
        "fp1_time": format_time(race['FirstPractice']['time']),
        "qualy_time": format_time(race['Qualifying']['time']),
        "sprint_time": format_time(race['Sprint']['time']),
        "sprint_qualy_time": format_time(race['SprintQualifying']['time']),
        "race_time": format_time(race['time'])
      }
    else:
      raceInfo = {
        "season": race['season'],
        "location": race['Circuit']['circuitName'],
        "country": race['Circuit']['Location']['country'],
        "fp1_date": format_date(race['FirstPractice']['date']),
        "fp2_date": format_date(race['SecondPractice']['date']),
        "fp3_date": format_date(race['ThirdPractice']['date']),
        "qualy_date": format_date(race['Qualifying']['date']),
        "race_date": format_date(race['date']),
        "fp1_time": format_time(race['FirstPractice']['time']),
        "fp2_time": format_time(race['SecondPractice']['time']),
        "fp3_time": format_time(race['ThirdPractice']['time']),
        "qualy_time": format_time(race['Qualifying']['time']),
        "race_time": format_time(race['time'])
      }
  return raceInfo


