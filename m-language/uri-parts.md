---
title: "Uri.Parts | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 88f24848-da8a-4bd2-bd8c-ac6a1e9932db
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Uri.Parts
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
