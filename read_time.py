#!/usr/bin/env python3



def make_readable(seconds):
    
    if seconds > 359999:
        return
    elif seconds <= 359999 and seconds >= 3600:
        hours = seconds // 3600
        seconds = seconds % 3600
        if hours >= 10:
            hours = str(hours)
        else:
            hours = "0" + str(hours)
        if seconds < 3600 and seconds >= 60:
            minutes = seconds // 60
            if minutes >= 10:
                minutes = str(minutes)
            else:
                minutes = "0" + str(minutes)
            seconds = seconds % 60
            if seconds >= 10:
                seconds = str(seconds)
            else:
                seconds = "0" + str(seconds)
        else:
            minutes = "00"
            if seconds >= 10:
                seconds = str(seconds)
            else:
                seconds = "0" + str(seconds)
        return hours + ":" + minutes + ":" + seconds
    elif seconds < 3600 and seconds >= 60:
        hours = "00"
        minutes = seconds // 60
        seconds = seconds % 60
        if minutes >= 10:
            minutes = str(minutes)
        else:
            minutes = "0" + str(minutes)
        if seconds >= 10:
            seconds = str(seconds)
        else:
            seconds = "0" + str(seconds)
        return hours + ":" + minutes + ":" + seconds
    elif seconds < 60 and seconds > 0:
        hours, minutes = "00", "00"
        if seconds >= 10:
            seconds = str(seconds)
        else:
            seconds = "0" + str(seconds)
        return hours + ":" + minutes + ":" + seconds
    else:
        return "00:00:00"



if __name__ == "__main__":

    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))