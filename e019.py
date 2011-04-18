import datetime
def Euler_19(year = [1901,2000], day=6):
    days = 0
    for years in range(year[0],year[1]+1):
        for months in range(1,13):
            d = datetime.date(years,months,1)
            if d.weekday()==6:
                days +=1
    return days

if __name__=='__main__':
    print(Euler_19())
