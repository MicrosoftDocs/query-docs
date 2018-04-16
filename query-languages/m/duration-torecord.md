---
title: "Duration.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.ToRecord

  
## About  
Returns a record with parts of a Duration value.  
  
```  
Duration.ToRecords(duration as duration) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## Example  
  
```  
Duration.ToRecord(#duration(2, 5, 55, 20)) equals [Days=2, Hours=5, Minutes=55, Seconds=20]  
```  
