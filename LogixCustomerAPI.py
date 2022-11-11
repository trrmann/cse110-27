#! python
import sys
sys.path.append('c:/program files/python310/lib/site-packages')
import base64, curlify, hashlib, hmac, requests
from datetime import datetime  
from typing import Dict

class LogixSecureAPICalls():
    __defAPIBasePath__ = None
    __defServer__ = None
    __defSharedKey__ = None
    __defSecretKey__ = None
    __defGUID__ = None
    __defPathDict__ = None
    __server__ = None
    __sharedKey__ = None
    __secretKey__ = None
    __apiBasePath__ = None
    __GUID__ = None
    __pathDict__ = None
    __empty__ = ""
    __assign__ = "="
    __and__ = "&"
    __parms__ = "?"
    __open_http__ = "http"
    __secure_http__ = "https"
    __port__ = ":"
    __serverToken__ = "//"
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
    __pathDictPathKey__ = "path"
    __pathDictMethodsKey__ = "methods"
    __pathDictParmsSpecKey__ = "parmsSpec"
    __pathDictDataSpecKey__ = "dataSpec"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, GUID = None, apiBasePath:str = None, pathDict: dict = None, server: str = None, sharedKey: str = None, secretKey: str = None, *args, **kwargs):
        self.setGUID(GUID)
        self.setAPIBasePath(apiBasePath)
        self.setServer(server)
        self.setSharedKey(sharedKey)
        self.setSecretKey(secretKey)
        self.setPathDict(pathDict)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(apiBasePath={self.getAPIBasePath()}, server={self.getServer()}, sharedKey={self.getSharedKey()}, secretKey={self.getSecretKey()}, GUID={self.getGUID()}, pathDictSize={self.getPathDictSize()})"

    def getPath(self, pathKey: str = None):
        if (pathKey == None) or (self.getPathDict() == None): return str(pathKey)
        elif pathKey in dict(self.getPathDict()).keys(): return str(self.getPathDict()[pathKey][self.__pathDictPathKey__])
        else: return str(pathKey)

    def getPathDict(self, defPathDict: dict = None):
        if (self.__pathDict__ == None) and (defPathDict == None):
            return self.__defPathDict__
        elif (self.__pathDict__ == None):
            return self.setPathDict(defPathDict)
        else:
            return dict(self.__pathDict__)

    def setPathDict(self, pathDict: dict = None):
        if pathDict == None: self.__pathDict__ = pathDict
        else: self.__pathDict__ = dict(pathDict)
        return pathDict

    def getPathDictSize(self):
        return len([*dict(self.getPathDict()).keys()])

    def getAPIBasePath(self, defAPIBasePath: str = None):
        if (self.__apiBasePath__ == None) and (defAPIBasePath == None):
            return self.__defAPIBasePath__
        elif (self.__apiBasePath__ == None):
            return self.setAPIBasePath(defAPIBasePath)
        else:
            return str(self.__apiBasePath__)

    def setAPIBasePath(self, apiBasePath: str = None):
        self.__apiBasePath__ = str(apiBasePath)
        return apiBasePath

    def getServer(self, defServer: str = None):
        if (self.__server__ == None) and (defServer == None):
            return self.__defServer__
        elif (self.__server__ == None):
            return self.setServer(defServer)
        else:
            return str(self.__server__)

    def setServer(self, server: str = None):
        self.__server__ = str(server)
        return server

    def getSharedKey(self, defSharedKey: str = None):
        if (self.__sharedKey__ == None) and (defSharedKey == None):
            return self.__defSharedKey__
        elif (self.__sharedKey__ == None):
            return self.setSharedKey(defSharedKey)
        else:
            return str(self.__sharedKey__)

    def setSharedKey(self, sharedKey: str = None):
        self.__sharedKey__ = str(sharedKey)
        return sharedKey

    def getSecretKey(self, defSecretKey: str = None):
        if (self.__secretKey__ == None) and (defSecretKey == None):
            return self.__defSecretKey__
        elif (self.__secretKey__ == None):
            return self.setSecretKey(defSecretKey)
        else:
            return str(self.__secretKey__)

    def setSecretKey(self, secretKey: str = None):
        self.__secretKey__ = str(secretKey)
        return secretKey

    def getGUID(self, defGUID: str = None):
        if (self.__GUID__ == None) and (defGUID == None):
            return self.__defGUID__
        elif (self.__GUID__ == None):
            return self.setGUID(defGUID)
        else:
            return str(self.__GUID__)

    def setGUID(self, GUID: str = None):
        self.__GUID__ = str(GUID)
        return GUID

    def genParmsStr(self, genParmsStrRawParmsDict: dict = None):
        genParmsStrParmsDict = dict(genParmsStrRawParmsDict)
        genParmsStrResult = self.__empty__
        for genParmsStrIdx, genParmsStrParm in enumerate([*genParmsStrParmsDict.keys()]):
            if genParmsStrIdx == 0:
                genParmsStrResult = f"{genParmsStrParm}{self.__assign__}{genParmsStrParmsDict[genParmsStrParm]}"
            else:
                genParmsStrResult = f"{genParmsStrResult}{self.__and__}{genParmsStrParm}{self.__assign__}{genParmsStrParmsDict[genParmsStrParm]}"
        return genParmsStrResult

    def genURLPathWParmsStr(self, genURLPathWParmsStrRawHTTPPathKey: str, genURLPathWParmsStrRawParmsDict: dict = None):
        genURLPathWParmsStrRawHTTPPath = self.getPath(pathKey=genURLPathWParmsStrRawHTTPPathKey)
        genURLPathWParmsStrHTTPPath = str(genURLPathWParmsStrRawHTTPPath)
        if genURLPathWParmsStrRawParmsDict == None:
            return f"{self.getAPIBasePath()}{self.__folder__}{genURLPathWParmsStrHTTPPath}"
        elif len(dict(genURLPathWParmsStrRawParmsDict).keys()) == 0:
            return self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPathKey=genURLPathWParmsStrHTTPPath)
        elif self.__parms__ in genURLPathWParmsStrHTTPPath:
            genURLPathWParmsStrParmsDict = dict(genURLPathWParmsStrRawParmsDict)
            return f"{self.getAPIBasePath()}{self.__folder__}{genURLPathWParmsStrHTTPPath}{self.__and__}{self.genParmsStr(genParmsStrRawParmsDict=genURLPathWParmsStrParmsDict)}"
        else:
            genURLPathWParmsStrParmsDict = dict(genURLPathWParmsStrRawParmsDict)
            return f"{self.getAPIBasePath()}{self.__folder__}{genURLPathWParmsStrHTTPPath}?{self.genParmsStr(genParmsStrRawParmsDict=genURLPathWParmsStrParmsDict)}"

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

    def genFullURLWParmsStr(self, genFullURLWParmsStrRawHTTPPathKey: str, genFullURLWParmsStrRawServer: str = None, genFullURLWParmsStrRawParmsDict: dict = None, genFullURLWParmsStrRawHTTPProtocol: str = None, genFullURLWParmsStrRawHTTPPort: int = None):
        genFullURLWParmsStrRawHTTPPath = self.getPath(pathKey=genFullURLWParmsStrRawHTTPPathKey)
        genFullURLWParmsStrHTTPPath = str(genFullURLWParmsStrRawHTTPPath)
        if genFullURLWParmsStrRawServer == None: genFullURLWParmsStrServer = self.getServer()
        else: genFullURLWParmsStrServer = str(genFullURLWParmsStrRawServer)
        genFullURLWParmsStrParmsDict = dict(genFullURLWParmsStrRawParmsDict)
        if genFullURLWParmsStrRawHTTPProtocol == None: genFullURLWParmsStrHTTPProtocol = self.__open_http__
        else: genFullURLWParmsStrHTTPProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=genFullURLWParmsStrRawHTTPProtocol)
        if genFullURLWParmsStrRawHTTPPort == None: return f"{genFullURLWParmsStrHTTPProtocol}{self.__port__}{self.__serverToken__}{genFullURLWParmsStrServer}{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPathKey=genFullURLWParmsStrHTTPPath, genURLPathWParmsStrRawParmsDict=genFullURLWParmsStrParmsDict)}"
        else:
            genFullURLWParmsStrHTTPPort = int(genFullURLWParmsStrRawHTTPPort)
            return f"{genFullURLWParmsStrHTTPProtocol}{self.__port__}{self.__serverToken__}{genFullURLWParmsStrServer}{self.__port__}{genFullURLWParmsStrHTTPPort}{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPathKey=genFullURLWParmsStrHTTPPath, genURLPathWParmsStrRawParmsDict=genFullURLWParmsStrParmsDict)}"

    def genAuthHeadersDict(self, genAuthHeadersDictRawHTTPMethod: str, genAuthHeadersDictRawContentType: str, genAuthHeadersDictRawHTTPPathKey: str, genAuthHeadersDictRawParmsDict: dict = None, genAuthHeadersDictRawTimestamp: datetime = None) -> Dict:    
        genAuthHeadersDictRawHTTPPath = self.getPath(pathKey=genAuthHeadersDictRawHTTPPathKey)
        genAuthHeadersDictHTTPMethod = self.getValidHTTPMethodStr(getValidHTTPMethodStrRawMethod=genAuthHeadersDictRawHTTPMethod)
        genAuthHeadersDictContentType = str(genAuthHeadersDictRawContentType)
        genAuthHeadersDictHTTPPath = str(genAuthHeadersDictRawHTTPPath)
        if genAuthHeadersDictRawTimestamp == None: genAuthHeadersDictTimestamp = datetime.utcnow()
        else: genAuthHeadersDictTimestamp = genAuthHeadersDictRawTimestamp
        if genAuthHeadersDictRawParmsDict == None: genAuthHeadersDictParmsDict = genAuthHeadersDictRawParmsDict
        else: genAuthHeadersDictParmsDict = dict(genAuthHeadersDictRawParmsDict)
        genAuthHeadersDictURLPathWParms = f"{self.__folder__}{self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPathKey=genAuthHeadersDictHTTPPath, genURLPathWParmsStrRawParmsDict=genAuthHeadersDictParmsDict)}"
        genAuthHeadersDictHeadersDict = {
            self.__authorizationKey__: None,
            self.__contentTypeKey__: genAuthHeadersDictContentType,
            self.__dateKey__: genAuthHeadersDictTimestamp.strftime("%a, %d %b %Y %H:%M:%S") + ' GMT'
        }
        genAuthHeadersDictZuluTimestamp  = genAuthHeadersDictTimestamp.strftime("%Y-%m-%dT%H:%M:%S")+ '.'+'000Z'
        genAuthHeadersDictUniqueKey = self.getSecretKey() + genAuthHeadersDictZuluTimestamp    
        genAuthHeadersDictSignableContent = str.format('{0}\n{1}\n{2}', genAuthHeadersDictHTTPMethod, genAuthHeadersDictURLPathWParms, genAuthHeadersDictContentType)
        genAuthHeadersDictSignatureHash = hmac.new(genAuthHeadersDictUniqueKey.encode(), genAuthHeadersDictSignableContent.encode(), hashlib.sha512).digest()
        genAuthHeadersDictBase64SignatureHash = base64.b64encode(genAuthHeadersDictSignatureHash).decode()
        genAuthHeadersDictHeadersDict[self.__authorizationKey__] = str.format('{0} {1}:{2}', self.__accessKey__, self.getSharedKey(), genAuthHeadersDictBase64SignatureHash)
        return genAuthHeadersDictHeadersDict

    def genGetDict(self, genGetDictRawContentType: str, genGetDictRawHTTPPathKey: str, genGetDictRawServer: str = None, genGetDictRawParmsDict: dict = None, genGetDictRawHTTPMethod: str = None, genGetDictRawHTTPProtocol: str = None, genGetDictRawHTTPPort: int = None, genGetDictRawTimestamp: datetime = None):
        genGetDictRawHTTPPath = self.getPath(pathKey=genGetDictRawHTTPPathKey)
        genGetDictContentType = str(genGetDictRawContentType)
        genGetDictHTTPPath = str(genGetDictRawHTTPPath)
        if genGetDictRawServer == None:  genGetDictServer = self.getServer()
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
        #genGetDictURLPathWParmsStr = self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genGetDictHTTPPath, genURLPathWParmsStrRawParmsDict=genGetDictParmsDict)
        return {
            self.__urlKey__ : self.genFullURLWParmsStr(genFullURLWParmsStrRawHTTPPathKey = genGetDictHTTPPath, genFullURLWParmsStrRawServer = genGetDictServer, genFullURLWParmsStrRawParmsDict = genGetDictParmsDict, genFullURLWParmsStrRawHTTPProtocol = genGetDictHTTPProtocol, genFullURLWParmsStrRawHTTPPort = genGetDictHTTPPort),
            self.__headersKey__ : self.genAuthHeadersDict(genAuthHeadersDictRawHTTPMethod = genGetDictHTTPMethod, genAuthHeadersDictRawHTTPPathKey = genGetDictHTTPPath, genAuthHeadersDictRawParmsDict = genGetDictParmsDict, genAuthHeadersDictRawContentType = genGetDictContentType, genAuthHeadersDictRawTimestamp = genGetDictTimestamp)
        }

    def genPostDict(self, genPostDictRawContentType: str, genPostDictRawHTTPPathKey: str, genPostDictRawServer: str = None, genPostDictRawParmsDict: dict = None, genPostDictRawHTTPMethod: str = None, genPostDictRawHTTPProtocol: str = None, genPostDictRawHTTPPort: str = None, genPostDictRawTimestamp: datetime = None, genPostDictRawDataDict: dict = None):
        genPostDictRawHTTPPath = self.getPath(pathKey=genPostDictRawHTTPPathKey)
        genPostDictContentType = str(genPostDictRawContentType)
        genPostDictHTTPPath = str(genPostDictRawHTTPPath)
        if genPostDictRawServer == None:  genPostDictServer = self.getServer()
        else: genPostDictServer = str(genPostDictRawServer)
        if genPostDictRawParmsDict == None: genPostDictParmsDict = genPostDictRawParmsDict
        else: genPostDictParmsDict = dict(genPostDictRawParmsDict)
        #genPostDictURLPathWParmsStr = self.genURLPathWParmsStr(genURLPathWParmsStrRawHTTPPath=genPostDictHTTPPath, genURLPathWParmsStrRawParmsDict=genPostDictParmsDict) 
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
            self.__urlKey__ : self.genFullURLWParmsStr(genFullURLWParmsStrRawHTTPPathKey = genPostDictHTTPPath, genFullURLWParmsStrRawServer = genPostDictServer, genFullURLWParmsStrRawParmsDict = genPostDictParmsDict, genFullURLWParmsStrRawHTTPProtocol = genPostDictHTTPProtocol, genFullURLWParmsStrRawHTTPPort = genPostDictHTTPPort),
            self.__dataKey__ : genPostDictDataDict,
            self.__headersKey__ : self.genAuthHeadersDict(genAuthHeadersDictRawHTTPMethod = genPostDictHTTPMethod, genAuthHeadersDictRawHTTPPathKey = genPostDictHTTPPath, genAuthHeadersDictRawParmsDict = genPostDictParmsDict, genAuthHeadersDictRawContentType = genPostDictContentType, genAuthHeadersDictRawTimestamp = genPostDictTimestamp)
        }

class LogixCustomerAPI(LogixSecureAPICalls):
    __defAPIBasePath__ = "Connectors/CustomerInquiry.asmx"
    __defPathDict__ = {
        "pkStatus" : {LogixSecureAPICalls.__pathDictPathKey__ : "CustomerPKStatus",
                        LogixSecureAPICalls.__pathDictMethodsKey__ : ["GET"],
                        LogixSecureAPICalls.__pathDictParmsSpecKey__ : {"0" : [{"required" : ["JobId"], "optional" : None}]},
                        LogixSecureAPICalls.__pathDictDataSpecKey__ : {"0": [{"required" : None, "optional" : None}],
                        LogixSecureAPICalls.__pathDictRespXMLFieldsSpecKey__ : {"0" : {"root":"CustPKStatus", "fields":[{"field":"Files","subFields":["string"]}, "ErrorMsg", "Status", "RecordsReturned", "JobId"]}}}
                    },
        "exportPK" : {LogixSecureAPICalls.__pathDictPathKey__ : "ExportCustomerPK",
                        LogixSecureAPICalls.__pathDictMethodsKey__ : ["POST"],
                        LogixSecureAPICalls.__pathDictParmsSpecKey__ : {"0" : [{"required" : None, "optional" : None}]},
                        LogixSecureAPICalls.__pathDictDataSpecKey__ : {"0": [{"required" : ["GUID", "StartPK", "EncryptionKey", "InitializationVector"], "optional" : None}]},
                        LogixSecureAPICalls.__pathDictRespXMLFieldsSpecKey__ : {"0" : {"root":"CustPKStatus", "fields":["ErrorMsg", "Status", "RecordsReturned", "JobId"]}}
                    }
    }

    empty = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, GUID = None, server: str = None, sharedKey: str = None, secretKey: str = None, empty = None, *args, **kwargs):
        super().__init__(GUID=GUID, apiBasePath=self.__defAPIBasePath__, pathDict=self.__defPathDict__, server=server, sharedKey=sharedKey, secretKey=secretKey, *args, **kwargs)
        self.empty = empty

    def __repr__(self) -> str:
        return f"{type(self).__name__}(apiBasePath={self.getAPIBasePath()}, server={self.getServer()}, sharedKey={self.getSharedKey()}, secretKey={self.getSecretKey()}, GUID={self.getGUID()}, pathDictSize={self.getPathDictSize()})"

    def genCustInqCustPKStatusInfDict(self,
            job_id:str,
            server:str = None,
            httpProtocol:str = None,
            httpPort:str = None,
            timestamp = None):
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.getServer()
        contentType = "application/x-www-form-urlencoded"
        httpMethod = self.__getMethod__

        if httpProtocol == None: httpProtocol = self.__open_http__
        else: httpProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=httpProtocol)

        parameters = {"JobId" : job_id}
        return self.genGetDict(genGetDictRawServer = server, genGetDictRawHTTPPathKey = "pkStatus", genGetDictRawParmsDict=parameters, genGetDictRawContentType = contentType, genGetDictRawHTTPMethod = httpMethod, genGetDictRawHTTPProtocol = httpProtocol, genGetDictRawHTTPPort = httpPort, genGetDictRawTimestamp = timestamp)

    def getCustomerInquiryCustomerPKStatus(self,
            job_id: str,
            server: str = None,
            timestamp = None):
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.getServer()
        info = self.genCustInqCustPKStatusInfDict(server = server, job_id = job_id, timestamp = timestamp)
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

        if GUID == None: GUID = self.getGUID()
        if timestamp == None: timestamp = datetime.utcnow()

        if httpProtocol == None: httpProtocol = self.__open_http__
        else: httpProtocol = self.getValidHTTPProtocolStr(getValidHTTPProtocolStrRawHTTPProtocol=httpProtocol)

        if server == None:  server = self.getServer()
        contentType = "application/x-www-form-urlencoded"
        httpMethod = self.__postMethod__
        parameters = {}
        data = {
                'GUID': GUID,
                'StartPK': StartPK,
                'EncryptionKey': EncryptionKey,
                'InitializationVector': InitializationVector
        }
        return self.genPostDict(genPostDictRawServer = server, genPostDictRawHTTPPathKey = "exportPK", genPostDictRawParmsDict=parameters, genPostDictRawContentType = contentType, genPostDictRawHTTPMethod = httpMethod, genPostDictRawHTTPProtocol = httpProtocol, genPostDictRawHTTPPort = httpPort, genPostDictRawTimestamp = timestamp, genPostDictRawDataDict = data)

    def postCustomerInquiryExportCustomerPK(self,
            StartPK:str,
            EncryptionKey:str,
            InitializationVector:str,
            GUID:str = None,
            server:str = None,
            timestamp = None):
        if GUID == None: GUID = self.getGUID()
        if timestamp == None: timestamp = datetime.utcnow()
        if server == None:  server = self.getServer()
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
    postReq = custAPI.postCustomerInquiryExportCustomerPK(StartPK='52398150', EncryptionKey='1Tu/S37K0ZTuy3kSIiSngXKB36oSaIe4D0fcrrlB7bw=', InitializationVector='eFZsnfQu2o2fDg1p2qdFQQ==')
    print('Post:')
    print(curlify.to_curl(postReq.request))
    print(postReq)
    print(postReq.content)

def testObject():
    custAPI = LogixCustomerAPI(server="10.37.24.156", sharedKey="cc73bfec4d774611b0e254fe7beea49a", secretKey="f2d7fea9a8d84d4b897160b2b90d9e97", GUID="234a86cc-1995-4886-82ea-8808cc9ec919")
    print(custAPI)
    testGet(custAPI)
    testPost(custAPI)


testObject()