
# scores_info.py - reads NUMBERS from file but
# also computes average and highest score.

def main():
    # make variable for format output
    column_width_string = '12s'
    column_width_integer = '8d'
    # open scores.txt as mytests in READ mode
    mytests = open('scores.txt','r')
    count = 0 # COUNTER (maybe # of scores is unknown)
    high = 0 # variable for highest score
    total = 0 # ACCUMULATOR for scores
    print('Reading six tests and scores') # BEFORE loop
    print(format('TEST',column_width_string), format('       SCORE',column_width_string))

    # start a for loop that will read each line
    # one-by-one, into a variable named line.
    for line in range(6):
            
        name = mytests.readline()
        name = name.rstrip('\n')

        score = mytests.readline()
        score = score.rstrip('\n')
        score = int(score) # convert from string
        
        print(format(name,column_width_string), format(score,'12d'))

        total += score  # ACCUMULATE scores


    # next statements are AFTER loop ends, NOT in loop
    mytests.close() # close file

    
    
    
    print('Average is: ',format(total / 6,'.1f'))
##    print('Highest score:',high)


main()


