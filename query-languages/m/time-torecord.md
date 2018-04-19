---
title: "Time.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
```  
Time.ToRecord(time as time) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|time|The time to parse.|  
  
## Example  
  
```  
Time.ToRecord(#time(12, 1, 2)) equals [Hour=12, Minute=1, Second=2]  
```  
