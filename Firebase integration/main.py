import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://attendancetest-33ab4-default-rtdb.firebaseio.com/'
})
