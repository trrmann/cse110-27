import ast
from datetime import MAXYEAR, MINYEAR, datetime, timedelta
import os

class DateDictionary():
    __type_key__ = "type"
    __datetime_type__ = "dateTime"
    __delta_type__ = "delta"
    __year_key__ = "year"
    __month_key__ = "month"
    __day_key__ = "day"
    __hour_key__ = "hour"
    __minute_key__ = "minute"
    __second_key__ = "second"
    __micro_second_key__ = "microSecond"
    __days_key__ = "days"
    __seconds_key__ = "seconds"
    __micro_seconds_key__ = "microSeconds"
    __datetime_key__ = "datetime"
    __timedelta_key__ = "timedelta"
    __date_dictionary_key__ = "dateDict"
    __delta_dictionary_key__ = "deltaDict"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, date_time :datetime = None, time_delta :timedelta = None, dateDict :dict = None, deltaDict :dict = None, *args, **kwargs):
        self.__data__ = {}
        if (date_time != None) and (dateDict != None): dateDict = None
        if (time_delta != None) and (deltaDict != None): deltaDict = None
        if dateDict != None:
            date_time = self.dict_to_date(dateDict)
            dateDict = None
        if deltaDict != None:
            time_delta = self.dict_to_delta(deltaDict)
            deltaDict = None
        if (date_time != None) and (time_delta != None):
            date_time += time_delta
            time_delta = None
        if date_time != None:
            self.set_type(self.__datetime_type__)
            self.set_datetime(date_time)
        if time_delta != None:
            self.set_type(self.__delta_type__)
            self.set_timedelta(time_delta)

    def __repr__(self) -> str:
        string = f"\"{self.__type_key__}\" : \"{self.get_type()}\""
        string = f"{string}, \"{self.__date_dictionary_key__}\" : {self.date_to_dict(self.get_datetime())}"
        string = f"{string}, \"{self.__delta_dictionary_key__}\" : {self.delta_to_dict(self.get_timedelta())}"
        string = f"\( {string} \)"
        string = f"\( \"{type(self).__name__}\" : {string} \)"
        string = string.replace("\(", "{")
        string = string.replace("\)", "}")
        return string

    def set_type(self, type :str = None):
        self.__data__[self.__type_key__] = str(type)
        return self

    def get_type(self, type :str = None):
        if self.__type_key__ in self.__data__.keys(): return self.__data__[self.__type_key__]
        elif type != None: return self.set_type(str(type)).get_type()
        else: return self.set_type().get_type()

    def set_datetime(self, date_time :datetime = None):
        # todo type check datetime
        if date_time == None: date_time = datetime.now()
        self.__data__[self.__datetime_key__] = date_time
        return self

    def get_datetime(self, date_time :datetime = None):
        if self.__datetime_key__ in self.__data__.keys(): return self.__data__[self.__datetime_key__]
        elif date_time != None: return self.set_datetime(datetime(date_time)).get_datetime()
        else: return self.set_datetime().get_datetime()

    def set_timedelta(self, time_delta :timedelta = None):
        # todo type check timedelta
        if time_delta == None: time_delta = timedelta(0,0,0)
        self.__data__[self.__timedelta_key__] = time_delta
        return self

    def get_timedelta(self, time_delta :timedelta = None):
        if self.__timedelta_key__ in self.__data__.keys(): return self.__data__[self.__timedelta_key__]
        elif time_delta != None: return self.set_timedelta(timedelta(time_delta)).get_timedelta()
        else: return self.set_timedelta().get_timedelta()

    def date_to_dict(self, date_time: datetime = datetime.now()): return {self.__type_key__ : self.__datetime_type__, self.__year_key__ : date_time.year, self.__month_key__ : date_time.month, self.__day_key__ : date_time.day, self.__hour_key__ : date_time.hour, self.__minute_key__ : date_time.minute, self.__second_key__ : date_time.second, self.__micro_second_key__ : date_time.microsecond}

    def delta_to_dict(self, delta: timedelta = timedelta(0,0,0)): return {self.__type_key__ : self.__delta_type__, self.__days_key__ : delta.days, self.__seconds_key__ : delta.seconds, self.__micro_seconds_key__ : delta.microseconds}

    def dict_to_date(self, dictionary: dict = None):
        if dictionary == None: self.date_to_dict()
        match dictionary[self.__type_key__]:
            case self.__datetime_type__: return datetime.datetime(dictionary[self.__year_key__], dictionary[self.__month_key__], dictionary[self.__day_key__], dictionary[self.__hour_key__], dictionary[self.__minute_key__], dictionary[self.__second_key__], dictionary[self.__micro_second_key__])
            case self.__delta_type__: return self.dict_to_delta(dictionary)
            case _: return None

    def dict_to_delta(self, dictionary: dict = None):
        if dictionary == None: self.date_to_dict()
        match dictionary[self.__type_key__]:
            case self.__delta_type__: return timedelta(dictionary[self.__days_key__], dictionary[self.__seconds_key__], dictionary[self.__micro_seconds_key__])
            case self.__datetime_type__: return self.dict_to_date(dictionary)
            case _: return None

    def date_diff_dict(self, first_date: datetime = None, second_date: datetime = None):
        if first_date == None: first_date = datetime.now()
        if second_date == None: second_date = datetime.now()
        return self.delta_to_dict(second_date - first_date)

    def date_dict_to_delta_dict(self, dictionary: dict = None):
        if dictionary == None: self.date_to_dict()
        now = datetime.datetime.now()
        if dictionary[self.__year_key__] < datetime.MINYEAR:
            year_mod = int(datetime.MINYEAR - dictionary[self.__year_key__])
        elif dictionary[self.__year_key__] > datetime.MAXYEAR:
            year_mod = int(dictionary[self.__year_key__] - datetime.MAXYEAR)
        else:
            year_mod = 0
        if dictionary[self.__month_key__] < 1:
            month_mod = int(1 - dictionary[self.__month_key__])
        elif dictionary[self.__month_key__] > 12:
            month_mod = int(dictionary[self.__month_key__] - 12)
        else:
            month_mod = 0
        if dictionary[self.__day_key__] < 1:
            day_mod = int(1 - dictionary[self.__day_key__])
        elif dictionary[self.__day_key__] > 31:
            day_mod = int(dictionary[self.__day_key__] - 31)
        else:
            day_mod = 0
        dictionary[self.__year_key__] += year_mod
        dictionary[self.__month_key__] += month_mod
        dictionary[self.__day_key__] += day_mod
        dictionary = self.date_to_dict(self.dict_to_date(dictionary))
        dictionary[self.__year_key__] -= year_mod
        dictionary[self.__month_key__] -= month_mod
        dictionary[self.__day_key__] -= day_mod
        minute_to_seconds_factor = 60
        hour_to_seconds_factor = minute_to_seconds_factor * 60
        month_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/(12*16))
        year_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/16)
        return self.delta_to_dict(datetime.timedelta(int(dictionary[self.__day_key__] + dictionary[self.__month_key__] * month_to_days_factor + dictionary[self.__year_key__] * year_to_days_factor), int(dictionary[self.__second_key__] + dictionary[self.__minute_key__] * minute_to_seconds_factor + dictionary[self.__hour_key__] * hour_to_seconds_factor), dictionary["microsecond"]))

    def delta_dict_to_date_dict(self, dictionary: dict = None):
        if dictionary == None: self.date_to_dict()
        now = datetime.now()
        dictionary = self.delta_to_dict(self.dict_to_delta(dictionary))
        minute_to_seconds_factor = 60
        hour_to_seconds_factor = minute_to_seconds_factor * 60
        month_to_days_factor = ((datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)\
            - datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/(12*16))
        year_to_days_factor = ((datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)\
            - datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/16)
        microseconds = dictionary[self.__micro_seconds_key__]
        seconds = dictionary[self.__seconds_key__]
        days = dictionary[self.__days_key__]
        microsecond = microseconds
        hour = divmod(seconds, hour_to_seconds_factor)[0]
        seconds = seconds - (hour * hour_to_seconds_factor)
        minute = divmod(seconds, minute_to_seconds_factor)[0]
        second = seconds - (minute * minute_to_seconds_factor)
        year = divmod(days, year_to_days_factor)[0]
        days = days - (year * year_to_days_factor)
        month = divmod(days, month_to_days_factor)[0]
        day = days - (month * month_to_days_factor)
        if year < MINYEAR:
            year_mod = int(MINYEAR - year)
        elif year > MAXYEAR:
            year_mod = int(year - MAXYEAR)
        else:
            year_mod = 0
        if month < 1:
            month_mod = int(1 - month)
        elif month > 12:
            month_mod = int(month - 12)
        else:
            month_mod = 0
        if day < 1:
            day_mod = int(1 - day)
        elif day > 31:
            day_mod = int(day - 31)
        else:
            day_mod = 0
        date_dict = self.date_to_dict(datetime(int(year) + year_mod, int(month) + month_mod, int(day) + day_mod, int(hour), int(minute), int(second), int(microsecond)))
        date_dict[self.__year_key__] = date_dict[self.__year_key__] - year_mod
        date_dict[self.__month_key__] = date_dict[self.__month_key__] - month_mod
        date_dict[self.__day_key__] = date_dict[self.__day_key__] - day_mod
        return date_dict


file_name = "data.dat"
if not os.path.exists(file_name):
    print("no file... create")
    file = open(file_name, "xt")
    file.close()
file = open(file_name, "rt")
file_data = ast.literal_eval(file.read())
file.close()
print(file_data)
if file_data == "":  file_data = {}
if "x" in file_data.keys(): print(f"x = {file_data['x']}")
if "y" in file_data.keys(): print(f"y = {file_data['y']}")
file_data["x"] = 1
file_data["y"] = 2
file = open(file_name, "wt")
file.write(str(file_data))
file.close()


created = DateDictionary(datetime.fromtimestamp(os.path.getctime(file_name)))
modified = DateDictionary(datetime.fromtimestamp(os.path.getmtime(file_name)))
accessed = DateDictionary(datetime.fromtimestamp(os.path.getatime(file_name)))

dd = DateDictionary()

create_age = dd.delta_dict_to_date_dict(dictionary = dd.date_diff_dict(first_date = created.get_datetime()))
modified_age = dd.delta_dict_to_date_dict(dictionary = dd.date_diff_dict(first_date = modified.get_datetime()))
accessed_age = dd.delta_dict_to_date_dict(dictionary = dd.date_diff_dict(first_date = accessed.get_datetime()))

print(f"created:  {created} - {created.get_datetime()}")
print(f"last modified:  {modified} - {modified.get_datetime()}")
print(f"last accessed:  {accessed} - {accessed.get_datetime()}")
print(f"now {datetime.now()}")

print(f"create age:  {create_age['year']} years {create_age['month']} months {create_age['day']} days {create_age['hour']} hours {create_age['minute']} minutes {create_age['second']} seconds")
print(f"modified age:  {modified_age['year']} years {modified_age['month']} months {modified_age['day']} days {modified_age['hour']} hours {modified_age['minute']} minutes {modified_age['second']} seconds")
print(f"last accessed age:  {accessed_age['year']} years {accessed_age['month']} months {accessed_age['day']} days {accessed_age['hour']} hours {accessed_age['minute']} minutes {accessed_age['second']} seconds")
