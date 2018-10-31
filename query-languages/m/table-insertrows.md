---
title: "Table.InsertRows | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.InsertRows

  
## About  
Returns a table with the list of rows inserted into the table at an index. Each row to insert must match the row type of the table..  
  
## Syntax

<pre> 
Table.InsertRows(table as table, offset as number, rows as list) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to insert rows into.|  
|offset|The row number to insert at.|  
|rows|The List of rows to insert.|  
  
## Remark  
  
-   Table.InsertRows is similar to List.InsertRange but requires a table as input.  
  
## Example  
  
```powerquery-m
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
  
Table.InsertRows(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] }),  
  
    2,  
  
    { [CustomerID = 3, Name = "Paul", Phone = "543-7890"] })  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
