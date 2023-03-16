#.\env\Scripts\activate
import computervision
import calculate
import Alarm
from test_database import update_status_flags
from test_database import update_status_flags_alarm
import time
running = True
LeafPercent=100
drowning= False
isDistress= False
while running:
    classes=[] 
    confidence=[] 

    classes,confidence= computervision.Model_detection() 
  
    LeafPercent,drowning,isDistress=calculate.filterclasses(classes,confidence)
    print(isDistress)
    #LeafPercent=100
    doc_data = update_status_flags(isDistress, drowning, LeafPercent)

    # Print the document data as a dictionary
    print(doc_data)

    # Check if alarm is active and noticeDistress is True
    if doc_data['alarmEnabled'] and isDistress == True:
        # Turn on alarm
        print('Alarm turned on')
        update_status_flags_alarm(alarmON=True)
        Alarm.play_audio(enabled=True)
    elif not doc_data['alarmEnabled']:
        # Alarm is not active, do nothing
        print('Alarm is not active')
        update_status_flags_alarm(alarmON=False)
        Alarm.play_audio(enabled=False)
    else:
        # Alarm is active but noticeDistress is False, turn off alarm
        print('Alarm turned off')
        Alarm.play_audio(enabled=False)

    # Wait for 1 second before running the loop again
    #time.sleep(1)

    # Check if the user has entered "quit" in the terminal
