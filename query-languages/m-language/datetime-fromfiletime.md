---
title: "DateTime.FromFileTime | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 54904a2e-01a6-460d-b417-aebb82c62c6d
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.FromFileTime

  
## About  
Returns a DateTime value from the supplied number.  
  
```  
DateTime.FromFileTime(fileTime as nullable number) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fileTime|The fileTime is a Windows file time value that represents the number of 100-nanoseconds intervals that have elapsed since 12:00 midnight, January 1, 1601 A.D. (C.E.) Coordinated Universal Time (UTC).|  
  
## Example  
  
```  
DateTime.FromFileTime(12987640252984224) equals #datetime(2012, 7, 24, 14, 50, 52.9842245)  
```  
