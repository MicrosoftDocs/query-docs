---
title: "Date.IsLeapYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 00f167b6-38bf-4c9e-a74b-562ff311b437
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsLeapYear

  
## About  
Returns a logical value indicating whether the year portion of a DateTime value is a leap year.  
  
```  
Date.IsLeapYear(dateTime as nullable datetime) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check.|  
  
## Examples  
`Date.IsLeapYear(DateTime.FromText("2011-01-01")) equals false`  
  
```  
Date.IsLeapYear(DateTime.FromText("2012-01-01")) equals true  
```  
