---
title: "Table.Last | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Last

  
## About  
Returns the last row of a table.  
  
## Syntax

<pre>
Table.Last(table as table, optional default as) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|optional default|Optional default value.|  
  
## <a name="__toc360789492"></a>Remark  
  
-   If the table is empty, Table.Last returns null.  
  
## Example  
  
```powerquery-m
Table.Last(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"]  
  
}))  
```  
  
|Name|Value|  
|--------|---------|  
|CustomerID|3|  
|Name|Paul|  
|Phone|543-7890|  
  
