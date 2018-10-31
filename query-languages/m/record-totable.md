---
title: "Record.ToTable | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.ToTable

  
## About  
Returns a table of records containing field names and values from an input record.  
  
## Syntax

<pre>
Record.ToTable(record as record) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to convert.|  
  
## <a name="__toc360789191"></a>Remarks  
  
-   The type of the return value of this function is {[Name = text, Value = any ]}.  
  
## Example  
  
```powerquery-m
Record.ToTable([OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0] )  
  
equals  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
