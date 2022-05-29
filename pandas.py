#Nombre: Deison Tuiran Londoño
#Email: deison.tuiran@upb.edu.co
#Codigo: 014810

import pandas as pd
#1
datos = pd.read_csv("netflix_titles.csv")
print(datos)
#2
print(datos.tail())
#3
print(datos.info())
#4
datos.to_excel("Netflix_list.xlsx", sheet_name="títulos")
#5
segt = datos[["type", "duration", "description", "country"]]
print(segt)
#6
movies = datos[datos["type"] == "Movie"]
DivDurationMovies = movies["duration"].str.split(expand=True).dropna()
movies.insert(4,"durationIntMovies", DivDurationMovies[0].astype(int))
filtered_by_more_than_100 = movies[movies["durationIntMovies"] > 100]
print(filtered_by_more_than_100)
#7
series = datos[datos["type"] == "TV Show"]
DivDurationseries = series["duration"].str.split(expand=True).dropna()
series.insert(5, "durationIntSeries", DivDurationseries[0].astype(int))
FiltBy3 = series[series["durationIntSeries"] > 3]
print(FiltBy3)
#8
print(datos[["type", "title"]])
#9
print(datos.loc[:, "director"])
print(datos.iloc[:, 4])
#10
datos["show_id"] = datos["show_id"].replace({"s1":"1","s2":"2","s3":"3","s4":"4","s5":"5"})
datos["show_id"] = datos["show_id"].replace({"s8803":"8803","s8804":"8804","s8805":"8805","s8806":"8806","s8807":"8807"})
print(datos)