---
title: "Table.AddIndexColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.AddIndexColumn

  
## About  
Returns a table with a new column with a specific name that, for each row, contains an index of the row in the table.  
  
## Syntax

<pre>
Table.AddIndexColumn(table as table, newColumnName as text, optional initialValue as nullable number, optional increment as nullable number) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|newColumnName|The name of the new column.|  
|optional initialValue|The initial column index. The default initial index is 0.|  
|optional increment|The column index increment. The default increment is 1.|  
  
## Examples  
  
```powerquery-m
Table.AddIndexColumn(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Index")  
```  
  
|CustomerID|Name|Phone|Index|  
|--------------|--------|---------|---------|  
|1|Bob|123-4567|0|  
|2|Jim|987-6543|1|  
|3|Paul|543-7890|2|  
|4|Ringo|232-1550|3|  
  
```powerquery-m
Table.AddIndexColumn(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Index", 1, 2)  
```  
  
|CustomerID|Name|Phone|Index|  
|--------------|--------|---------|---------|  
|1|Bob|123-4567|1|  
|2|Jim|987-6543|3|  
|3|Paul|543-7890|5|  
|4|Ringo|232-1550|7|  
  
