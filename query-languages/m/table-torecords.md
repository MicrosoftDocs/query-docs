---
title: "Table.ToRecords | Microsoft Docs"
ms.date: 5/17/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToRecords


## Syntax

<pre>
Table.ToRecords(<b>table</b> as table) as list  
</pre>
  

## About  
Converts a table, <code>table</code>, to a list of records.

  
## Example  
  
Convert the table to a list of records.

```powerquery-m
Table.ToRecords(Table.FromRows({{1, "Bob", "123-4567"} , {2, "Jim", "987-6543"}, {3, "Paul", "543-7890"} },{"CustomerID", "Name", "Phone"}))
```

<code>{[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"]}</code> 
