## Section 3: Support Vector Machine (SVM) Activities (The Smart Boundary)
Instead of just drawing a random line, an SVM tries to build a wide, safe "buffer street" (the margin) between our groups.

## Activity 1: Spotting the "VIP Roads"
The Task: Look at the rows: GB, DP, HM, and NP. Note how their distance from the center line is exactly 5 or -5.
The Lesson: Explain that these are the Support Vectors. They sit right on the curbs of our buffer street. SVM completely ignores the roads sitting deep in the safe zone or deep in the traffic jam, focusing entirely on the ones closest to the edge.

## Activity 2: Messing with the Neighbors
The Task: Go to a road like MN (-25) and change its density so its distance becomes -10. Did the yellow rows change? No.
The Lesson: This proves the core philosophy of an SVM: points deep inside their own zones don't affect the boundary line at all. The model stays completely stable.

## Activity 3: Testing the Street Structural Integrity
The Task: Now, change one of the roads, like moving GB from 75 down to 72.
The Lesson: The distance column shrink to 2. This proves that if a Support Vector moves, it actively encroaches on the safety buffer, threatening to warp the entire model's decision boundary.

## Activity 4: Measuring the Street Width
The Task: Find the highest number (+5) and the lowest number (-5). Calculate the total gap between them (5 - (-5) = 10).
The Lesson: In an SVM, the goal is always to make this street as wide as possible so the system has a safe buffer zone to prevent sorting mistakes.

## Activity 5: Designing a Smart Road Sign
The Task: Go to Column J and type in a rule that talks to drivers based on their SVM position:
=IF(I2 > 5, "ALERT: Divert Traffic", "All Clear")
The Lesson: This ties the math back to real life. A geometric distance calculation instantly turns into an automated road sign that routes cars away from upcoming bottlenecks in a smart city.