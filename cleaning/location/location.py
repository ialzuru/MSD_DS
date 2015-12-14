#
# Done by: Icaro Alzuru
# December - 2015
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
    if (len(argv) < 1) or (len(argv) > 2):
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
     
    t1 = df[[ 'track_id', 'artist_location' ]]
    countries_file = pd.read_csv('GeoLite2-Country-Locations-en.csv', sep=',', header=0) 
    country = countries_file[[ 'country_name' ]]
     
    for idx, row in t1.iterrows():
        loc_lower = str(row['artist_location']).lower()
        if loc_lower != "nan":
            if ',' in loc_lower:
                s = loc_lower.split(",")[-1]
                s = s.strip()
                s_upper = s.upper()

                try:
                    idx = states_abb.index(s_upper)
                    print states[idx].title(), 'United States'
                except ValueError:
                    if 
                    print s_upper
            #else:
                

            
        #lowloc = str(row['artist_location']).lower()
         
        #if 'italy' in lowloc:
        #    print row 

    #print country

    #print t1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    