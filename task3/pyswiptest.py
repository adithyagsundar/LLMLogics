from pyswip import Prolog

prolog = Prolog()

prolog.consult(r"C:\Users\Tntad\OneDrive\Desktop\Documents\LLMLogics\LLMLogics\task3\SimpsonsKB.pl")

while True:
    query = input("What would you like to ask Prolog?")

    query_result = prolog.query(query)

    for query in query_result:
        print(query["X"])