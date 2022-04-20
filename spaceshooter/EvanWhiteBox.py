
global player_lives
player_lives = 3
global offset
offset = 1

score = 0
offset = 1

def extralife():
        #Give the player and extra life every so often
        global player_lives
        global offset
        if (score > (1000 * offset) and score != 0):
            player_lives += 1
            offset += 1

#----------- Start white box testing
with open("spaceshooter/evan_whitebox_suite.txt", "r") as input_file:
    tests = input_file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
tests = [x.strip() for x in tests]

with open("spaceshooter/evan_whitebox_expected.txt", "r") as expected_file:
    expected = expected_file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
expected = [x.strip() for x in expected]

with open("spaceshooter/evan_whitebox_suite_output.txt", "w+") as output:
    for x in range(len(tests)):
        score = int(tests[x])
        extralife()
        if (player_lives == int(expected[x])):
            output.write("Test " + str(x) + " PASSED ---------------------\n")
            output.write("Given score: " + str(score) + "\n")
            output.write("Player lives is: " + str(player_lives) + "\n")
            output.write("This matched the expected value: " + expected[x] + "\n\n")
        else:
            output.write("Test " + str(x) + " FAILED ---------------------\n")
            output.write("Given score: " + str(score) + "\n")
            output.write("Player lives is: " + str(player_lives) + "\n")
            output.write("This did not match the expected value: " + expected[x] + "\n\n")

print("Done Testing")