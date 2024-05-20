import timeit
import requests
from bm_search import * 
from kmp_search import *  
from rk_search import * 

def download_and_save_articles(response1, response2, filename1, filename2):
    try:
        response1 = requests.get('https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view')
        response2 = requests.get('https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view')

        if response1.status_code == 200 and response2.status_code == 200:
            with open(filename1, "w") as f1, open(filename2, "w") as f2:
                f1.write(response1.text)
                f2.write(response2.text)
            return True
        else:
            print(f"Error downloading articles. Status codes: {response1.status_code}, {response2.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during download: {e}")
        return False

def compare_algorithms(text_file, real_substring, fake_substring):
    
    try:
        with open(text_file, "r") as f:
            text = f.read()

        real_times = {
            'BM': timeit.timeit(lambda: bm_search(text, real_substring), number=1000),
            'KMP': timeit.timeit(lambda: kmp_search(text, real_substring), number=1000),
            'RK': timeit.timeit(lambda: rk_search(text, real_substring), number=1000),
        }

        fake_times = {
            'BM': timeit.timeit(lambda: bm_search(text, fake_substring), number=1000),
            'KMP': timeit.timeit(lambda: kmp_search(text, fake_substring), number=1000),
            'RK': timeit.timeit(lambda: rk_search(text, fake_substring), number=1000),
        }

        print(f"**{text_file}**")
        print("Real substring:")
        for algorithm, time in real_times.items():
            print(f"{algorithm}: {time:.4f} seconds")

        print("Fake substring:")
        for algorithm, time in fake_times.items():
            print(f"{algorithm}: {time:.4f} seconds")

        fastest_real = min(real_times, key=real_times.get)
        fastest_fake = min(fake_times, key=fake_times.get)

        print(f"Fastest algorithm for real substring: {fastest_real}")
        print(f"Fastest algorithm for fake substring: {fastest_fake}")

    except FileNotFoundError:
        print(f"Error: File '{text_file}' not found.")

if __name__ == '__main__':
    article1_url = 'https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view' 
    article2_url = 'https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view'