#Windows service check using python

import psutil

def getService(name):

        service = None
        try:
            service = psutil.win_service_get(name)
            service = service.as_dict()
        except Exception as ex:
            print (ex)

        return service

service = getService('KeyIso')

print (service)

if service:

        print ("service found")
else:

    print ("service not found")


if service and service['status'] == 'running' :

        print ("service is running")
else :

        print ("service is not running")

