import pandas as pd

data_series = pd.Series(['UCLA', 'UC Berkeley', 'UC Irvine',
                         'University of Central Florida', 'Rutgers University'])

states_dicts = [{'STATE': 'New Jersey', 'ABBREVIATION': 'NJ'},
                {'STATE': 'New York', 'ABBREVIATION': 'NY'}]

df = pd.DataFrame(
    {'Dynasty': ['Early Dynastic Period', 'Old Kingdom'],
     'Pharoh': ['Thinis', 'Memphis']
     }
)

