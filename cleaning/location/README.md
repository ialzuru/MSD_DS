## Artist Location Cleaning

The script to generate this statistics and graph is location.py, which is found in
this same folder.

### Basic statistics for the Artist Location field:

There are **487129 null values** of the 1 million songs (almost half).

Obtaining the artist location is difficult because there is no standard format, some examples of location that we can find are:

Some artist_location values | Format
--------------------------- | ------
Chicago, IL  | City < comma > State_Abbreviation    (Country = USA)
New Jersey  | State   (Country = USA)
Sassuolo, Italy  | City < comma > Country
CANADA - Ontario | Country < hyphen > State
Queens, NY  | Borough < comma >  State_Abbreviation
Burlington, Ontario, Canada  | City < comma >  State < comma >  Country
CP3  | (Invalid location)
UK - England - London  | State_Abbreviation < hyphen > Country < hyphen > City
Tokyo/Japan  | City < slash > Country
Jerez De La Frontera (Cádiz) | City < open_parenthesis > City (Spanish) < close_parenthesis >

The cleaning process was divided in three steps:
1. It was generated a new file: location_result.txt with the artist_id, state, and country.
In order to determine state and country values was used the artist_location column of the original
MSD. For this step were used lists of the countries of the world and the states of USA.   
2. The duplicated rows were eliminated
3. Some statistics were generated

The 10 countries with more artists in the MSD:

Country | # Artists
------- | ---------
United States | 6572
England | 1075
Canada | 259
Germany | 213
Australia | 121
France | 118
Sweden | 102
Scotland | 94
Jamaica | 94
Italy | 83

The 10 states of USA with more artists in the MSD:

State | # Artists
------- | ---------
California | 1072
New York | 910
Texas | 436
Illinois | 370
Pennsylvania | 282
Tennessee | 263
Michigan | 260
Ohio | 231
Florida | 206
Louisiana | 195

The 10 countries with more songs in the MSD:

Country | # Songs
------- | ---------
United States | 247901
England | 46698
Canada | 8650
Germany | 7770
Jamaica | 4713
France | 4486
Scotland | 4380
Australia | 3998
Sweden | 3658
Italy | 3139

The 10 states of USA with more songs in the MSD:

State | # Songs
------- | ---------
California | 40243
New York | 34490
Texas | 16099
Illinois | 13292
Tennessee | 11096
Pennsylvania | 10549
Michigan | 9745
Mississippi | 9064
Ohio | 8640
Louisiana | 8100


This cleaning process can be extended and improved to cover a bigger number of artists
and songs when considering more cases of identification of countries and states.



**Icaro Alzuru**
December - 2015
