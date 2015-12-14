#
# Done by: Icaro Alzuru
# December - 2015
#
# Whatever (copyright).

import os, sys
import pandas as pd
import matplotlib.pyplot as plt

# ===================================================================================================
def usage():
    print '###################################################################################'
    print '                     M I L L I O N   S O N G   D A T A S E T'
    print 'usage:'
    print '    python duration.py <msd_file>\n'
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
    #      D   U   R   A   T   I   O   N
    
    # -------------------- STATISTICS ----------------------------------------------------------
    duration = df['duration'].to_frame()
    duration.columns = ['duration']
    print("Mean: %.2f seconds" % round(duration.mean(0), 2))
    print("Standard Deviation: %.2f seconds" % round(duration.std(0), 2))
    print("Median: %.2f seconds" % round(duration.median(0), 2))
    print("Maximum: %.2f seconds" % round(duration.max(0), 2))
    print("Minimum: %.2f seconds" % round(duration.min(0), 2))
 
    # ----------------- OUTLIERS ------------------------------------------------------------
#     t1 = df[['track_id','title','artist_name','duration']]
#     print t1[ t1['duration'] < 30.0 ] #.count()
#     print t1[ t1['duration'] > 3000 ] #.count()
#     print t1.sort_values(by='duration', ascending=True).head(5)
#     print t1.sort_values(by='duration', ascending=False).head(5)
         
    # ----------------- HISTOGRAM GRAPH -----------------------------------------------------
    d = df['duration'].map(lambda x: round(x/60))
    #print d.value_counts()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(d, d.max(0))
    ax.set_xticks((0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5))
    ax.set_xticklabels(('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',))
    ax.set_title('Songs "duration"')
    ax.set_xlabel("minutes")
    ax.set_ylabel("# songs")
    ax.axis([0, 16, 0, 300000])
    plt.show()

    # ----------------- UTILS -----------------------------------------------------
    #print duration[ duration['duration'] > 1000 ]      
    #print duration.head(5)
    #print d.head(5)
