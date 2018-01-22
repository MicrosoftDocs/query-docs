---
title: "Date.WeekOfMonth | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2a7977d3-3f15-4cac-92cc-de69a986698a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.WeekOfMonth

  
## About  
Returns a number for the count of week in the current month.  
  
```  
Date.WeekOfMonth(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The **DateTime** to check against.|  
  
## Example  
  
```  
Date.WeekOfMonth(DateTime.FromText("2011-08-30")) equals 5  
```  
