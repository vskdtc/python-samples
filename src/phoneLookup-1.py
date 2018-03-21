#!/usr/bin/python
# Python Example code for NumberPortabilityLookup.com

import httplib

# Put your username and password here:
username="username"
password="secret"

# This is the number to be queried:
number="447788450450"

# Call API to perform HLR Query
conn = httplib.HTTPConnection("api.comcetera.com")
conn.request("GET", "/npl?user="+username+"&pass="+password+"&msisdn="+number+"&apiver=2.4")
data = conn.getresponse().read()
conn.close()


# Parse the response
response=data.split("\n")

# First line indicates success of the query
if response[0]=="QUERYOK":

    # Response returned OK - now read the data into variables

    # This is a basic example querying a single number.
    # If you queried more than one number in a single API call by delimiting MSISDNs
    # with commas, you could extend the block below to loop through lines of response[]
    # for each pair of msisdn/hlrdata until you reach response[n]=="ENDBATCH"

    (msisdn,hlrdata)=response[1].split(" ",2)
    (plmn,msc,imsi)=hlrdata.split(",",3)

    # Use the data as needed. For this example we will just print it to console:

    print("MSISDN ",msisdn)
    print("MSC    ",msc)
    print("IMSI   ",imsi)

else:
    # If we didn't get "QUERYOK", something broke - tell somebody!

    print("Lookup error:",response[0])
