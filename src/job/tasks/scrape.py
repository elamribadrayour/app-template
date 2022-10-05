from data import elysee

def run(data_name: str = None) -> None:
    if data_name == "elysee":
        elysee.get_documents()
    return