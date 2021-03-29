##############################################
#### Written By: SATYAKI DE               ####
#### Written On: 20-Mar-2021              ####
#### Modified On 20-Mar-2021              ####
####                                      ####
#### Objective: Calling Azure dynamic API ####
##############################################

import io
import json
import logging

from fdk import response

import clsAzureAPI as ca

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn


def handler(ctx, data: io.BytesIO = None):
    try:
        email = "default@gmail.com"

        # Checking individual elements
        try:
            body = json.loads(data.getvalue())
            email = body.get("email")
        except (Exception, ValueError) as ex:
            logging.getLogger().info('error parsing json payload: ' + str(ex))

        logging.getLogger().info("Calling Oracle Python getCovidData function!")

        # Create the instance of the Mock Mulesoft API Class
        x1 = ca.clsAzureAPI()

        # Let's pass this to our map section
        retJson = x1.searchQry()

        # Converting JSon to Pandas Dataframe for better readability
        # Capturing the JSON Payload
        resJson = json.loads(retJson)

        return response.Response(
            ctx, response_data=json.dumps(
                {"status":"Success", "message": resJson}),
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        x = str(e)

        return response.Response(
            ctx, response_data=json.dumps(
                {"status":"Failed", "message": x}),
            headers={"Content-Type": "application/json"}
        )
