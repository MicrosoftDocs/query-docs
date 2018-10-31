---
title: "Table.Contains | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Contains

  
## About  
Determines whether the a record appears as a row in the table.  
  
## Syntax

<pre>
Table.Contains(table as table, row as record, optional equationCriteria as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|row|The row to check for.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789665"></a>Remarks  
  
-   Table.Contains is similar to List.Contains but requires a table as input.  
  
## Example  
  
```powerquery-m
Table.Contains(  
  
    Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),  
  
    [Name="Bob"])  
  
equals true  
```  
