mast_param = {}
student_param = {}
graph_param = {}


def default():
    global mast_param
    global student_param
    global graph_param
    mast_param = {
        # liczba studentów w symulacji
        "student_count": {
            # liczba studentów w akademikach
            "dorms": 400,
            # liczba studentów mieszkająca "na własnym"
            "outside": 5000
        },
        # wartości używane w losowaniach (0 - min, 100 - max)
        "probability": {
            # prawdopodobieństwa wybrania danej akcji jako celu przez studenta
            "action": {
                "home": 10,
                "sleep": 10,
                "sport": 10,
                "study": 10,
                "party": 10
            },
            # prawdopodobieństwo że dany student zostanie wysłany na kwarantannę
            "quarantine": 0
        },
        # o ile mniejsza szansa, że daną akcję wykonamy w czasie do tego nie przeznaczonym
        # im większa wartość, tym mniejsze prawdopodobieństwo
        # przez wartość tą należy podzielić prawdopodobieństwo zajścia zdażenia, żeby uzyskać rzeczywiste prawdopodobieństwo
        "probability_modifier": {
            "home": 100,
            "sleep": 100,
            "sport": 100,
            "study": 100,
            "party": 100,
            "quarantine": {
                "right": 0.1,
                "wrong": 10
            }
        },
        "false_positive_testing_for_quarantine": False,
        # określenie przedziałów czasu potrzebnych na wykonanie danego zadania
        "timeout": {
            "home": {
                "min": 981,
                "max": 2617
            },
            "sleep": {
                "min": 3924,
                "max": 6541
            },
            "sport": {
                "min": 981,
                "max": 1636
            },
            "study": {
                "min": 981,
                "max": 2617
            },
            "party": {
                "min": 981,
                "max": 1636
            },
            "default": 327
        },
        # ilość osób zarażonych na samym początku symulacji
        "initial_infectious_count": {
            "dorms": 1,
            "outside": 0
        },
        "dynamic_action": {
            "infectious_threshold": 100
        }
    }

    student_param = {
        "probability": {
            "recovery": 60
        },
        # współczynnik higieny wpływa na prawdopodobieństwo zarażenia
        "hygiene": 1,
        # współczynnik symptomatyczności wpływa na prawdopodobieństwo wykrycia
        "symptoms": 0.2,
        # czas trwania bycia zarażonym
        "infected_counter": {
            "min": 654 * 12,
            "max": 654 * 13,
        }
    }

    graph_param = {
        # współczynniki zarażalności w danym wierzchołku
        "infectiousness": {
            "dormitory": 0.005,
            "campus_building": 0.01,
            "sport_centre": 0.015,
            "party_zone": 0.02,
            "road": 0.01,
            "quarantine": 1,
            "graveyard": 1
        }
    }


def dict_print(d, indent: int = 0):
    for key, value in d.items():
        if isinstance(value, dict):
            print('\t' * indent + str(key))
            dict_print(value, indent+1)
        else:
            print('\t' * indent + str(key) + ": " + str(value))


def display():
    print("=== mast_param ===")
    dict_print(mast_param)
    print()
    print("=== student_param ===")
    dict_print(student_param)
    print()
    print("=== graph_param ===")
    dict_print(graph_param)
    print()
