import requests
from datetime import datetime

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
  time = time[0:5]
  return time

def fetch_next_race():
  response = requests.get('https://api.jolpi.ca/ergast/f1/current/next/races')
  if response.status_code == 200:
    data = response.json()
    raceInfo = {
      "location": data['MRData']['RaceTable']['Races'][0]['Circuit']['circuitName'],
      "country": data['MRData']['RaceTable']['Races'][0]['Circuit']['Location']['country'],
      "fp1Date": format_date(data['MRData']['RaceTable']['Races'][0]['FirstPractice']['date']),
      "fp2Date": format_date(data['MRData']['RaceTable']['Races'][0]['SecondPractice']['date']),
      "fp3Date": format_date(data['MRData']['RaceTable']['Races'][0]['ThirdPractice']['date']),
      "qualifyingDate": format_date(data['MRData']['RaceTable']['Races'][0]['Qualifying']['date']),
      "raceDate": format_date(data['MRData']['RaceTable']['Races'][0]['date']),
      "fp1Time": format_time(data['MRData']['RaceTable']['Races'][0]['FirstPractice']['time']),
      "fp2Time": format_time(data['MRData']['RaceTable']['Races'][0]['SecondPractice']['time']),
      "fp3Time": format_time(data['MRData']['RaceTable']['Races'][0]['ThirdPractice']['time']),
      "qualifyingTime": format_time(data['MRData']['RaceTable']['Races'][0]['Qualifying']['time']),
      "raceTime": format_time(data['MRData']['RaceTable']['Races'][0]['time'])
    }
  return raceInfo

fetch_next_race()

