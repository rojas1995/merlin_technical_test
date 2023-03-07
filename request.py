import requests
#import apache_beam as beam
#from apache_beam import PCollection
import json


class Pet:

    def __init__(self, pairs):
        self.pairs = pairs

    def count_eq_names(self):
        names = list(map(lambda element: element[1] if element is not None else None, self.pairs))
        tuple_count = tuple(
            map(lambda element: (names[names.index(element)], names.count(element)) if element is not None else None,
                names))

        result =  list(dict.fromkeys(tuple_count))
        if None in result:
            result.remove(None)

        return result

def get_id_name(element):
    if 'id' in element and 'name' in element:
        return (element['id'], element['name'])


# create the user
url = "https://petstore.swagger.io/v2/user"

payload = json.dumps({
    "id": 7,
    "username": "rojas",
    "firstName": "jose",
    "lastName": "manuel",
    "email": "rojas@email.com",
    "password": "1234",
    "phone": "666666666",
    "userStatus": 1
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print('Response of first call (create user)')
print(response.text)


# check the user has been created
url = "https://petstore.swagger.io/v2/user/rojas"

response = requests.request("GET", url)
print('response to request get the user rojas')
print(response.text)


# get all the pets with the status sold
url = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"

response = requests.request("GET", url)

print('list pets response')
print(response.text)
pets_list = list(map(get_id_name, response.json()))

print('full list of id-name')
print(pets_list)
pets = Pet(pets_list)

print('result of how many pets have equal names')
print(pets.count_eq_names())


#this is another implementation with apache beam, if you want to try it you only need to install the apache-beam dependency and run: python request.py --runner=DirectRunner
'''
def getIdName(element):
    if 'id' in element and 'name' in element:
        return (element['id'], element['name'])
    else:
        pass

def quit_none_values(element):
    if element is not None:
        return element


with beam.Pipeline() as p:
    data: PCollection = (p | beam.Create(response.json()) #create a dataset with the body of the response
                         | beam.Map(getIdName) #remove all the properties except id and name
                         | beam.Filter(quit_none_values) #quit the None values
                         )
    print('Print of the second part with the intermediate result and the final result')
    intermediate_values:PCollection = (data | beam.Map(print)
                 ) #print the intermediate result
    pets: PCollection = (data
                         | beam.Map(lambda element: element[1]) #quit the id
                         | beam.Map(lambda element: (element, 1)) #add value one per name and create a tuple (name, 1)
                         | beam.CombinePerKey(sum) #sum all the number per key (all the number are 1 that is because the result is the count of occurrences)
                         | 'print the result' >> beam.Map(print)
                         | beam.io.WriteToText('output.txt') #write the result in a external file
                         )

'''
