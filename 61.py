# store_scores.py - writes NUMBERS to file.
# NOTE: ALL file input/output uses STRINGS.
# str() converts numbers to strings.  

def main():
    # open scores.txt as tests in WRITE mode
    tests = open('scores.txt','w')
    # use a loop to prompt user for 6 test scores
    for test in range(6):
        name = input('Enter a test name: ')
        score = int(input('Enter test score '))
        # assume user complies and enters integers
        # convert to STRING and write to file
        tests.write(str(name) + '\n')
        tests.write(str(score) + '\n')

    # close file
    tests.close()
    print('File was created successfully') # report success 

main()

