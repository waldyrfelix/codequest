from check_attendance_award.quest import checkAttendanceAward


def test_checkAttendanceAward_1():
    result = checkAttendanceAward("PALPLP")
    assert result == True


def test_checkAttendanceAward_2():
    result = checkAttendanceAward("PLPALLL")
    assert result == False


def test_checkAttendanceAward_3():
    result = checkAttendanceAward("PAPLAPP")
    assert result == False
