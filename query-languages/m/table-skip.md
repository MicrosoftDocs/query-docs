---
title: "Table.Skip | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Skip

  
## About  
Returns a table that does not contain the first row or rows of the table.  
  
## Syntax

<pre>
Table.Skip(table as table, optional countOrCondition as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional countOrCondition|The number of rows to skip.|  
  
## <a name="__toc360789542"></a>Remarks  
  
-   **Table.Skip** is similar to **List.Skip** but requires a table as input.  
  
-   If countOrCondition is a number, that many rows (starting at the top) will be skipped.  
  
-   If countOrCondition is a condition, the rows that meet the condition will be skipped until a row does not meet the condition.  
  
## Examples  
  
```powerquery-m
Table.Skip(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
