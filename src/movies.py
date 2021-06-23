import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)


def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(movie_id)
    item = {
        'pk': movie_id,
        'sk': 'info',
        'tittle': body["tittle"],
        'actors': body["actors"],
        'year': body["year"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getMovieByRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    movie_id = path.split("/")[-3] # ["user", "id"]
    body = json.loads(event["body"])
    response = table.get_item(
        Key={
            'pk': room_id,
            'sk': movie_id
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def getRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': room_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getPerson(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    person_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': person_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putPeopleList(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(room_id)
    item = {
        'pk': room_id,
        'sk': 'info',
        'room_list': body["room_list"],

    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }