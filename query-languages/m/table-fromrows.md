---
title: "Table.FromRows | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromRows
## About  
Creates a table from the list `rows` where each element of the list is an inner list that contains the column values for a single row. An optional list of column names, a table type, or a number of columns could be provided for `columns`.
  
  
## Syntax

<pre>
Table.FromRows(rows as list, optional columns as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|rows|The List to convert.|  
|optional columns|An optional list of column names, or a table type.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Table.FromRows({{1, "Bob", "123-4567"} , {2, "Jim", "987-6543"}}, {"CustomerID ", "Name", "Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
  
