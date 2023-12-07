import os.path
# Data Handling Imports
import pandas as pd
import matplotlib.pyplot
import seaborn as sns

# Converting reviews scores into plottable data program
# Created by:   Rayan Arshed
# Created for:  Final Year Project in Computer Science

# Improvements since Prototype:
# CSV file now has the unique data in it, but the program can convert it to the scores needed to plot the data
# Very basic GUI added for simple error messages

# Improvements since Presentation:
# GUI expanded upon, runs indefinitely until exited
# Functions added to GUI; multiple graphs available to be outputted
# Also can output the scores for all the data values stored
# Some data type checking implemented to mitigate potential errors

# Pandas and Data Section

# Imports the CSV file into scoreFrame to save the data as a dataframe
# This is the start of the data handling in order to manipulate the data to make it plottable
# Finds the CSV file containing the scores, reads it and converts it to a Pandas Data frame named scoreFrame
CSV_File = os.path.join("Scores.csv")
scoreFrame = pd.read_csv(CSV_File)

# Initialises scoreValues (the titles of each column), averageScores (an array to be used later to hold the
# average scores), and totalGames (holds the calculated total of games)
scoreValues = []
averageScores = []
totalGames = int((len(scoreFrame.columns) - 1) / 2)

# Creation of the calculatedScores data frame (the Data Frame holding the calculated scores of the CSV file)
# Begins by assigning a list totalColumns the value of Date
# This list will be what defines the column headers for the Data Frame
totalColumns = ["Date"]
# For loop loops through the range of totalGames, eg will repeat 5 times if there are 5 games
for i in range(totalGames):
    # Appends to the totalColumns list the game + the number following it, so eg Game 1, Game 2, etc
    totalColumns.append("Game " + str(i + 1))
# Once the loop is done, the calculatedScores data frame is made, using totalColumns as the headers for each column
calculatedScores = pd.DataFrame([], columns=totalColumns)


# Calculated Scores function
# This function simply takes the values from the CSV file, and converts them into calculated ratio scores
def calculatedScoresCalculation():
    # Sets temporary array to be empty
    cScoreArray = []
    # Loops through the rows of the data frame
    for k in range(len(scoreFrame.values)):
        j = 1
        # Adds 2000 to the temp array, as the first column is the date, so this normalises the date
        cScoreArray.append(2000 + k)
        # While there are still game scores left to be processed
        while j < len(scoreFrame.values[k]):
            # Calculates the score by dividing the current value the pointer j is on by the one after
            # Story value / Gameplay value
            calculatedScore = scoreFrame.values[k][j] / scoreFrame.values[k][j + 1]
            # Appends the score to the end of the temp array, as Game 1
            cScoreArray.append(calculatedScore)
            # j is incremented by 2, and the process is repeated for however many games there are
            j += 2
        # After the while loop, the result in the temp array is added in a new row to the calculatedScores frame
        calculatedScores.loc[len(calculatedScores)] = cScoreArray
        # The temp array is reset to be empty, allowing for a new for loop pass to begin
        cScoreArray = []


# This function appends to the array scoreValues each column; this makes less code for graphing via an array later on
# Score Values holds the title for each column, so this essentially sets the title for each column to a different
# game title
# eg Game 1, Game 2... etc
def dateAxisCreation()
    for i in range(len(calculatedScores.values[1]) - 1):
        scoreValues.append(calculatedScores.columns[i + 1])


# Assigns the scoreDate variable to be the dates within the dataframe; this variable is used in graph creation
scoreDate = calculatedScores.columns[0]


# averageScoreCalculation is a function that simply calculates the average score per year
def averageScoreCalculation():
    # Begins a for loop through the calculatedScores dataframe
    for k in range(len(calculatedScores.values)):
        # Initialises the next two variables for use in the While loop
        j = 1
        averageValue = 0
        # While there are still values within this row to be added
        while j < len(calculatedScores.values[k]):
            # Add the values to the total and iterate
            averageValue = averageValue + calculatedScores.values[k][j]
            j += 1
        # Divide the total value by the total numbers, calculating the average value
        averageValue = averageValue / (j - 1)
        # Append the average value to the array to be plotted later
        averageScores.append(averageValue)


# Seaborn Section
# Starts by setting the theme of the graph
sns.set_theme(style="darkgrid")


# This function handles graph creation
# By using an array to hold every column of data, a while loop can be used to iterate through the frame
# and a new graph can be drawn by calling scoreValues[k-1]
# This function is necessary to keep code neat, otherwise, if there were 5 or more scores,
# 5 or more graph calls would be needed, instead of this single one function
def graphCreation():
    graphArray = []
    k = 0
    # While there are still values of data to be plotted within the Data Frame
    while k < len(calculatedScores.values[1]):
        # Begins the drawing of the scatter plot
        graphArray.append(sns.scatterplot(
            # Assigns the data to be used as the calculatedScores frame created and processed earlier
            data=calculatedScores,
            # Mapping the X and Y values; x is the date axis, y is the values for each row of the data frame
            x=scoreDate, y=scoreValues[k - 1], ci=None
        ))
        # Iterates to draw the next graph on top of the previous scatter plot
        k += 1


# Similar to graphCreation, except this is a simplified function to plot only a specific set of the data
def setgraphCreation(dataset):
    setGraph = sns.scatterplot(
        data=calculatedScores,
        x=scoreDate, y=scoreValues[dataset - 1]
    )


# The functions from before are called, the making of the graph is much neater this way
# calculatedScoresCalculation() calculates the scores from the CSV file and data frame
calculatedScoresCalculation()
# dateAxisCreation() is a simple function that just simplifies the creation of the date axis in the graph loop
dateAxisCreation()
# averageScoreCalculation() calculates the average from the calculatedScores dataframe
averageScoreCalculation()


# The graph for the averages is made after calculating the average scores
# This graph is a regplot (regression plot) while the others were scatter plots
# This is so that only a single regression line is represented, while the whole dataset can also be plotted on
# the same axis
def averageGraphCreation():
    AverageGraph = sns.regplot(
        # Assigns the data to be used as the calculatedScores created and processed earlier
        data=scoreFrame,
        # Mapping the X and Y values; x is the date axis, y is the average scores
        # This X value is the same as the previous graphs to map the axis onto each other
        x=scoreDate, y=averageScores
    )
    # Setting the labels for the axis on the graph for Years and Scores
    AverageGraph.set(xlabel='Years', ylabel='Scores')


# Output and GUI Section
# The outputs below are for troubleshooting and investigating

# print(scoreFrame)
# print(averageScores)
# print(calculatedScores)
# print(len(scoreValues))

# [y][x], the y ignores non-numeral values
# print(scoreFrame.values[0][0])

# Function for the GUI
def guiFunction():
    # First message within the GUI; each time the user interacts with the GUI, the graph must be closed
    print("The graph will need to be closed each time in order to access the GUI, please close the graph to proceed!")
    # graphCreation() creates the original scatter plots with the other values
    graphCreation()
    # Running the Average Graph Creation Function to create that graph
    averageGraphCreation()
    # Will output the Seaborn graph
    matplotlib.pyplot.show()
    # Continuing the user friendly GUI, suggests using the help function to see all commands available
    print("If you wish to leave, please enter the command 'exit'. To see a list of commands, type 'help'!")
    # Initialises userInput as empty
    userinput = ""
    # While the user's input isn't exit, the program will run indefinitely unless if
    # "exit" is typed, or the program closed through windows
    while userinput.lower() != "exit":
        # Input to tell the user the program is ready to receive a new command
        userinput = input("Please enter your next command! ")
        # This line below simply clears the current state of the graph saved in memory
        # This is just so that no odd interactions happen when doing functions one after the other
        matplotlib.pyplot.clf()
        # if/elif/else statement section; Simply checks if the input is X command, if not,
        # moves to check the next command
        # Average Plot Command
        # Plots a graph of the averages from each year
        if userinput.lower() == "averageplot":
            averageGraphCreation()
            print("Outputting Graph of Average Scores only!")
            matplotlib.pyplot.show()
        # Data Plot Command
        # Plots a graph of the raw data from each year
        elif userinput.lower() == "dataplot":
            graphCreation()
            print("Outputting Graph of Data Points only!")
            matplotlib.pyplot.show()
        # Full Plot Command
        # Plots a graph of the raw data and the averages from each year
        elif userinput.lower() == "fullplot":
            graphCreation()
            averageGraphCreation()
            print("Outputting Full Graph!")
            matplotlib.pyplot.show()
        # Sample Plot Command
        # Allows the user to select specific sets of data to be plotted
        # EG in my example, Game set 1, 2, 3, 4, or 5
        elif userinput.lower() == "sampleplot":
            # Input 2 asks the user for which sample they want, as well as the max value possible
            # The max value is coded to fit dynamically, so that if a set of 10 values is used, it will adjust
            userinput2 = input("Please enter the set you wish to see! Max: " + str(len(scoreValues)) + "! ")
            # Does a data check on if the input is a digit/number
            if userinput2.isdigit():
                # If so, checks if the value is between 0 and the max
                if len(scoreValues) >= int(userinput2) >= 1:
                    # If so, draws the graph
                    setgraphCreation(int(userinput2))
                    print("Outputting graph of sample", int(userinput2), "!")
                    matplotlib.pyplot.show()
                # Else, tell the user the value is the wrong size
                else:
                    print("Value either too big or below 1! Try again!")
            # Else, tell the user that the value they entered is invalid
            else:
                print("Value invalid! Try again!")
        # Dataset Command
        # Simply outputs the whole dataset of the calculated values
        elif userinput.lower() == "dataset":
            print("Outputting dataset below:\n ", calculatedScores)
        # Help Command
        # Lists all available commands to the user
        elif userinput.lower() == "help":
            print("List of Commands:"
                  "\n   averageplot -->     Outputs a regression graph showing only the calculated average scores."
                  "\n   dataplot    -->     Outputs a scatter graph showing only the data points of scores."
                  "\n   fullplot    -->     Outputs a regression and scatter graph overlaid for all the available data."
                  "\n   sampleplot  -->     Outputs a scatter graph of a specific sample of data. Requires a follow up "
                  "int input for sample selection."
                  "\n   dataset     -->     Outputs the calculated dataset of values, calculated from the input CSV."
                  "\n   help        -->     Outputs a list of all the available commands."
                  "\n   exit        -->     Exits the program, closes the console window.")
        # Exit Command
        # Prints a farewell message
        # Has no functional use, is only here so the final else command is not triggered when writing exit
        elif userinput.lower() == "exit":
            print("Thank you! See you next time!")
        # Else command
        # Tells the user that they entered an invalid command, so that they are aware why the program has done nothing
        else:
            print("Unrecognized command! Please try again!")


# Running the GUI function to make the whole program work and come together
guiFunction()
