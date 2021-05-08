import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Credential json dosyanızı aynı klasöre yükleyin
cred = credentials.Certificate("serviceAccountKey.json")

# Firebase Database URL'inizi ekleyin
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://robowars-783a9-default-rtdb.firebaseio.com'
})

# Database en üst referansızın adını girin
ref = db.reference('robowars_deniz')

# Açı, yön ve motor durumlarını ilgili isimlerle Firebase'den çekin
angle = ref.get()['angle']
direction = ref.get()['direction']
motor_state = ref.get()['motor_state']


# Tüm datayı diğer bir Python dosyasından hızlıca çağırın
def get_from_firebase():
    return ref.get()
