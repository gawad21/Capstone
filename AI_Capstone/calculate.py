#classes = [2, 2, 2, 0]
#confidence = [0.4, 0.6, 0.7,0.7]
def filterclasses(classes,confidence):
    maxedLeaves = False
    drowning = False
    isDistress = False
    # Define the minimum confidence threshold
    min_confidence = 0.6

    # Get the indices of the elements that meet the minimum confidence threshold
    filtered_indices = [i for i in range(len(confidence)) if confidence[i] >= min_confidence]

    # Create a new list that contains the classes that meet the confidence threshold
    filtered_classes = [classes[i] for i in filtered_indices]

    # Count the number of times the object of interest appears in the filtered list
    object_of_interest = 2
    leaf_count = filtered_classes.count(object_of_interest)

    if leaf_count >= 3:
        maxedLeaves = True
    else :
        maxedLeaves = False

    for c in filtered_classes:
        if c == 0:
            drowning = True
        elif c == 3:
            isDistress = True

    return maxedLeaves,drowning,isDistress
