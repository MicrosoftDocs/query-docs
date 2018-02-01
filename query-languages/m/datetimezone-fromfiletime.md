---
title: "DateTimeZone.FromFileTime | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 565684a8-f1a3-442c-83e3-80bc06388d3c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.FromFileTime

  
## About  
Returns a DateTimeZone from a number value.  
  
```  
DateTimeZone.FromFileTime(fileTime as nullable number) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fileTime|The fileTime is a Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).|  
  
## <a name="__goback"></a>Example  
  
```  
DateTimeZone.FromFileTime(12987640252984224) equals #datetimezone(2012, 7, 24, 14, 50, 52.9842245, -7, 0)  
```  
