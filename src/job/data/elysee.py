import urllib.request

from tqdm import tqdm

def get_document(index: str) -> int:
    url = f"https://www.elysee.fr/front/pdf/elysee-module-{index}-fr.pdf"
    try:
        response = urllib.request.urlretrieve(url, "filename.pdf")
    except:
        return 404
    return response.status_code

def get_documents() -> None:
    start = 0
    index = 0
    for index in tqdm(range(1000)):
        status_code = get_document(index)
        if status_code != 404 and start == 0:
            start = index
        elif status_code == 404 and start != 0:
            print(f"Ending at index {index}")
            break
    return

if __name__ == "__main__":
    get_documents()