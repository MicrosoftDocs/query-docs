---
title: "Table.Column | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Column

  
## About  
Returns the values from a column in a table.  
  
## Syntax

<pre>
Table.Column(table as table, column as text) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|column|The column to check.|  
  
## <a name="__toc360789550"></a>Remarks  
  
-   **Table.Column** is similar to **Record.Field** but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Table.Column(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Name")  
  
equals {"Bob", "Jim", "Paul", "Ringo"}  
```  
