---
title: "Date.Month | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 44aff369-76dd-4117-a801-4fe90387d1e7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.Month

  
## About  
Returns the month from a DateTime value.  
  
```  
Date.Month(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the month for.|  
  
## Example  
  
```  
Date.Month(DateTime.FromText("2011-02-19")) equals 2  
```  
