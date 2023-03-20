import requests
from bs4 import BeautifulSoup


def extraction_data():
    i = 0
    magnitude = None
    depth = None
    ls = None
    bt = None
    location = None
    felt = None

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        results = soup.find('span', {'class', 'waktu'})
        results = results.text.split(', ')
        time = results[0]
        date = results[1]

        results = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        results = results.findChildren('li')

        for res in results:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                coordinate = res.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                location = res.text
            elif i == 5:
                felt = res.text
            i = i + 1

        results = dict()
        results['tanggal'] = date
        results['waktu'] = time
        results['magnitudo'] = magnitude
        results['kedalaman'] = depth
        results['koordinat'] = {'ls': ls, 'bt': bt}
        results['lokasi'] = location
        results['diraskan'] = felt
        return results
    else:
        return None


def view_data(results):
    if results is None:
        print('Data not found')
        return
    print(f"Date {results['tanggal']}")
    print(f"Time {results['waktu']}")
    print(f"Magnitude {results['magnitudo']}")
    print(f"Depth {results['kedalaman']}")
    print(f"Location {results['lokasi']}")
    print(f"Coordinate : LS {results['koordinat']['ls']}, BT={results['koordinat']['lb']}")
    print(f"Felt {results['dirasakan']}")


if __name__ == '__main__':
    print('WEB SCRAP APP')
    result = extraction_data()
    view_data(result)



