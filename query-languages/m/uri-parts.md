---
title: "Uri.Parts | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Uri.Parts

  
## About  
Returns a record value with the fields set to the parts of a Uri text value.  
  
```  
Uri.Parts(absoluteUri as text) as [Scheme = text, Host = text, Port = number, Path = text, Query = record, Fragment = text, UserName = text, Password = text]  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|absoluteUri|The absolute Uri.|  
  
## Example 1  
  
```  
Uri.Parts("http://www.microsoft.com")   
equals [  
Scheme = "http",  
Host = "www.microsoft.com",  
Port = 80,  
Path = "/",  
Query = [],  
Fragment = "",  
UserName = "",  
Password = ""  
]  
```  
  
## Example 2  
Decode a percent-encoded string.  
  
```  
let UriUnescapeDataString = (data as text) as text => Uri.Parts("http://contoso?a=" & data)[Query][a] in UriUnescapeDataString("%2Bmoney%24")  
  
equals "+money$"  
```  
  
