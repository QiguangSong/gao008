import requests as requests

if __name__ == '__main__':
    response = requests.get('http://www.gao008.com/So.asp')
    if response.status_code == 200:
        open('../gao888.html', 'wb').write(response.content)
