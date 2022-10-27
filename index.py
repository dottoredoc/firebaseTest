import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
cred = credentials.Certificate("test-6145b-firebase-adminsdk-ewt22-3cfb0a1c55.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection('utenti')
docs = users_ref.stream()

doc_ref = db.collection('utenti').document('alovelace')
doc_ref.set({
    'nome': 'Ada',
    'cognome': 'Lovelace',
})

for doc in docs:
    print(doc.to_dict()['nome'])
   #print(f'{doc.id} => {doc.to_dict()}')

print("------------")

utenti_ref = db.collection("utenti")
query = utenti_ref.order_by("nome").limit_to_last(2)
results = query.get()
for doc in results:
    print(doc.to_dict()['nome'])