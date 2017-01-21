import requests
import base64
import secrets

class FitbitClient():

    # SECRETS

    # These get imported from secrets.py, which is in the .gitnorefile. Make sure to
    # create this file and set them yourself. To get them for you own application, log 
    # into the fitbit developer website and create a new application. You will then need
    # to visit the fitbit oAuth URL in your web browser to pull back the application code
    # using your own details, see https://dev.fitbit.com/docs/oauth2/#authorization-page

    APP_CLIENTID = secrets.APP_CLIENTID
    APP_CLIENTSECRET = secrets.APP_CLIENTSECRET

    def auth(self):
        print("Authenticating")

        auth_string = self.APP_CLIENTID + ":" + self.APP_CLIENTSECRET
        encoded_auth_string = base64.b64encode( auth_string.encode() )

        #print(auth_string)
        #print(encoded_auth_string)
        #print( base64.b64decode(encoded_auth_string) )

        # Set the headers
        header_authorisation = "Basic %s" % encoded_auth_string.decode()
        header_content_type = 'application/x-www-form-urlencoded'
        headers = {'Authorization': header_authorisation, 'Content-Type' : header_content_type }

        # Set the payload
        #body_clientID =
        #body_grantType =
        #body_redirectURL = 
        #body_code = 
        payload = {}

        r = requests.post("https://api.fitbit.com/oauth2/token", headers=headers, params=payload )


if __name__ == "__main__":
    print("--- FITBIT ---\n")

    client = FitbitClient()
    client.auth()



