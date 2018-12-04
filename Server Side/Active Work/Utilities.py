#Firebase Timestamping
def __GenerateConnection__():
    #Create a secure connection to the Firestore REST API using google Oauth2
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    scopes = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/firebase.database"]

    credentials = service_account.Credentials.from_service_account_file( r'C:\Users\thepe_000\Desktop\PP5\Void Scribe\Server Side\Active Work\void-scribe-firebase-adminsdk-xtf9j-a419db8670.json', scopes=scopes)

    authed_session = AuthorizedSession(credentials)

    return authed_session

authed_session = __GenerateConnection__()

def GetTimeStamp(authed_session = authed_session):
    #Use authenticated session to retreive the current timestamp
    import json
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import service_account
    my_data = dict()
    my_data["timestamp"] = {".sv": "timestamp"}
    json_data = json.dumps(my_data).encode()

    response = authed_session.put("https://void-scribe.firebaseio.com/TEST_COLLECTION/TEST_DOCUMENT_2.json", data=json_data)

    if response.status_code != 200:
        raise Exception("Communication With The Firebase REST Server Unsuccesful")

    return response.json()['timestamp']

def CD(directory):
    #Changes the working directory to the filepath
    #Returns a callback to revert to initial directory
    #ex. usage
    #temp = CD("Misc")
    #import Utilities
    #temp()
    #This will import Utilites from the Misc directory
    import os
    initial_path = os.getcwd()
    def ReturnToPrevousDirectory():
        nonlocal initial_path
        os.chdir(initial_path)
    os.chdir(directory)
    return ReturnToPrevousDirectory

