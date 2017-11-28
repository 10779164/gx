#!encoding=utf8
from app import app
import time



@app.route('/time')
def local_time():
    week={'Monday':'星期一',
    	 'Tuesday':'星期二',
	 'Wednesday':'星期三',
	 'Thursday':'星期四',
	 'Friday':'星期五',
	 'Saturday':'星期六',
	 'Sunday':'星期六'}
    local_time=time.strftime("%Y-%m-%d %H:%M:%S")
    local_week=time.strftime('%A')
    rel_week=week[local_week]
    return local_time+' '+rel_week
