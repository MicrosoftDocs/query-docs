---
title: "Time.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.FromText

  
## About  
Returns a Time value from a set of date formats.  
  
```  
Time.FromText(time as nullable text, optional culture as nullable text) as nullable date  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|time|The text value representing the time.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
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
