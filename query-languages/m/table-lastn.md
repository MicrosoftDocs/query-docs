---
title: "Table.LastN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.LastN

  
## About  
Returns the last row(s) from a table, depending on the **countOrCondition** parameter.  
  
## Syntax

<pre>
Table.LastN(table as table, countOrCondition as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|countOrCondition|Depending on the type, more than one row will be returned.|  
  
## <a name="__toc360789488"></a>Remarks  
  
-   If countOrCondition is a number, that many rows will be returned starting from the end of the table.  
  
-   If countOrCondition is a condition, the rows that meet the condition will be returned in ascending position until a row does not meet the condition.  
  
## Example  
  
```powerquery-m
Table.LastN(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]  
  
}), 1)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|3|Paul|543-7890|  
  
