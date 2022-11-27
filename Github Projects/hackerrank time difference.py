from datetime import datetime
def time_delta(t1, t2):
    time_one = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    time_two = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    final = str(int(abs(time_one - time_two).total_seconds()))
    print(final)

time_delta('Sun 10 May 2015 13:54:36 -0700','Sun 10 May 2015 13:54:36 -0000')