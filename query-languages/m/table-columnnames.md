---
title: "Table.ColumnNames | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ColumnNames

  
## About  
Returns the names of columns from a table.  
  
## Syntax

<pre>
Table.ColumnNames(table as table) as {Text}  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
  
## <a name="__toc360789554"></a>Remarks  
  
-   **Table.ColumnNames** is similar to **Record.FieldNames** but requires a table as input.  
  
## Example  
  
```powerquery-m
Table.ColumnNames(Table.FromRecords(  
  
{  
  
  [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
  [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
  [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
  [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
))  
  
equals { "CustomerID", "Name", "Phone"}  
```  
