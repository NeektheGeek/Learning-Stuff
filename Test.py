import random

state_dict = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little_Rock', 'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des_Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton_Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint_Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson_City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson_City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Sante_Fe', 'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma_City', 'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt_Lake_City', 'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

random.shuffle(states)
for state in states:
    answer = input("%s" %state)
    if answer == (state_dict[state]):
        print('Correct!')
    else:
        print('Wrong!')