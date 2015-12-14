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


Icaro Alzuru
December - 2015