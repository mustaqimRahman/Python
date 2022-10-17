import random
import uuid
import datetime
import config

# Declaring names, verbs and nouns for Title
names = ["You", "I", "They", "He", "She", "Robert", "Steve", "Canada", "US"]
article = ["was", "is", "are", "were", "here", "there"]
verbs = ["playing cricket.", "watching television.",
         "singing.", "fighting.", "cycling.", "working", "learning"]
special_character = ["@", "^", "*", "%", "€", " ", ""]

# Declaring roman numbers for type
roman_numbers = ["i", "iv", "v", "ix", "x",
                 "xl", "l", "xc", "c", "cd", "d", "cm", "m"]


def generate_row():
    # TITLE
    # ===================================================================================
    a = (random.choice(names))
    b = (random.choice(article))
    c = (random.choice(verbs))
    sp = (random.choice(special_character))

    title = a+" " + sp + b+" " + c
    title = str(title)
    title = title.encode("ascii", "ignore")
    title = title.decode()
    # ===================================================================================

    # ID
    # ===================================================================================
    # Generating random uniqie id
    id = uuid.uuid4()
    id = str(id)
    # ===================================================================================

    # PUBLICATION_DATE
    # ===================================================================================
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2022, 9, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    publication_date = start_date + \
        datetime.timedelta(days=random_number_of_days)
    publication_date = str(publication_date).split('-')
    year = publication_date[0]
    month = publication_date[1]
    day = publication_date[2]
    publication_date = month + '/' + day + '/' + year
    # ===================================================================================

    # SOURCE
    # ===================================================================================
    source = random.randint(0, 99)
    source = str(source)
    source = source.replace(str(random.randint(50, 99)), '')
    # ===================================================================================

    # TYPE
    # ===================================================================================

    type = (random.choice(roman_numbers))
    type = str(type)
    # ===================================================================================

    row = title + ',' + id + ',' + publication_date + ',' + source + ',' + type

    return row


def add_rows_to_csv(number_of_records_to_add):
    i = 0
    rows = ''
    while i < number_of_records_to_add:
        rows += generate_row() + '\n'
        i += 1

    with open(config.source, 'a') as fd:
        fd.write(rows)

    return 'source csv file appended'
