---
title: "Record.FieldCount | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldCount

  
## About  
Returns the number of fields in a record.  
  
```  
Record.FieldCount(record as record) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check against.|  
  
## Example  
  
```  
Record.FieldCount([A=1, B=2]) equals 2  
```  
