---
title: "Web.Contents | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 55efc096-bddb-44d9-9f6d-f35f5095c1ad
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Web.Contents
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
