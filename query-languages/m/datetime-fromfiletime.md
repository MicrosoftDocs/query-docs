---
title: "DateTime.FromFileTime | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.FromFileTime

  
## About  
Returns a DateTime value from the supplied number.  
  
## Syntax

<pre>
DateTime.FromFileTime(fileTime as nullable number) as nullable datetime  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fileTime|The fileTime is a Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).|  
  
## Example  
  
```powerquery-m
DateTime.FromFileTime(12987640252984224) equals #datetime(2012, 7, 24, 14, 50, 52.9842245)  
```  
