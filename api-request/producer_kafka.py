from kafka import KafkaProducer
from api_request import fetch_data
import json
topic = 'user_topic'
import time

def formated_data():
    raw_data = fetch_data()
    result_data = raw_data['results'][0]
    
    data = {}
    data['name'] = result_data['name']['first'] + result_data['name']['last']
    data['gender'] = result_data['gender']
    data['email'] = result_data['email']
    data['phone'] =result_data['phone']
    data['address'] = f"{result_data['location']['street']['number']}, "\
                    f"{result_data['location']['street']['name']}, {result_data['location']['city']}, "\
                    f"{result_data['location']['state']}, {result_data['location']['country']}"
                    
    data['picture'] = result_data['picture']['medium']
    data['username'] = result_data['login']['username']
    data['registered_date'] = result_data['registered']['date']
    
    
    return(data)

def producer_kafka():
    print(f"Sending data to topic: user_topic ........")
    producer = KafkaProducer(bootstrap_servers= ['kafka:9092'])
    try:
        for i in range(10): 
            data = formated_data()
            producer.send("user_topic", json.dumps(data).encode('utf-8'))
        print("Successfully!")
    except Exception as e:
        print(f"An error occured: {e}")
        raise
