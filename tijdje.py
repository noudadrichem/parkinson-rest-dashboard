import time, datetime

# THIS IS NOT MY CODE:

def now_milliseconds():
   return int(time.time() * 1000)

# reference time.time
# Return the current time in seconds since the Epoch.
# Fractions of a second may be present if the system clock provides them.
# Note: if your system clock provides fractions of a second you can end up
# with results like: 1405821684785.2
# our conversion to an int prevents this

def date_time_milliseconds(date_time_obj=datetime.datetime.utcnow()):
  return int(time.mktime(datetime.datetime.utcnow().timetuple()) * 1000)

# reference: time.mktime() will
# Convert a time tuple in local time to seconds since the Epoch.

# source:
#https://stackoverflow.com/questions/24829726/python-function-to-return-javascript-date-gettime
