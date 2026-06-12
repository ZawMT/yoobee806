## Regression Activities (Predicting Continuous Numbers)
How AI predicts continuous, changing numbers, like tracking how travel times rise and fall based on traffic conditions.

### Section 1: Regression Activities
#### Activity 1: Balancing the Past vs. the Present
**The Task**: Look at the Alpha slider in Column E. Tell them to change the values to 1.0 (purely live data) for some roads, and 0.0 (purely historical data) for others.
**The Lesson**: The Actual Travel Time target changes instantly. Is it better for a navigation app to only look at what's happening this exact second, or does it need historical patterns to make a good guess?

#### Activity 2: The "Too Good to Be True" Accuracy Check
**The Task**: Show students the R Square score of 0.999 on the summary tab. Explain that this score is like a grade from 0 to 1 on how well the AI guesses.
**The Lesson**: Trust a financial advisor who claims they can predict the stock market with 99.9% accuracy. A crucial real-world concept: when a model looks absolutely perfect, it usually means it just memorized the data instead of actually learning how to handle new situations.

#### Activity 3: Spotting the Speed Limit Flaw
**The Task**: Find the BD (School) row. Point out how the density (Estimated Rho) is incredibly high (174), forcing the travel time up to 118 seconds.
**The Lesson**: If a road gets completely jammed, do cars just slow down, or do they even move slower than a human walking? This shows them why simple formulas struggle with real-world extremes.

#### Activity 4: The Impact of Road Length
**The Task**: Compare GB and HM. Both have the exact same traffic density (75), but HM takes much longer (52 seconds vs. 51 seconds).
**The Lesson**: Find the culprit column (Distance). To see that a regression model has to weigh multiple pieces of the puzzle at the same time to get the final prediction right.

#### Activity 5: Finding the Model's "Blunder"
**The Task**: Pick a road and manually change its Distance to something massive, like 5 km, while keeping traffic light.
**The Lesson**: The travel time shoots through the roof. How data errors or typos can instantly break a prediction model, showing them why cleaning data matters just as much as the math itself.


### Section 2: Standard Classification Activities (Sorting Into Buckets)
In these activities, we stop looking at exact seconds. Instead, students practice grouping roads into simple, clear categories: Clear (0) or Jammed (1).
#### Activity 1: Testing the Tipping Point
**The Task**: Your spreadsheet uses a simple rule: if traffic density goes over 70, it's a bottleneck. Have students change a clear road's DP (currently 65) to 69. Then have them change it to 71.
**The Lesson**: Watch the Congestion Status flip from 0 to 1. How basic classification works — it doesn't care how close you are to the edge; it only cares the moment you cross the line.

#### Activity 2: The "False Alarm" Debate
**The Task**: Look at row FH. It has a safe density of 55, but because it's a longer road, its travel time is 74 seconds, which is higher than the jammed GB road (51 seconds). Yet, the model labels FH as "Clear (0)".
**The Lesson**: "If you were a driver, would you be annoyed if your app said a road was 'Clear', but you ended up sitting there for a long time?" Introduces "False Positives" and "False Negatives" in a completely practical way.

#### Activity 3: Shifting the Goalposts
**The Task**: Change the threshold in the formula from >70 to >50 across the entire column.
**The Lesson**: Suddenly, almost the whole sheet turns red! The human who sets the rules controls how sensitive the AI is. If you set the bar too low, you end up triggering alarms constantly.

#### Activity 4: Grouping the Neighborhoods
**The Task**: Count how many 0s and 1s they have in total on the sheet.
**The Lesson**: Have way more clear roads than jammed ones. Introduces "Class Imbalance" — a common problem where an AI gets really good at recognizing one group simply because it sees it way more often.

#### Activity 5: The Rush Hour Chaos
**The Task**: That school just let out, and every single road's density has suddenly spiked by 25 points. Have them update the sheet.
**The Lesson**: Watch the status column completely change. How classification models can be used to monitor systems in real time, shifting instantly as the surrounding environment changes.