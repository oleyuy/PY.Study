def add_time(start, duration, day='' ):
    new_time = 0
    converted_to_24h=0
    digits_time,argument = start.split(' ')
    

    hourse,minutes=digits_time.split(':')
    hourse_of_dur,minutes_of_dur= duration.split(':')
    if argument.lower() == 'pm':
        converted_to_24h=int(hourse)+12
        new_hourse=converted_to_24h+int(hourse_of_dur)
    else:
        new_hourse=int(hourse)+int(hourse_of_dur)
    new_minutes=int(minutes)+int(minutes_of_dur)

    days_of_week={
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
    }
    if day !='' :
        for key,value in days_of_week.items():
            if day.lower() == value.lower():
                current_day=key
                day = days_of_week[key]
    
    
    
    
    if new_hourse >= 24:
        days_later= new_hourse//24
        new_hourse = new_hourse%24   
    else:
        days_later = 0
    
    
    if days_later>=1 and day != '' :
        calculated_day =(current_day+days_later)%7
    elif day!= '':
        calculated_day = current_day

        
    
    if new_minutes>=60:
        new_minutes-=60
        new_hourse+=1
    
    

    pm_hourse={13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,24:12}


    if new_hourse < 12:
        new_argument='AM'
        converted_hourse = new_hourse
    elif new_hourse > 12:
        new_argument='PM'
        converted_hourse=pm_hourse[new_hourse]
        if pm_hourse[new_hourse] == 12:
            days_later+=1
            calculated_day+=1
            new_argument = "AM"

    if day :
        new_time=f"{converted_hourse}:{new_minutes if new_minutes >= 10 else '0' + str(new_minutes)} {new_argument}, {days_of_week[calculated_day]} {'(next day)' if days_later == 1 else f'({days_later} days later)' if days_later > 1 else ''}"
    else:
        new_time=f"{converted_hourse}:{new_minutes if new_minutes >= 10 else '0' + str(new_minutes)} {new_argument}, {'(next day)' if days_later == 1 else f'({days_later} days later)' if days_later > 1 else ''}"


    return new_time



def main():
    
    print(add_time('5:59 AM', '100:00', "Tuesday"))

main()