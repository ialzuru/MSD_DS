# MSD_DS
Data wrangling and cleaning of the Million Song Dataset for the Data Science class of Fall 2015. https://ufl.instructure.com/courses/320501/pages/introduction-to-data-science

The Millon Song Dataset (MSD) is available at http://labrosa.ee.columbia.edu/millionsong/

> The Million Song Dataset is a freely-available collection of audio features and metadata for a million contemporary popular music tracks.

> Its purposes are:

> 	* To encourage research on algorithms that scale to commercial sizes
> 	* To provide a reference dataset for evaluating research
> 	* As a shortcut alternative to creating a large dataset with APIs (e.g. The Echo Nest's)
> 	* To help new researchers get started in the MIR field


## Data Wrangling
The MSD is available for download at https://www.opensciencedatacloud.org/publicdata/million-song-dataset/
When it is extracted, the dataset occupies about 280 GB. It is in HDF5 format (https://www.hdfgroup.org/HDF5), and there is a file per song, that is to say 1 million files. Each file has the 54 fields described in the MSD documentation.

The original format is not so easy to manipulate and includes fields for segments and their musical characteristics that occupy the vast majority of the dataset.

This format was converted to text (fields separated by tab) and reduced to 22 fields:
1. track_id   
2. track_7digitalid   
3. title   
4. artist_id   
5. artist_7digitalid   
6. artist_name   
7. artist_hotttnesss   
8. artist_latitude   
9. artist_location   
10. artist_longitude   
11. danceability   
12. duration   
13. energy   
14. loudness   
15. release   
16. release_7digitalid   
17. song_hotttnesss   
18. song_id   
19. tempo   
20. time_signature   
21. time_signature_confidence   
22. year   

The conversion program is available at the **/wrangling** folder and is called convert.py. It translates to text all the MSD files found in a folder (and its subfolders) and writes the consolidated information in a text file.

The conversion script is an adaptation of the code provided by Thierry Bertin-Mahieux in his project: https://github.com/tbertinmahieux/MSongsDB

To execute the conversion script, download the code provided by Thierry Bertin-Mahieux, put the **convert.py** script in the folder PythonSrc, and execute the script using he following syntax:
>   python convert.py < src_folder > < dts_filename >

Using this script was converted the MSD dataset. The conversion can be found in the folder **/dataset**. The dataset is shared as 26 text files because of the github limitations and problems loading medium size files. The user can create a single file with a simple command: `cat *.txt > MSD.txt`


This conversion process reduced the dataset from 280 GB to 250 MB.

## Data Cleaning

Three fields were studied: Duration, Tempo, and Artist Location.
The outliers in each case were verified, while the artist location was normalized
and completed.
We also show some plots of the raw data for  duration, tempo, and artist location.

For the cleaning process of these 3 fields, please review the .md files of each correspondent subdirectory in the /cleaning folder.
