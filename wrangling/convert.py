"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu

Modified by:
Icaro Alzuru (2015) University of Florida
ialzuru@gmail.com


Code to quickly see the content of an HDF5 file.

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.


Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import hdf5_getters
import numpy as np


def die_with_usage():
    """ HELP MENU """
    print 'convert.py: Converts to text all the MSD files available in a directory and its subdirectories'
	print ''
    print 'usage:'
    print '   python convert.py <src_folder> <dts_filename'
	print ''
    sys.exit(0)


if __name__ == '__main__':
    """ MAIN """

    # help menu
    if len(sys.argv) < 2:
        die_with_usage()

    # flags
    summary = False
    while True:
        if sys.argv[1] == '-summary':
            summary = True
        else:
            break
        sys.argv.pop(1)

    # get params
    hdf5path = sys.argv[1]
    onegetter = ''
    summary = True
    filename = sys.argv[2]
    
    # sanity check
    if not os.path.isdir(hdf5path):
        print 'ERROR: file', hdf5path, 'does not exist.'
        sys.exit(0)
        
    sel_get = ['get_track_id','get_track_7digitalid','get_title','get_artist_id','get_artist_7digitalid','get_artist_name','get_artist_hotttnesss','get_artist_latitude','get_artist_location','get_artist_longitude','get_danceability','get_duration','get_energy','get_loudness','get_release','get_release_7digitalid','get_song_hotttnesss','get_song_id','get_tempo','get_time_signature','get_time_signature_confidence','get_year']
    f = open(filename, "w")
    i=1
    for root, dirs, files in os.walk(hdf5path):
        for file in files:
            if file.endswith(".h5"):
                filename = os.path.join(root, file)
                h5 = hdf5_getters.open_h5_file_read(filename)
                numSongs = hdf5_getters.get_num_songs(h5)
    
                if numSongs>1:
                    print "Error: More than one song is included in file ", filename
                    f.close()
                    sys.exit(0)
                
                getters = filter(lambda x: x[:4] == 'get_', hdf5_getters.__dict__.keys())
                getters.remove("get_num_songs") # special case
                getters = np.sort(getters)
    
                dict_get ={'get_track_id':'','get_track_7digitalid':'','get_title':'','get_artist_id':'','get_artist_7digitalid':'','get_artist_name':'','get_artist_hotttnesss':'','get_artist_latitude':'','get_artist_location':'','get_artist_longitude':'','get_danceability':'','get_duration':'','get_energy':'','get_loudness':'','get_release':'','get_release_7digitalid':'','get_song_hotttnesss':'','get_song_id':'','get_tempo':'','get_time_signature':'','get_time_signature_confidence':'','get_year':''}
                # print them
                for getter in getters:
                	if getter in sel_get:
                		try:
                		    dict_get[getter] = hdf5_getters.__getattribute__(getter)(h5,songidx)
                		except AttributeError, e:
                		    continue
                
                f.write(str(dict_get['get_track_id']) + '\t')
                f.write(str(dict_get['get_track_7digitalid']) + '\t')
                f.write(str(dict_get['get_title']) + '\t')
                f.write(str(dict_get['get_artist_id']) + '\t')
                f.write(str(dict_get['get_artist_7digitalid']) + '\t')
                f.write(str(dict_get['get_artist_name']) + '\t')
                f.write(str(dict_get['get_artist_hotttnesss']) + '\t')
                f.write(str(dict_get['get_artist_latitude']) + '\t' )
                f.write(str(dict_get['get_artist_location']) + '\t' )
                f.write(str(dict_get['get_artist_longitude']) + '\t')
                f.write(str(dict_get['get_danceability']) + '\t' )
                f.write(str(dict_get['get_duration']) + '\t' )
                f.write(str(dict_get['get_energy']) + '\t' )
                f.write(str(dict_get['get_loudness']) + '\t' )
                f.write(str(dict_get['get_release']) + '\t' )
                f.write(str(dict_get['get_release_7digitalid']) + '\t')
                f.write(str(dict_get['get_song_hotttnesss']) + '\t')
                f.write(str(dict_get['get_song_id']) + '\t' )
                f.write(str(dict_get['get_tempo']) + '\t' )
                f.write(str(dict_get['get_time_signature']) + '\t')
                f.write(str(dict_get['get_time_signature_confidence']) + '\t' )
                f.write(str(dict_get['get_year']) + '\n')

                h5.close()
                i = i + 1
                if i == 2:
                    f.close()
                    sys.exit(1)
                
    f.close()
