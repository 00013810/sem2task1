def new_line():
    print('*')


new_line()
print('One new line *')


# in this function we will add additional stars with help of previous function new_line()
def three_line():
    new_line()
    new_line()
    new_line()


three_line()
print('Three lines of *')

'''as this new function include the last function three lines we will write only three times
inside of new function nine_line()'''


def nine_lines():
    three_line()
    three_line()
    three_line()


nine_lines()
print('Nine lines of *')


# now we combine three different functions to get 25 * in output
def clean_screen():
    nine_lines()
    nine_lines()
    three_line()
    three_line()
    new_line()


clean_screen()
print('Twenty five lines of *')
