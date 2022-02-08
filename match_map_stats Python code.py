import pandas as pd
import sqlite3

#   Note: before importing the data I added column match_loser in
#   excel and removed team_one_name as well as team_two_name

#   Imports OWL Match Map Stats dataset from my SQL database
database = r'C:\Users\Max\Google Drive\Data\SQL Database\Scrying Pool.db'
conn = sqlite3.connect(database)

OWL_MMS = pd.read_sql('select * from OWL_Match_Map_Stats_Raw', con=conn)
conn.close()

#   Corrects column spelling errors, 'perecent' -> 'percent'
OWL_MMS = OWL_MMS.rename(columns={'attacker_control_perecent':'attacker_control_percent',
                                  'defender_control_perecent':'defender_control_percent'})

#   Creates and adds 'final_map_score' column to our dataframe
finalMapScore = OWL_MMS.winning_team_final_map_score.astype('str') + ' - ' + \
                OWL_MMS.losing_team_final_map_score.astype('str')
OWL_MMS.insert(14, 'final_map_score', finalMapScore)



#   Converts 'round_start_time' to datetime dtype
OWL_MMS.round_start_time = pd.to_datetime(OWL_MMS.round_start_time, 
                                          errors='coerce')
OWL_MMS.round_end_time = pd.to_datetime(OWL_MMS.round_end_time, 
                                          errors='coerce')


#   Removes excess portions of string in stage and adds year the stage took place
OWL_MMS.stage = OWL_MMS.stage.str.replace(' - Title Matches', '')
OWL_MMS.stage = OWL_MMS.stage.str.replace(' Title Matches', '')
OWL_MMS.stage = OWL_MMS.stage.str.replace('Overwatch League - ', '2018 ')
OWL_MMS.stage = OWL_MMS.stage.str.replace('Overwatch League Inaugural Season Championship', '2018 Playoffs')
OWL_MMS.stage = OWL_MMS.stage.str.replace('Overwatch League S', '2019 S')
OWL_MMS.stage = OWL_MMS.stage.str.replace('Overwatch League ', '')
OWL_MMS.stage = OWL_MMS.stage.str.replace('OWL ', '')


#   Converts columns to int dtype
for col in ['winning_team_final_map_score', 'losing_team_final_map_score', 
            'attacker_round_end_score', 'defender_round_end_score']:
    OWL_MMS[col] = OWL_MMS[col].astype('int')
    
    
#   Converts columns to float dtype
for col in ['attacker_payload_distance', 'defender_payload_distance',
            'attacker_time_banked', 'defender_time_banked']:
    OWL_MMS[col] = OWL_MMS[col].astype('float')


#   Converts columns to float dtype w/ coercion
OWL_MMS.defender_control_percent = pd.to_numeric(OWL_MMS.defender_control_percent,
                                                 errors='coerce')

OWL_MMS.attacker_control_percent = pd.to_numeric(OWL_MMS.attacker_control_percent,
                                                 errors='coerce')


#   Converts columns to category dtype
for col in ['stage', 'match_id', 'game_number', 'match_winner', 
            'match_loser', 'map_winner', 'map_loser', 'map_name', 
            'map_round', 'control_round_name', 'attacker', 
            'defender', 'final_map_score']:
    OWL_MMS[col] = OWL_MMS[col].astype('category')
    
    
#   Creates a new column round_length and converts it to string
roundLengthSeries = OWL_MMS.round_end_time - OWL_MMS.round_start_time
OWL_MMS.insert(2, 'round_length', roundLengthSeries)
OWL_MMS.round_length = OWL_MMS.round_length.astype('string')

#   Commented out as I've already uploaded a copy to my SQL database
#   Exports table to SQL database
# conn = sqlite3.connect(database)
# OWL_MMS.to_sql(name='OWL_Match_Map_Stats', con=conn)
# conn.close()