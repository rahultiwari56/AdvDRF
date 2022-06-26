import json
import requests

URL = "http://127.0.0.1:8000/api/"
# URL = "http://127.0.0.1:8000/api/stuinfo/2"

def get_student(id):
    api_url = f'{URL}stuinfo/{id}'
    resp = requests.get(url = api_url)
    data = resp.json()
    print(data)

def get_all_student():
    api_url = f'{URL}stuinfo/'
    resp = requests.get(url = api_url)
    data = resp.json()
    print(data)
    

# get
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    api_url = f'{URL}getstudata/'
    resp = requests.get(url = api_url, data=json_data)
    data = resp.json()
    print(data)


# post
def add_student(name, roll, city):

    data = {
        'name': name,
        'roll': roll,
        'city': city
    }

    api_url = f'{URL}stucreate/'

    json_data = json.dumps(data)

    resp = requests.post(url = api_url, data = json_data)
    data = resp.json()
    print(data)


if __name__=='__main__':
    # get_student(2)
    # get_all_student()

    ## post data 
    # add_student('Anuj', 104, 'Pune')

    ## get data
    # get_data(4)
    # get_data()

    pass

