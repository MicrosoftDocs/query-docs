---
title: "Date.WeekOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ecb51e09-ce6b-4112-9fe6-f8b66419717e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.WeekOfYear

  
## About  
Returns a number for the count of week in the current year.  
  
```  
Date.WeekOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Date.WeekOfYear(DateTime.FromText("2011-02-21")) equals 8  
```  
