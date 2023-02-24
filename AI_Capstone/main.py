'''
import computervision
import calculate
import Alarm
from test_database import update_status_flags
classes=[] 
confidence=[] 

classes,confidence= computervision.Model_detection()    
maxedLeaves,drowning,isDistress=calculate.filterclasses(classes,confidence)
print(isDistress)
doc_data = update_status_flags(isDistress, drowning, maxedLeaves)

# Print the document data as a dictionary
print(doc_data)


# Check if alarm is active and noticeDistress is True
if doc_data['alarmActive'] and doc_data['noticeDistress']:
    # Turn on alarm
    print('Alarm turned on')
    Alarm.play_audio(enabled=True)
elif not doc_data['alarmActive']:
    # Alarm is not active, do nothing
    print('Alarm is not active')
else:
    # Alarm is active but noticeDistress is False, turn off alarm
    print('Alarm turned off')
    Alarm.play_audio(enabled=False)
'''
import computervision
import calculate
import Alarm
from test_database import update_status_flags
import time
running = True
while running:
    classes=[] 
    confidence=[] 

    classes,confidence= computervision.Model_detection()    
    maxedLeaves,drowning,isDistress=calculate.filterclasses(classes,confidence)
    print(isDistress)
    doc_data = update_status_flags(isDistress, drowning, maxedLeaves)

    # Print the document data as a dictionary
    print(doc_data)

    # Check if alarm is active and noticeDistress is True
    if doc_data['alarmActive'] and doc_data['noticeDistress']:
        # Turn on alarm
        print('Alarm turned on')
        Alarm.play_audio(enabled=True)
    elif not doc_data['alarmActive']:
        # Alarm is not active, do nothing
        print('Alarm is not active')
        Alarm.play_audio(enabled=False)
    else:
        # Alarm is active but noticeDistress is False, turn off alarm
        print('Alarm turned off')
        Alarm.play_audio(enabled=False)

    # Wait for 1 second before running the loop again
    #time.sleep(1)

    # Check if the user has entered "quit" in the terminal
