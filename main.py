from core import track_function, dag_structure


@track_function
def clean_data(data):
    return data + " cleaned"


@track_function
def transform_data(data):
    data = clean_data(data)
    return data + " transformed"


@track_function
def process_data(data):
    data = transform_data(data)
    return data + " processed"


result = process_data("raw data")


print(dag_structure)
