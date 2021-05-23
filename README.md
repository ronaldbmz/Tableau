# Tableau

## Phenomenon-1: 
### Assumption/ Ideal Behavior: 
During the day, as the number of rides increases and reaches up to the peak, the increment in the number of rides should attribute to increase in both female and male riders.
### Anomaly Observed: 
Proportion of female riders remains almost same throughout the day.
### Analysis:
1.	First, we check the ratio of female to male riders across the months to understand the distribution of gender. We observe that gender ratio (F/M) of riders remains overall same throughout the past 6 months.
2.	Next, we analyze the distribution of number of rides across the hours of day to confirm about peak hours
3.	At last, we check the percentage split between female and male rides across hours of day and notice that female rider’s percentage remains almost the same irrespective of number of rides being increased at peak hours

## Phenomenon-2: 
### Assumption/ Ideal Behavior: 
Number of rides in the early morning’s (between 6am to 9am) of warmer months like Mar & Apr should be higher than cold months (Dec, Jan & Feb).
### Anomaly Observed: 
Number of rides between 5am to 9am of Mar & Apr are quite lower than Dec, Jan & Feb. This could be because riders prefer to walk/jog in early morning hours in warm months.
### Analysis:
1.	First, we build a line chart to see the trend of number of rides across hours of day for each month and observe that between 5am to 9am number of rides are quite lower in Mar & Apr compared to colder months.
2.	Next, through heatmap we analyze the number of bikes were in use between 5am to 9am across each month and notice the same trend that there were very less bikes used for Mar & Apr.
3.	At last, to confirm the anomaly mentioned above, we build an area chart to see to trip duration between 5am to 9am for all months to make sure that a smaller number of rides were not due to long trip duration. We notice that there is no significant difference between the trip duration in month of Dec or Apr.
This confirms our anomaly that there might be possibility that because riders prefer to walk/jog in early morning hours in warm months.

## City Official Dynamic Map:
Details: In the map, we are showing the number of rides started from each station along with the most popular station with highest number of rides to start and end a journey. Also, different layers of map are being used to show the zip codes and region boundaries.

### Trends: 
1. 3141 (1 Ave & E 68 St) is the most popular bike station with the highest number of starting and ending of bike rides
2. We observe that number of bike rides from each station gradually decreases from Nov 20 to Feb 21 and then start increasing from Mar 21 to Apr 21
![image](https://user-images.githubusercontent.com/75644803/119278423-879da700-bc25-11eb-8386-be83459cd323.png)
