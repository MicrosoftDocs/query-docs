---
title: "Date.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.FromText

  
## About  
Returns a Date value from a set of date formats and culture value, following ISO 8601 format standard.  

## Syntax

<pre>
Date.FromText(date as nullable text, optional culture as nullable text) as nullable date  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|A string value to transorm.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### Supported formats  
  
-   yyyy-MM-dd  
  
-   YYYYMMDD  
  
-   M/d/yyyy  
  
### Terms  
  
-   Y = years  
  
-   M = months  
  
-   D = days  
  
## <a name="__toc360788938"></a>Remarks  
  
-   If the culture is not specified, the current user culture is used.  
  
## Example  
  
```powerquery-m 
Date.FromText("2010-02-19") equals Date,yyyy-MM-dd  
```  
