from pyswip import Prolog

prolog = Prolog()

prolog.consult("SimpsonsKB.pl")

while True:
    query = input("What would you like to ask Prolog?")

    query_result = prolog.query(query)

    for query in query_result:
        print(query["X"])