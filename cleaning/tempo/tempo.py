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
    print '    python tempo.py <msd_file>\n'
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
    #     T   E   M   P   O  

    # ----------------- STATISTICS ----------------------------------------------------------
    tempo = df['tempo'].to_frame()
    tempo.columns = ['tempo']
    print("Mean: %.2f seconds" % round(tempo.mean(0), 2))
    print("Standard Deviation: %.2f seconds" % round(tempo.std(0), 2))
    print("Median: %.2f seconds" % round(tempo.median(0), 2))
    print("Maximum: %.2f seconds" % round(tempo.max(0), 2))
    print("Minimum: %.2f seconds" % round(tempo.min(0), 2))
    
    # ----------------- OUTLIERS and UTILS ----------------------------------------------------------
  
#     print df['tempo'].head(20)
#     t2 = df[['track_id','title','artist_name','tempo','duration']]
#     print t2.sort_values(by='tempo', ascending=False).head(10)
#     print t2[ t2['tempo'] == 0 ].count()
#     t3 = t2[ t2['tempo'] != 0 ]
#     print t3.sort_values(by='tempo', ascending=True).head(10)
#     print t2[ t2['tempo'].map(lambda x: x>200 ) ]

    # ----------------- HISTOGRAM GRAPH -----------------------------------------------------
    d = df['tempo'].map(lambda x: round(x))
    #print d.value_counts()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(d, d.max(0))
    ax.set_xticks((0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270))
    ax.set_xticklabels(('0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200', '210', '220', '230', '240', '250', '260', '270'))
    ax.set_title('Songs "tempo"')
    ax.set_xlabel("bpm")
    ax.set_ylabel("# songs")
    ax.axis([0, 270, 0, 24000])
    plt.show()

