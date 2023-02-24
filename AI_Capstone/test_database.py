import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('aquaspecta-creds.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def update_status_flags(inDistress, isDrowning, maxedLeaves):
    # Reference to document containing status flags
    statRef = db.collection(u'user1').document(u'status-flags')

    # For updating the three status flags
    statRef.update({u'inDistress': inDistress})
    statRef.update({u'isDrowning': isDrowning})
    statRef.update({u'maxedLeaves': maxedLeaves})

    # Reference to document containing user settings
    doc_ref = db.collection(u'user1').document(u'settings')

    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        print(u'No such document!')


