---
title: "DateTime.Date | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 903181a7-eee6-4ea5-8a9a-87445cc494fe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.Date

  
## About  
Returns a date part from a DateTime value  
  
```  
DateTime.Date(dateTime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to parse.|  
  
## Example  
  
```  
DateTime.Date(#datetime(2010, 5, 4, 6, 5, 4)) equals #date(2010, 5, 4)  
```  
