---
title: "Time.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cae35309-2a82-4007-9ef3-55627ed82257
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Time.FromText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a Time value from a set of date formats.  
  
```  
Time.FromText(time as nullable text, optional culture as nullable text) as nullable date  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|time|The text value representing the time.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### Time formats  
  
-   hh:mm  
  
-   hh:mm:ss  
  
-   hh:mm:ss.nnnnnnn  
  
### Terms  
  
-   h = hours  
  
-   m = minutes  
  
-   s = seconds  
  
-   n = fractional seconds  
  
## Examples  
  
```  
Time.FromText("12:34:12") equals Time,hh:mm:ss  
```  
  
```  
Time.FromText("12:34:12.1254425") equals hh:mm:ss.nnnnnnn  
```  
