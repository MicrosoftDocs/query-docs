---
title: "Time.Hour | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 750e5dc9-58d4-4c4f-98b1-1195dc032d29
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Time.Hour

  
## About  
Returns an hour value from a DateTime value.  
  
```  
Time.Hour(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Time.Hour(DateTime.FromText("12:56:20")) equals 12  
```  
