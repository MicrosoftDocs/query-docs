---
title: "Record.FieldNames | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldNames

  
## About  
Returns a list of field names in order of the record's fields.  
  
## Syntax

<pre>
Record.FieldNames(record as record) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check.|  
  
## Example  
  
```powerquery-m
Record.FieldNames( [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] )  
```  
  
```powerquery-m 
equals {"OrderID","CustomerID", "Bait", "Price"}  
```  
