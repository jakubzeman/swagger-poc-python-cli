# swagger_client.EntrypointApi

All URIs are relative to *http://localhost/http://slc07ifc.us.oracle.com:8181/http://slc06xlq.us.oracle.com:7103/paas/bdcs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plus**](EntrypointApi.md#plus) | **POST** /entry-point/plus | Count a result of plus operation


# **plus**
> PlusResult plus(msg)

Count a result of plus operation

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntrypointApi()
msg = swagger_client.Plus() # Plus | json serialization of {@link Plus}

try: 
    # Count a result of plus operation
    api_response = api_instance.plus(msg)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EntrypointApi->plus: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg** | [**Plus**](Plus.md)| json serialization of {@link Plus} | 

### Return type

[**PlusResult**](PlusResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

