---
title: "Web.Contents | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Web.Contents

  
## About  
Returns the contents downloaded from a web **url** as a binary value.  
  
```  
Web.Contents(url as text, optional options as nullable record) as binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|url|The URL for the Web site.|  
|options|An options record to control the behavior of this function.|  
  
### <a name="__toc360793395"></a>options Field  
  
|Field|Description|  
|---------|---------------|  
|Query|Programmatically add query parameters to the URL.|  
|ApiKeyName|Specify the name of the API key parameter for the target site. The actual key is provided in the credentials dialog.|  
|Content|The content of the POST web request (specifying this values changes the web request from a GET to a POST).|  
|Headers|Specifying this value as a record will supply additional headers to an HTTP request|  
|Timeout|Specifying this value as a duration will change the timeout for an HTTP request. The default value is 100 seconds.|  
|ExcludedFromCacheKey|Specifying this value as a list will exclude these HTTP header keys from being part of the calculation for caching data.|  
|IsRetry|Specifying this logical value as true will ignore any existing response in the cache when fetching data.|  
|ManualStatusHandling|Specifying this value as a list will prevent any builtin handling for HTTP requests whose response has one of these status codes.|  
|RelativePath|Specifying this value as text appends it to the base URL before making the request.|  
  
## Example  
  
```  
Web.Contents("www.microsoft.com") equals  The binary contents from the URL www.microsoft.com when accessed via HTTP  
```  
