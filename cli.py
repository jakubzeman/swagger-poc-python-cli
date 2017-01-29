import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntrypointApi()
msg = swagger_client.Plus(5, 3) # Plus | json serialization of {@link Plus}

try: 
    # Count a result of plus operation
    api_response = api_instance.plus(msg)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EntrypointApi->plus: %s\n" % e

