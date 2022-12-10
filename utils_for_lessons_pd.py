import pandas as pd
df = pd.read_json("lessons_pd.json")
import datetime
all_cabs = set(df["classroom"].unique())-{None}
cabs = {cab for cab in all_cabs if not(cab.isdigit()|(cab[0]=="G"))}
teachers = list(df["teacher"].unique())
def from_time(hours, minutes=None):
    if minutes is None:
        hours, minutes = hours.split(":")
    return int(hours)*60+int(minutes)
def to_time(time):
    return f"{time//60}:"+str(time%60).ljust(2, '0')
def now(df):
    today = datetime.datetime.now()
    return then(df, from_time(today.hour, today.minute))
def time_overlap(df, time=None):
    if isinstance(time, str):
        time = from_time(time)
    if isinstance(time, list):
        time = from_time(*time)
    if time is None:
        return now(df)
    return df[(df["start"]<=time) & (df["end"]>=time)]
def then(df, time, date=None):
    today = datetime.datetime.now()
    if date is None:
        date = str(today.month).rjust(2, "0")+"/"+str(today.day).rjust(2, "0")
    return time_overlap(df[(df["date"] == date)], time)
def overlap(df, fields):
    df = df.copy()
    try:
        df = time_overlap(df, fields["time"])
        del fields["time"]
    except KeyError:
        pass
    for key in fields:
        df = df[df[key].apply(lambda x: fields[key] in x if x else False)]
    return df
def where_will(df, teacher, date):
    return overlap(df, {"teacher": teacher})[df["date"] == date]
def where(df, teacher):
    today = datetime.datetime.now()
    return where_will(df, teacher, f"{today.month}/{today.day}")
def show(df):
    df = df.copy()

    new_df = pd.DataFrame(columns = df.keys())
    for entry in df.values:
        overlap = list(df[(df["date"]==entry[0]) & (df["start"]==entry[1]) & (df["classroom"]==entry[6])]["class"].values)
        repeat = new_df[(new_df["date"]==entry[0]) & (new_df["start"]==entry[1]) & (new_df["classroom"]==entry[6])].index
        if len(repeat) == 0:
            entry[4] = overlap
            new_df.loc[len(new_df.index)] = entry
    df = sorted_df(new_df)
    df["start"] = df["start"].apply(to_time)
    df["end"] = df["end"].apply(to_time)
    return df
def will_free(df, time, date=None):
    return cabs-set(then(df, time, date)["classroom"])
def free(df):
    return cabs-set(now(df)["classroom"])
def sorted_df(df):
    df = df.copy()
    return df.sort_values(["date", "start", "end"])
def today(df):
    now = datetime.datetime.now()
    return df[df["date"] == (str(now.month).rjust(2, "0")+"/"+str(now.day).rjust(2, "0"))]
def df_now():
    return now(df)
def df_time_overlap(time=None):
    return time_overlap(df, time)
def df_then(time, date=None):
    return then(time, date)
def df_overlap(fields):
    return overlap(fields)
def df_where_will(teacher, date):
    return where_will(teacher, date)
def df_where(teacher):
    return where(teacher)
def df_show():
    return show()
def df_will_free(time, date=None):
    return will_free(time, date)
def df_free():
    return free()
def df_sorted_df():
    return sorted_df()
def df_today():
    return today()
