---
title: "Date.DaysInMonth | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3a407482-b933-4596-9bdc-43fe2f1de523
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.DaysInMonth

  
## About  
Returns the number of days in the month from a DateTime value.  
  
```  
Date.DaysInMonth(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Date.DaysInMonth(DateTime.FromText("2012-03-01")) equals 31  
```  
