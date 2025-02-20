"""
Problem
Create a function to evaluate a student's attendance record given as a string.

The record includes:

'A' for absent
'L' for late
'P' for present.
To qualify for an attendance award, the student must have:

Fewer than two absences
Should not be late for three or more consecutive days
The function returns true if the student
meets these criteria, and false otherwise.

Examples
checkAttendanceAward("PALPLP")
// true
// Why? The student was absent only once and was never late
// for 3 consecutive days.

checkAttendanceAward("PLPALLL")
// false
// Why? Despite only one absence, the student was late for 3 consecutive days.

checkAttendanceAward("PAPLAPP")
// false
// Why? The student was absent twice even tough was not late for 3 consecutive days.
"""


def checkAttendanceAward(s: str) -> bool:
    if "LLL" in s:
        return False

    if s.count("A") >= 2:
        return False

    return True
