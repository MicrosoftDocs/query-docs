---
title: "DateTimeZone.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4b08597a-1128-45a4-9e9e-89c409499a9d
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.FromText

  
## About  
Returns a DateTimeZone value from a set of date formats and culture value.  
  
```  
DateTimeZone.FromText(dateTimeZone as nullable text, optional culture as nullable text) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone||  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
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
  
```  
DateTime.FromText("2010-12-31T01:30:00") equals YYYY-MM-DDThh:mm:ss  
```  
  
```  
DateTime.FromText("2010-12-31T01:30:00Z") equals 2010-12-31T01:30:00+00:00  
```  
