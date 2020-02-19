def explode_meetings(meetings):
    '''
        In this function we take each meeting and we expand them from their
        edges {1,3} => {1, 2, 3}
    '''
    new_meeting_list = list()
    for meeting in meetings:
        new_meeting = [meeting[0]]
        pointer = 0
        while new_meeting[-1] != meeting[-1]:
            new_meeting.append(new_meeting[pointer]+1)
            pointer += 1
        new_meeting_list.append(new_meeting)
    return (new_meeting_list)


