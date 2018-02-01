---
title: "DateTimeZone.RemoveZone | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: aa2f84ae-dcb8-485c-981f-76d8377289fe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.RemoveZone

  
## About  
Returns a datetime value with the zone information removed from the input datetimezone value.  
  
```  
DateTimeZone.RemoveZone(dateTimeZone as datetimezone) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to modify.|  
  
## Example  
  
```  
DateTimeZone.RemoveZone(#datetimezone(2010, 5, 4, 14, 5, 5, 8, 0)) equals #datetime(2010, 5, 4, 14, 5, 5)  
```  
