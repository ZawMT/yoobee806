## Decision Tree Activities

### Activity 1: The Gatekeeper's Tipping Point
The Action: Go to road DP (Row 5) or NP (Row 9) which currently sit at an Estimated Rho of 65. Slowly increase their Current Rho values until the Estimated Rho hits exactly 70, and then 71.
What to Observe: cell J5 or J9 and the automated counter at the bottom in Cell N14.
Question: What is the exact mathematical difference in how the Decision Tree treats a road with a density of 70 versus 71? Does it show any nuance, or is it a hard split?

### Activity 2: The Cascading Shift (Watching the Leaves Change)
The Action: Manually change the traffic values for three clear roads simultaneously (FG, DP, and FH) so that their Estimated Rho values all cross above 70.
What to Observe: Look directly at your automated visual tree structure down in cells L14 and N14.
The Question: How do the terminal 'Leaf Nodes' at the bottom of our tree react to sudden, widespread gridlock? How does this automated counting feature help a [text continues on next page]

### Activity 3: The Blind Spot of a Single Feature
The Action: Look at road BD (School). It has a massive traffic density of 174. Now look at road GB, which has a density of 75. Both are labeled "Congested" by the tree.
What to Observe: Notice that the Decision Tree treats the absolute gridlock of a school zone (+104 over the line) exactly the same as a road that is barely over the line (+5 over the line).
The Question: Because this tree only asks a single 'Yes/No' question, what critical information about the severity of traffic is it completely missing? How could a single-layered tree lead to emergency vehicles being routed incorrectly?

### Activity 4: Shifting the Logic Boundary
The Action: Click on cell J2. Go up to the Excel formula bar and manually change the gating threshold from > 70 to > 50:
Excel
=IF(F2 > 50, "Congested", "Clear")
Flash-fill this new rule down to cell J9, and manually update your question text in cell M12 to read: Is Estimated Rho > 50?
What to Observe: Count how many roads instantly turn red and get routed to the "Congested" leaf node.
The Question: By lowering the tree's threshold from 70 to 50, did we make our navigation application more conservative or more aggressive? What would happen to driver trust if our app started flagging minor, everyday traffic as a major crisis?

### Activity 5: Decision Trees vs. Support Vector Machines (The Great Debate)
The Action: Open your SVM tab and your DT tab side-by-side on your screen. Compare Column I on the SVM tab (Distance from Boundary) with Column J on the DT tab (DT Output).
What to Observe: Notice how the SVM calculates a continuous, variable distance score for every road, while the Decision Tree only spits out fixed, binary group labels.
The Question: If you were designing a self-driving car routing system, when would you want to use a strict, fast, rule-based flowchart (Decision Tree), and when would you want a model that calculates a soft, protective safety buffer corridor (SVM)?