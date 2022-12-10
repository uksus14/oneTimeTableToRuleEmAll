from json import loads, dumps
with open("lessons.json", "r", encoding="utf-8") as f:
    data = loads(f.read())
t = lambda m:list(zip(*m))
classes = set()
for r in data:
    for el in r:
        if el[:5] == "Класс":
            classes = classes.union({class_.strip() for class_ in el[6:].split(",")})
classes = tuple(classes)
norm_label = {"Предмет": "subject", "Класс": "class", "Учитель": "teacher", "Кабинет": "classroom"}
pd_data = []
compare = lambda left,right,*args:all([left[arg]==right[arg]for arg in args])
for info in data:
    date = "/".join(info[0].replace(".", "").split()[:0:-1])
    start, end = [time.split(":") for time in info[1].split("-")]
    start = int(start[0])*60+int(start[1])
    end = int(end[0])*60+int(end[1])
    add = {"date": date, "start": start, "end": end}
    add.update({value: None for value in norm_label.values()})
    for inf in info[2:]:
        label, _, value = inf.partition(":")
        add[norm_label[label]] = value.strip()
    add_list = add["class"].split(",")
    for class_add in add_list:
        add["class"] = class_add.strip()
        overlap = [info for info in pd_data if compare(info, add, "class", "subject", "teacher", "classroom", "start", "end", "date")]
        if not overlap:
            pd_data.append(add.copy())
with open("lessons_pd.json", "w", encoding="utf-8") as f:
    f.write(dumps(pd_data))