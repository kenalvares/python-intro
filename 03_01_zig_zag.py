# ZigZag Pattern
import time, sys
indent = 0  # Spaces to indent
indentIncreasing = True # Is the indent going up or not

try:
    while True:  # Main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th sec

        if indentIncreasing:
            # Increase number of spaces
            indent+=1
            if indent == 20:
                # Change direction
                indentIncreasing = False
        else:
            # Decrease number of spaces
            indent-=1hhhh
            if indent == 0:
                # Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
