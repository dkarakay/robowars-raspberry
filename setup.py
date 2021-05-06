import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://robowars-783a9-default-rtdb.firebaseio.com'
})

ref = db.reference('robowars_deniz')

angle = ref.get()['angle']
direction = ref.get()['direction']
motor_state = ref.get()['motor_state']

print(f"angle: {angle}")
print(f"direction: {direction}")
print(f"motor_state: {motor_state}")
