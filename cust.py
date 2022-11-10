#! python
import sys
sys.path.append('c:/program files/python310/lib/site-packages')
import base64, curlify, hashlib, hmac, requests
from datetime import datetime  
from typing import Dict

class LogixSecureAPICalls():
    server = None
    sharedKey = None
    secretKey = None
    apiBasePath = None
    __empty__ = ""
    __assign__ = "="
    __and__ = "&"
    __parms__ = "?"
    __open_http__ = "http"
    __secure_http__ = "https"
    __port__ = ":"
    __server__ = "//"
    __folder__ = "/"
    __authorizationKey__ = "Authorization"
    __contentTypeKey__ = "Content-Type"
    __dateKey__ = "Date"
    __accessKey__ = "AccessKey"
    __urlKey__ = "url"
    __headersKey__ = "headers"
    __dataKey__ = "data"
    __getMethod__ = "GET"
    __postMethod__ = "POST"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, apiBasePath:str = None, server: str = None, sharedKey: str = None, secretKey: str = None, *args, **kwargs):
        self.apiBasePath = apiBasePath
        self.server = server
        self.sharedKey = sharedKey
        self.secretKey = secretKey

    def __repr__(self) -> str:
        return f"{type(self).__name__}(apiBasePath={self.apiBasePath}, server={self.server}, sharedKey={self.sharedKey}, secretKey={self.secretKey})"

    def genParmsStr(self, genParmsStrRawParmsDict: dict = None):
        genParmsStrParmsDict = dict(genParmsStrRawParmsDict)
        genParmsStrResult = self.__empty__
        for genParmsStrIdx, genParmsStrParm in enumerate([*genParmsStrParmsDict.keys()]):
            if genParmsStrIdx == 0:
                genParmsStrResult = f"{genParmsStrParm}{self.__assign__}{genParmsStrParmsDict[genParmsStrParm]}"
            else:
                genParmsStrResult = f"{genParmsStrResult}{self.__and__}{genParmsStrParm}{self.__assign__}{genParmsStrParmsDict[genParmsStrParm]}"
        return genParmsStrResult

    def genURLPathWParmsStr(self, genURLPathWParmsStrRawHTTPPath: str, genURLPathWParmsStrRawParmsDict: dict = None):
        genURLPathWParmsStrHTTPPath = str(genURLPathWParmsStrRawHTTPPath)
        if genURLPathWParmsStrRawParmsDict == None:
            return f"{self.apiBasePath}{self.__folder__}{genURLPathWParmsStrHTTPPath}"
        elif len(dict(genURLPathWParmsStrRawParmsDict).keys()) == 0:
            return self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genURLPathWParmsStrHTTPPath)
        elif self.__parms__ in genURLPathWParmsStrHTTPPath:
            genURLPathWParmsStrParmsDict = dict(genURLPathWParmsStrRawParmsDict)
            return f"{self.apiBasePath}{self.__folder__}{genURLPathWParmsStrHTTPPath}{self.__and__}{self.genParmsStr(genParmsStrRawParmsDict=genURLPathWParmsStrParmsDict)}"
        else:
            genURLPathWParmsStrParmsDict = dict(genURLPathWParmsStrRawParmsDict)
            return f"{self.apiBasePath}{self.__folder__}{genURLPathWParmsStrHTTPPath}?{self.genParmsStr(genParmsStrRawParmsDict=genURLPathWParmsStrParmsDict)}"

    def getValidHTTPProtocolStr(self, getValidHTTPProtocolStrRawHTTPProtocol: str):
        getValidHTTPProtocolStrHTTPProtocol = str(getValidHTTPProtocolStrRawHTTPProtocol)
        match getValidHTTPProtocolStrHTTPProtocol:
            case self.__open_http__:
                return getValidHTTPProtocolStrHTTPProtocol
            case self.__secure_http__:
                return getValidHTTPProtocolStrHTTPProtocol
            case _:
                return self.__open_http__

    def getValidHTTPMethodStr(self, getValidHTTPMethodStrRawMethod: str):
        getValidHTTPMethodStrMethod = str(getValidHTTPMethodStrRawMethod)
        match getValidHTTPMethodStrMethod:
            case self.__getMethod__:
                return getValidHTTPMethodStrMethod
            case self.__postMethod__:
                return getValidHTTPMethodStrMethod
            case _:
                return self.__getMethod__

    def genFullURLWParmsStr(self, genFullURLWParmsStrRawHTTPPath: str, genFullURLWParmsStrRawServer: str = None, genFullURLWParmsStrRawParmsDict: dict = None, genFullURLWParmsStrRawHTTPProtocol: str = None, genFullURLWParmsStrRawHTTPPort: int = None):
        genFullURLWParmsStrHTTPPath = str(genFullURLWParmsStrRawHTTPPath)
        if genFullURLWParmsStrRawServer == None: genFullURLWParmsStrServer = self.server
        else: genFullURLWParmsStrServer = str(genFullURLWParmsStrRawServer)
        genFullURLWParmsStrParmsDict = dict(genFullURLWParmsStrRawParmsDict)
        if genFullURLWParmsStrRawHTTPProtocol == None: genFullURLWParmsStrHTTPProtocol = self.__open_http__
        else: genFullURLWParmsStrHTTPProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=genFullURLWParmsStrRawHTTPProtocol)
        if genFullURLWParmsStrRawHTTPPort == None: return f"{genFullURLWParmsStrHTTPProtocol}{self.__port__}{self.__server__}{genFullURLWParmsStrServer}{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genFullURLWParmsStrHTTPPath, genURLPathWParmsStrRawParmsDict=genFullURLWParmsStrParmsDict)}"
        else:
            genFullURLWParmsStrHTTPPort = int(genFullURLWParmsStrRawHTTPPort)
            return f"{genFullURLWParmsStrHTTPProtocol}{self.__port__}{self.__server__}{genFullURLWParmsStrServer}{self.__port__}{genFullURLWParmsStrHTTPPort}{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genFullURLWParmsStrHTTPPath, genURLPathWParmsStrRawParmsDict=genFullURLWParmsStrParmsDict)}"

    def genAuthHeadersDict(self, genAuthHeadersDictRawHTTPMethod: str, genAuthHeadersDictRawContentType: str, genAuthHeadersDictRawHTTPPath: str, genAuthHeadersDictRawParmsDict: dict = None, genAuthHeadersDictRawTimestamp: datetime = None) -> Dict:    
        genAuthHeadersDictHTTPMethod = self.getValidHTTPMethodStr(getValidHTTPMethodStrRawMethod=genAuthHeadersDictRawHTTPMethod)
        genAuthHeadersDictContentType = str(genAuthHeadersDictRawContentType)
        genAuthHeadersDictHTTPPath = str(genAuthHeadersDictRawHTTPPath)
        if genAuthHeadersDictRawTimestamp == None: genAuthHeadersDictTimestamp = datetime.utcnow()
        else: genAuthHeadersDictTimestamp = genAuthHeadersDictRawTimestamp
        if genAuthHeadersDictRawParmsDict == None: genAuthHeadersDictParmsDict = genAuthHeadersDictRawParmsDict
        else: genAuthHeadersDictParmsDict = dict(genAuthHeadersDictRawParmsDict)
        genAuthHeadersDictURLPathWParms = f"{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genAuthHeadersDictHTTPPath, genURLPathWParmsStrRawParmsDict=genAuthHeadersDictParmsDict)}"
        genAuthHeadersDictHeadersDict = {
            self.__authorizationKey__: None,
            self.__contentTypeKey__: genAuthHeadersDictContentType,
            self.__dateKey__: genAuthHeadersDictTimestamp.strftime("%a, %d %b %Y %H:%M:%S") + ' GMT'
        }
        genAuthHeadersDictZuluTimestamp  = genAuthHeadersDictTimestamp.strftime("%Y-%m-%dT%H:%M:%S")+ '.'+'000Z'
        genAuthHeadersDictUniqueKey = self.secretKey + genAuthHeadersDictZuluTimestamp    
        genAuthHeadersDictSignableContent = str.format('{0}\n{1}\n{2}', genAuthHeadersDictHTTPMethod, genAuthHeadersDictURLPathWParms, genAuthHeadersDictContentType)
        genAuthHeadersDictSignatureHash = hmac.new(genAuthHeadersDictUniqueKey.encode(), genAuthHeadersDictSignableContent.encode(), hashlib.sha512).digest()
        genAuthHeadersDictBase64SignatureHash = base64.b64encode(genAuthHeadersDictSignatureHash).decode()
        genAuthHeadersDictHeadersDict[self.__authorizationKey__] = str.format('{0} {1}:{2}', self.__accessKey__, self.sharedKey, genAuthHeadersDictBase64SignatureHash)
        return genAuthHeadersDictHeadersDict

    def genGetDict(self, genGetDictRawContentType: str, genGetDictRawHTTPPath: str, genGetDictRawServer: str = None, genGetDictRawParmsDict: dict = None, genGetDictRawHTTPMethod: str = None, genGetDictRawHTTPProtocol: str = None, genGetDictRawHTTPPort: int = None, genGetDictRawTimestamp: datetime = None):
        genGetDictContentType = str(genGetDictRawContentType)
        genGetDictHTTPPath = str(genGetDictRawHTTPPath)
        if genGetDictRawServer == None:  genGetDictServer = self.server
        else: genGetDictServer = str(genGetDictRawServer)
        if genGetDictRawParmsDict == None: genGetDictParmsDict = genGetDictRawParmsDict
        else: genGetDictParmsDict = dict(genGetDictRawParmsDict)
        if genGetDictRawHTTPMethod == None: genGetDictHTTPMethod = self.__getMethod__
        else: genGetDictHTTPMethod = self.getValidHTTPMethodStr(getValidHTTPMethodStrRawMethod=genGetDictRawHTTPMethod)
        if genGetDictRawHTTPProtocol == None: genGetDictHTTPProtocol = self.__open_http__
        else: genGetDictHTTPProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=genGetDictRawHTTPProtocol)
        if genGetDictRawHTTPPort == None: genGetDictHTTPPort = genGetDictRawHTTPPort
        else: genGetDictHTTPPort = int(genGetDictRawHTTPPort)
        if genGetDictRawTimestamp == None: genGetDictTimestamp = datetime.utcnow()
        else: genGetDictTimestamp = genGetDictRawTimestamp
        genGetDictURLPathWParmsStr = self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genGetDictHTTPPath, genURLPathWParmsStrRawParmsDict=genGetDictParmsDict)
        return {
            self.__urlKey__ : self.genFullURLWParmsStr(genFullURLWParmsStrRawHTTPPath = genGetDictHTTPPath, genFullURLWParmsStrRawServer = genGetDictServer, genFullURLWParmsStrRawParmsDict = genGetDictParmsDict, genFullURLWParmsStrRawHTTPProtocol = genGetDictHTTPProtocol, genFullURLWParmsStrRawHTTPPort = genGetDictHTTPPort),
            self.__headersKey__ : self.genAuthHeadersDict(genAuthHeadersDictRawHTTPMethod = genGetDictHTTPMethod, genAuthHeadersDictRawHTTPPath = genGetDictHTTPPath, genAuthHeadersDictRawParmsDict = genGetDictParmsDict, genAuthHeadersDictRawContentType = genGetDictContentType, genAuthHeadersDictRawTimestamp = genGetDictTimestamp)
        }

    def genPostDict(self, genPostDictRawContentType: str, genPostDictRawHTTPPath: str, genPostDictRawServer: str = None, genPostDictRawParmsDict: dict = None, genPostDictRawHTTPMethod: str = None, genPostDictRawHTTPProtocol: str = None, genPostDictRawHTTPPort: str = None, genPostDictRawTimestamp: datetime = None, genPostDictRawDataDict: dict = None):
        genPostDictContentType = str(genPostDictRawContentType)
        genPostDictHTTPPath = str(genPostDictRawHTTPPath)
        if genPostDictRawServer == None:  genPostDictServer = self.server
        else: genPostDictServer = str(genPostDictRawServer)
        if genPostDictRawParmsDict == None: genPostDictParmsDict = genPostDictRawParmsDict
        else: genPostDictParmsDict = dict(genPostDictRawParmsDict)
        genPostDictURLPathWParmsStr = self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genPostDictHTTPPath, genURLPathWParmsStrRawParmsDict=genPostDictParmsDict) 
        if genPostDictRawHTTPMethod == None: genPostDictHTTPMethod = self.__postMethod__
        else: genPostDictHTTPMethod = self.getValidHTTPMethodStr(getValidHTTPMethodStrRawMethod=genPostDictRawHTTPMethod)
        if genPostDictRawHTTPProtocol == None: genPostDictHTTPProtocol = self.__open_http__
        else: genPostDictHTTPProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=genPostDictRawHTTPProtocol)
        if genPostDictRawHTTPPort == None: genPostDictHTTPPort = genPostDictRawHTTPPort
        else: genPostDictHTTPPort = str(genPostDictRawHTTPPort)
        if genPostDictRawTimestamp == None: genPostDictTimestamp = datetime.utcnow()
        else: genPostDictTimestamp = genPostDictRawTimestamp
        if genPostDictRawDataDict == None: genPostDictDataDict = {}
        else: genPostDictDataDict = dict(genPostDictRawDataDict)
        return {
            self.__urlKey__ : self.genFullURLWParmsStr(genFullURLWParmsStrRawHTTPPath = genPostDictHTTPPath, genFullURLWParmsStrRawServer = genPostDictServer, genFullURLWParmsStrRawParmsDict = genPostDictParmsDict, genFullURLWParmsStrRawHTTPProtocol = genPostDictHTTPProtocol, genFullURLWParmsStrRawHTTPPort = genPostDictHTTPPort),
            self.__dataKey__ : genPostDictDataDict,
            self.__headersKey__ : self.genAuthHeadersDict(genAuthHeadersDictRawHTTPMethod = genPostDictHTTPMethod, genAuthHeadersDictRawHTTPPath = genPostDictHTTPPath, genAuthHeadersDictRawParmsDict = genPostDictParmsDict, genAuthHeadersDictRawContentType = genPostDictContentType, genAuthHeadersDictRawTimestamp = genPostDictTimestamp)
        }

class LogixCustomerAPI(LogixSecureAPICalls):
    GUID = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, GUID = None, apiBasePath:str = None, server: str = None, sharedKey: str = None, secretKey: str = None, *args, **kwargs):
        super().__init__(apiBasePath=apiBasePath, server=server, sharedKey=sharedKey, secretKey=secretKey, *args, **kwargs)
        self.GUID = GUID

    def __repr__(self) -> str:
        return f"{type(self).__name__}(server={self.server}, sharedKey={self.sharedKey}, secretKey={self.secretKey}, GUID={self.GUID})"

    def generateCustomerInquiryCustomerPKStatusInformationDictionary(self,
            job_id:str,
            server:str = None,
            httpProtocol:str = None,
            httpPort:str = None,
            timestamp = None):
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.server
        contentType = "application/x-www-form-urlencoded"
        httpMethod = self.__getMethod__

        if httpProtocol == None: httpProtocol = self.__open_http__
        else: httpProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=httpProtocol)

        httpPath = "CustomerPKStatus"
        parameters = {"JobId" : job_id}
        return self.genGetDict(genGetDictRawServer = server, genGetDictRawHTTPPath = httpPath, genGetDictRawParmsDict=parameters, genGetDictRawContentType = contentType, genGetDictRawHTTPMethod = httpMethod, genGetDictRawHTTPProtocol = httpProtocol, genGetDictRawHTTPPort = httpPort, genGetDictRawTimestamp = timestamp)

    def getCustomerInquiryCustomerPKStatus(self,
            job_id: str,
            server: str = None,
            timestamp = None):
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.server
        info = self.generateCustomerInquiryCustomerPKStatusInformationDictionary(server = server, job_id = job_id, timestamp = timestamp)
        return requests.get(url=info[self.__urlKey__], headers = info[self.__headersKey__])

    def generateCustomerInquiryExportCustomerPKInformationDictionary(self,
            StartPK:str,
            EncryptionKey:str,
            InitializationVector:str,
            GUID:str = None,
            server:str = None,
            httpProtocol:str = None,
            httpPort:str = None,
            timestamp = None):

        if GUID == None: GUID = self.GUID
        if timestamp == None: timestamp = datetime.utcnow()

        if httpProtocol == None: httpProtocol = self.__open_http__
        else: httpProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=httpProtocol)

        if server == None:  server = self.server
        contentType = "application/x-www-form-urlencoded"
        httpMethod = self.__postMethod__
        httpPath = "ExportCustomerPK"
        parameters = {}
        return self.genPostDict(genPostDictRawServer = server, genPostDictRawHTTPPath = httpPath, genPostDictRawParmsDict=parameters, genPostDictRawContentType = contentType, genPostDictRawHTTPMethod = httpMethod, genPostDictRawHTTPProtocol = httpProtocol, genPostDictRawHTTPPort = httpPort, genPostDictRawTimestamp = timestamp, genPostDictRawDataDict = {
                'GUID': GUID,
                'StartPK': StartPK,
                'EncryptionKey': EncryptionKey,
                'InitializationVector': InitializationVector
            })

    def postCustomerInquiryExportCustomerPK(self,
            StartPK:str,
            EncryptionKey:str,
            InitializationVector:str,
            GUID:str = None,
            server:str = None,
            timestamp = None):
        if GUID == None: GUID = self.GUID
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.server
        info = self.generateCustomerInquiryExportCustomerPKInformationDictionary(GUID = GUID, StartPK = StartPK, EncryptionKey = EncryptionKey, InitializationVector = InitializationVector, server = server, timestamp = timestamp)
        return requests.post(url=info[self.__urlKey__], data=info[self.__dataKey__], headers=info[self.__headersKey__])

def testGet(custAPI):
    # Get test
    getReq = custAPI.getCustomerInquiryCustomerPKStatus(212)
    print('Get:')
    print(curlify.to_curl(getReq.request))
    print(getReq)
    print(getReq.content)

def testPost(custAPI):
    # Post test
    postReq = custAPI.postCustomerInquiryExportCustomerPK('52398150', '1Tu/S37K0ZTuy3kSIiSngXKB36oSaIe4D0fcrrlB7bw=', 'eFZsnfQu2o2fDg1p2qdFQQ==')
    print('Post:')
    print(curlify.to_curl(postReq.request))
    print(postReq)
    print(postReq.content)

def testObject():
    custAPI = LogixCustomerAPI(server="10.37.24.156", sharedKey="cc73bfec4d774611b0e254fe7beea49a", secretKey="f2d7fea9a8d84d4b897160b2b90d9e97", GUID="234a86cc-1995-4886-82ea-8808cc9ec919", apiBasePath = "Connectors/CustomerInquiry.asmx")
    print(custAPI)
    testGet(custAPI)
    testPost(custAPI)


# from urllib.request import Request
# import requests
# import hashlib
# import hmac
# import base64
# import time
# import curlify

# from datetime import datetime  



# timestamp = datetime.utcnow()

# hh = '20'
# mm = '22'
# ss = '02'
# jobid = '212'

# nonce  = timestamp.strftime("%Y-%m-%dT%H:%M:%S")+ '.'+'000Z'
# nonce = f'2022-11-08T{hh}:{mm}:{ss}.000Z'
# print("Current timestamp", nonce )
# uniqueKey = 'f2d7fea9a8d84d4b897160b2b90d9e97' + nonce    
# print(f"unique key: {uniqueKey}")



# signableContent = 'POST' + '\n' + '/Connectors/CustomerInquiry.asmx/ExportCustomerPK' + '\n' + 'application/x-www-form-urlencoded'

# signableContentGet = 'GET' + '\n' + '/Connectors/CustomerInquiry.asmx/CustomerPKStatus?JobId=212' + '\n' + 'application/x-www-form-urlencoded'
# print(signableContentGet)

# signature_hash = hmac.new(uniqueKey.encode(), signableContent.encode(), hashlib.sha512).digest()
# signature_hashGet = hmac.new(uniqueKey.encode(), signableContentGet.encode(), hashlib.sha512).digest()
# base64_signature_hash = base64.b64encode(signature_hash).decode()
# #print(f"hash: {base64_signature_hash}")
# base64_signature_hashGet = base64.b64encode(signature_hashGet).decode()
# print(f"hash: {base64_signature_hashGet}")



# AuthKey = 'AccessKey cc73bfec4d774611b0e254fe7beea49a:' + base64_signature_hash
# #print(f"authkey: {AuthKey}")
# AuthKeyGet = 'AccessKey cc73bfec4d774611b0e254fe7beea49a:' + base64_signature_hashGet
# print(f"authkey: {AuthKeyGet}")




# headers = {
#   'Authorization':AuthKey,
#   'Date':f'Tue, 08 Nov 2022 {hh}:{mm}:{ss} GMT',
#   'Content-Type':'application/x-www-form-urlencoded'#,
#   #'User-Agent' : 'PostmanRuntime/7.29.2'
# }

# headersGet = {
#   'Authorization':AuthKeyGet,
#   'Date':f'Tue, 08 Nov 2022 {hh}:{mm}:{ss} GMT',
#   'Content-Type':'application/x-www-form-urlencoded'#,
#   #'Connection': None,
#   #'Accept-Encoding': None,
#   #'User-Agent':None#,
#   #'User-Agent' : 'PostmanRuntime/7.29.2'
# }
# print(headersGet)


# url = 'http://10.37.24.156/connectors/customerinquiry.asmx/ExportCustomerPK'
# urlGet = f'http://10.37.24.156/connectors/customerinquiry.asmx/CustomerPKStatus?JobId={jobid}'
# print(urlGet)
# data={'GUID': '234a86cc-1995-4886-82ea-8808cc9ec919',
#       'StartPK': '52398150',
#       'EncryptionKey': '1Tu/S37K0ZTuy3kSIiSngXKB36oSaIe4D0fcrrlB7bw=',
#       'InitializationVector': 'eFZsnfQu2o2fDg1p2qdFQQ=='
#      }
# #response = requests.post(url,data=data, headers=headers)
# responseGet = requests.get(urlGet, headers=headersGet)
# #response = requests.post(url, data = data, json = None, params = None, headers = headers)

# #print(f"request:  {response.request}")
# print(f"request:  {responseGet.request}")


# #print(f"{curlify.to_curl(response.request)} \n")
# print(f"{curlify.to_curl(responseGet.request)} \n")

# #print(f"response:  {response}")
# print(f"response:  {responseGet}")
# # print(response.request.url)
# # print(response.request.body)
# # print(response.request.headers)





# sharedKey = 'cc73bfec4d774611b0e254fe7beea49a'
# secretKey = 'f2d7fea9a8d84d4b897160b2b90d9e97'


# def generateAuthHeaders(httpMethod:str, httpPath:str, contentType:str) -> Dict:    
#     timestamp = datetime.utcnow()
#     headers = {
#         "Authorization": None,
#         "Content-Type": contentType,
#         "Date": timestamp.strftime("%a, %d %b %Y %H:%M:%S") + ' GMT'
#     }
#     nonce  = timestamp.strftime("%Y-%m-%dT%H:%M:%S")+ '.'+'000Z'
#     uniqueKey = secretKey + nonce    
#     signableContent = str.format('{0}\n{1}\n{2}', httpMethod, httpPath, contentType)
#     signature_hash = hmac.new(uniqueKey.encode(), signableContent.encode(), hashlib.sha512).digest()
#     base64_signature_hash = base64.b64encode(signature_hash).decode()
#     headers['Authorization'] = str.format('AccessKey {0}:{1}', sharedKey, base64_signature_hash)

#     return headers



# Get test
# getReq = requests.get(
#             url='http://10.37.24.156/Connectors/CustomerInquiry.asmx/CustomerPKStatus?JobId=212',
#             headers=generateAuthHeaders('GET', '/Connectors/CustomerInquiry.asmx/CustomerPKStatus?JobId=212', 'application/x-www-form-urlencoded')
#         )
# print('Get:')
# print(curlify.to_curl(getReq.request))
# print(getReq)

# # Post test
# postReq = requests.post(
#             url='http://10.37.24.156/Connectors/CustomerInquiry.asmx/ExportCustomerPK',
#             data={
#                 'GUID': '234a86cc-1995-4886-82ea-8808cc9ec919',
#                 'StartPK': '52398150',
#                 'EncryptionKey': '1Tu/S37K0ZTuy3kSIiSngXKB36oSaIe4D0fcrrlB7bw=',
#                 'InitializationVector': 'eFZsnfQu2o2fDg1p2qdFQQ=='
#             },
#             headers=generateAuthHeaders('POST', '/Connectors/CustomerInquiry.asmx/ExportCustomerPK', 'application/x-www-form-urlencoded')
#         )
# print('Post:')
# print(curlify.to_curl(postReq.request))
# print(postReq)


testObject()