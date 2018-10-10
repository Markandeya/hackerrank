import re

time1 = '1:10:10AM'
time2 = '12:10:30AM'
time3 = '12:00:01PM'
time4 = '4:30:59PM'
time5 = '12:00:00AM'
time6 = '12:10:01AM'
time7 = '07:05:45PM'

def conversion(time):
    strsplit = ''
    strsplit = time.split(':')
    hour = int(strsplit[0])
    mini = int(strsplit[1])
    sec = int(strsplit[2][0:2])
    pfix = strsplit[2][2:4] 
    print('{} {} {} {}'.format(hour, mini, sec, pfix))

    hour = hour*3600
    mini = mini*60

    elapsedtime = float(hour+mini+sec)

    if pfix == 'PM' and hour != 12*3600:
        elapsedtime += 12*3600

    if pfix == 'AM' and hour == 12*3600:
        elapsedtime -= 12*3600

    hour24 = elapsedtime//3600;


    print(hour24)
    elapsedtime = elapsedtime - hour24*3600
    min24 = (elapsedtime)//60
    print(min24)
    sec24 = elapsedtime - min24*60
    print(sec24)

    hour24 = str(int(hour24))
    if len(hour24) == 1:
        hour24 = '0'+ hour24 
    min24 = str(int(min24))
    if len(min24) == 1:
        min24 = '0'+ min24
    sec24 = str(int(sec24))
    if len(sec24) == 1:
        sec24 = '0'+ sec24

    timestr =  hour24+ ':' +  min24+ ':' + sec24
    return timestr

p = conversion(time7)
print(p)