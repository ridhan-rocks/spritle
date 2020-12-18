# spritle
##Table of Contents
*[General Info](#general-info)
*[Algorithm](#algorithm)
*[Technologies](#technologies)
*[Sample Output](sample-output)

## General Info
This project allots seats to passengers in airplane according to a way in which seats are filled from left to right , aisle seats first followed by window seats, then followed by middle seats.
The number of passengers and Seat array is taken as input.

## Algorithm
*First we construct the seats using data given and print them .
*For filling aisle seats:
     Take the first row and start traversing it.
     While traversing , the first and last colums are ignored and only the corner seats of each block is filled.
     This same procedure applies to rows from top to bottom .And we retun the function saying "Aisle seats filled".
*For Filling Window Seats:
     Now ,we come back to first row .
     The first and last colums of the entire row is filled from left to right.Now we traverse the rows from top to bottom 
     A function is returned saying "window seats filled".
*For Filling Middle Seats:
     We identify the middle seats using loops .
     Now start filling them from left to rigt.
     Do the same for rows from top to bottom. Afunction is returned saying "middle seats filled".
     
##Technologies
* Python 3.9
*VS Code

## Sample Input/ Output:
#Input
* Number of passengers:30
*Seat Array:[[3, 2], [4, 3], [2, 3], [3, 4]]
#Output
+--+--+--+    +--+--+--+--+    +--+--+    +--+--+--+
|19|25|1 |    |2 |26|27|3 |    |4 |5 |    |6 |28|20|
+--+--+--+    +--+--+--+--+    +--+--+    +--+--+--+
|21|29|7 |    |8 |30|  |9 |    |10|11|    |12|  |22|
+--+--+--+    +--+--+--+--+    +--+--+    +--+--+--+
              |13|  |  |14|    |15|16|    |17|  |23|
              +--+--+--+--+    +--+--+    +--+--+--+
                                          |18|  |24|
                                          +--+--+--+
