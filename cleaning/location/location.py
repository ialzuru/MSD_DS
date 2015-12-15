#
# Done by: Icaro Alzuru
# December - 2015
#
# Notes: I was working with the GeoLite2 list of countries, but there are several missing countries (England, Wales, etc.)
#        The program generates a file called location_result.txt, where it is stored: artist_id, state, country for the rows 
#        of the input file. Some statistics are generated when joining the cleaned data with the original MSD.
#
# Whatever (copyright).

import os, sys
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from string import lower
#from pip import locations

# ===================================================================================================
def usage():
    print '###################################################################################'
    print '                     M I L L I O N   S O N G   D A T A S E T'
    print 'usage:'
    print '    python location.py <msd_file>\n'
    print 'INPUTS:'
    print '    <msd_file> - MSD text file with the following fields order: '
    print '        track_id, track_7digitalid, title, artist_id, artist_7digitalid,artist_name,'
    print '        artist_hotttnesss, artist_latitude, artist_location, artist_longitude, '
    print '        danceability, duration, energy, loudness, release, release_7digitalid, '
    print '        song_hotttnesss, song_id, tempo, time_signature, time_signature_confidence,'
    print '        year'
    print '###################################################################################\n'
    sys.exit()
    
# ===================================================================================================
def input_validation(argv):
    if (len(argv) != 2):
        usage()
        
    filename = argv[1]
    if ( not os.path.isfile(filename)):
        print("Error: File %s was not found\n" % (filename))
        usage()

    return filename

# ===================================================================================================
if __name__ == '__main__':
    filename = input_validation(sys.argv)
    df = pd.read_csv(filename, sep='\t', header=None, names=['track_id', 'track_7digitalid', 'title', 'artist_id', 
        'artist_7digitalid','artist_name','artist_hotttnesss','artist_latitude','artist_location','artist_longitude',
        'danceability','duration','energy','loudness','release','release_7digitalid','song_hotttnesss','song_id', 
        'tempo','time_signature','time_signature_confidence','year']) 
      
#     #print filename, df.shape[0], "rows"             # 1000000 rows
    ##########################################################################################################
    #------------------------ 'artist_location'
    # print df['artist_location'].value_counts()
    # NaN:
    # print df['artist_location'].isnull().sum()
    
    states = ['alabama','alaska','arizona','arkansas','california','colorado','connecticut','delaware','florida','georgia','hawaii','idaho',
              'illinois','indiana','iowa','kansas','kentucky','louisiana','maine','maryland','massachusetts','michigan','minnesota','mississippi',
              'missouri','montana','nebraska','nevada','new hampshire','new jersey','new mexico','new york','north carolina','north dakota',
              'ohio','oklahoma','oregon','pennsylvania','rhode island','south carolina','south dakota','tennessee','texas','utah',
              'vermont','virginia','washington','west virginia','wisconsin','wyoming']
    
    states_abb = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN',
                  'MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA',
                  'WA','WV','WI','WY']
    
    country = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua & Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan',
               'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia & Herzegovina','Botswana',
               'Brazil','Brunei Darussalam','Bulgaria','Burkina Faso','Burma','Myanmar','Burundi','Cambodia','Cameroon','Canada','Cape Verde',
               'Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo','Democratic Republic of the Congo','Congo','Costa Rica',
               'Cote d Ivoire','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','East Timor',
               'Egypt','El Salvador','England','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','The Gambia',
               'Georgia','Germany','Ghana','Great Britain','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras',
               'Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya',
               'Kiribati','North Korea','South Korea','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya',
               'Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands',
               'Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia',
               'Nauru','Nepal','The Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Northern Ireland','Oman','Pakistan','Palau',
               'Palestinian State','Panama','Papua New Guinea','Paraguay','Peru','The Philippines','Poland','Portugal','Qatar','Romania','Russia',
               'Rwanda','St. Kitts & Nevis','St. Lucia','St. Vincent & The Grenadines','Samoa','San Marino','Sao Tome & Principe','Saudi Arabia',
               'Scotland','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa',
               'Spain','Sri Lanka','Sudan','South Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania',
               'Thailand','Togo','Tonga','Trinidad & Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates',
               'United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City (Holy See)','Venezuela','Vietnam','Western Sahara',
               'Wales','Yemen','Zaire','Zambia','Zimbabwe']
    
    #########################################################################################################################################################
    # 1st Step: location_result.txt 
     
#     t1 = df[[ 'artist_id', 'artist_location' ]]
#     f = open("location_result.txt", 'w')
#        
#     for idx, row in t1.iterrows():
#         loc_lower = str(row['artist_location']).lower()
#         if loc_lower != "nan":                                              # NULL ?
#             if ',' in loc_lower:                                            # Separated by ,
#                 last_s = loc_lower.split(",")[-1]
#                 last_s = last_s.strip()
#                 last_s_upper = last_s.upper()
#   
#                 try:
#                     idx = states_abb.index(last_s_upper)
#                     f.write( str(row['artist_id']) + ',' + states[idx].title() + ',' + 'United States\n' )
#                 except ValueError:                                          # No City, ST format
#                     if last_s.title() in country:                           # format <something>, Country
#                         f.write( str(row['artist_id']) + ',,' + last_s.title() + '\n')
#                     else:
#                         try:
#                             idx = states.index(last_s)                      # format <something>, State     (USA)
#                             f.write( str(row['artist_id']) + ',' + last_s.title() + ',' + 'United States\n' )
#                         except ValueError:                                  # No <something>, State format
#                             continue
#       
#     f.close()            

    ########################################################################################################################################################
    # 2nd Step: Getting a single location by artist_id
    
#     loc = pd.read_csv("location_result.txt", sep=',', header=None, names=['artist_id', 'state', 'country'])
#     print "location_result.txt: ", loc.shape[0], "rows"                 # 314880 rows
#  
#     loc_unique = loc.drop_duplicates(['artist_id', 'state', 'country'], keep='first')
#     print "unique_result.txt: ", loc_unique.shape[0], "rows"            # 9490 rows
#     loc_unique.to_csv("unique_result.txt", index=False)
#     print loc_unique[ loc_unique.duplicated(['artist_id', 'state', 'country']) ]    # Empty DataFrame 
#     
    ########################################################################################################################################################
    # 3rd step: Statistics
    loc_unique = pd.read_csv("unique_result.txt", sep=',', header=None, names=['artist_id', 'state', 'country'])
    #print loc_unique[ 'country' ].value_counts()
    #print loc_unique[ 'state' ].value_counts()
    song_loc = df.merge(loc_unique, on = 'artist_id')
    #print song_loc[ 'country' ].value_counts()
    print song_loc[ 'state' ].value_counts()
    
    
    
    
    
    
    
    
    
    
    
    