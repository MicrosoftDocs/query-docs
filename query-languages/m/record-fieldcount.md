---
title: "Record.FieldCount | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldCount

  
## About  
Returns the number of fields in a record.  
  
## Syntax

<pre>
Record.FieldCount(record as record) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check against.|  
  
## Example  
  
```powerquery-m
Record.FieldCount([A=1, B=2]) equals 2  
```  
