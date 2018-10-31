---
title: "DateTimeZone.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.FromText

  
## About  
Returns a DateTimeZone value from a set of date formats and culture value.  
  
## Syntax

<pre>
DateTimeZone.FromText(dateTimeZone as nullable text, optional culture as nullable text) as nullable datetimezone  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone||  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### DateTimeZone formats  
  
-   YYYY-MM-DDThh:mmhh:mm  
  
-   YYYYMMDDThh:mmhh:mm  
  
-   YYYY-MM-DDThh:mm:sshh:mm  
  
-   YYYYMMDDThh:mm:sshh:mm  
  
-   YYYY-MM-DDThh:mm:ss.nnnnnnnhh:mm  
  
-   YYYYMMDDThh:mm:ss.nnnnnnnhh:mm  
  
-   YYYY-MM-DDThh:mm-hh:mm  
  
-   YYYYMMDDThh:mm-hh:mm  
  
-   YYYY-MM-DDThh:mm:ss-hh:mm  
  
-   YYYYMMDDThh:mm:ss-hh:mm  
  
-   YYYY-MM-DDThh:mm:ss.nnnnnnn-hh:mm  
  
-   YYYYMMDDThh:mm:ss.nnnnnnn-hh:mm  
  
-   YYYY-MM-DDThh:mmZ  
  
-   YYYYMMDDThh:mmZ  
  
-   YYYY-MM-DDThh:mm:ssZ  
  
-   YYYYMMDDThh:mm:ssZ  
  
-   YYYY-MM-DDThh:mm:ss.nnnnnnnZ  
  
-   YYYYMMDDThh:mm:ss.nnnnnnnZ  
  
### Terms  
  
-   Y = years  
  
-   M = months  
  
-   D = days  
  
-   h = hours  
  
-   m = minutes  
  
-   s = seconds  
  
-   n = fractional seconds  
  
-   TZD = time zone designator  
  
## Examples  
  
```powerquery-m
DateTime.FromText("2010-12-31T01:30:00") equals YYYY-MM-DDThh:mm:ss  
```  
  
```powerquery-m
DateTime.FromText("2010-12-31T01:30:00Z") equals 2010-12-31T01:30:00+00:00  
```  
