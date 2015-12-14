#
# Done by: Icaro Alzuru
# December - 2015
#
# Whatever (copyright).

import os, sys
import pandas as pd

# ===================================================================================================
def usage():
    print '###################################################################################'
    print '                     M I L L I O N   S O N G   D A T A S E T'
    print 'usage:'
    print '    python read_MSD.py <msd_file> 10\n'
    print 'INPUTS:'
    print '    10         - number of rows to print (non required parameter, default = 10)'    
    print '    <msd_file> - text file with the following fields order: '
    print '        track_id, track_7digitalid, title, artist_id, artist_7digitalid,artist_name,'
    print '        artist_hotttnesss, artist_latitude, artist_location, artist_longitude, '
    print '        danceability, duration, energy, loudness, release, release_7digitalid, '
    print '        song_hotttnesss, song_id, tempo, time_signature, time_signature_confidence,'
    print '        year'
    print '###################################################################################\n'
    sys.exit()
    
# ===================================================================================================
def input_validation(argv):
    if (len(argv) < 2) or (len(argv) > 3):
        usage()
        
    filename = argv[1]
    if ( not os.path.isfile(filename)):
        print("Error: File %s was not found\n" % (filename))
        usage()
    
    n = 10
    if len(argv) == 3:
        if argv[2].isdigit():
            n = int(argv[2])
            if n < 1:
                print 'Error: Invalid number of rows\n'
                usage()
        else:
            print 'Error: The second parameter must be a number\n'
            usage()
            
    return filename, n

# ===================================================================================================
if __name__ == '__main__':
    filename, n = input_validation(sys.argv)
    df = pd.read_csv(filename, sep='\t', header=None, names=['track_id', 'track_7digitalid', 'title', 'artist_id', 
        'artist_7digitalid','artist_name','artist_hotttnesss','artist_latitude','artist_location','artist_longitude',
        'danceability','duration','energy','loudness','release','release_7digitalid','song_hotttnesss','song_id', 
        'tempo','time_signature','time_signature_confidence','year'])
    print df.head(n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
