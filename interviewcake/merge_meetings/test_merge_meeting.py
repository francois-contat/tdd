import merge_meeting

def test_exploding_meeting():
    assert merge_meeting.explode_meetings([[1,3]]) == [[1,2,3]]
    assert merge_meeting.explode_meetings([[1,2,3]]) == [[1,2,3]]
    assert merge_meeting.explode_meetings([[1,7]]) == [[1,2,3,4,5,6,7]]
