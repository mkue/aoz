In PyCharm, auf Ordner `berkel/` Rechtsklick und dann auf "Mark Directory" -> "sources Root"

Server starten:

```
python manage.py runserver
```


Falls models geändert wurden, muss makemigrations ausgeführt werden:

```
python manage.py makemigrations
```

und danach angewendet werden mit:

```
python manage.py migrate
```
