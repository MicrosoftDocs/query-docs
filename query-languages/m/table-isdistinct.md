---
title: "Table.IsDistinct | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.IsDistinct

  
## About  
Determines whether a table contains only distinct rows.  
  
```  
Table.IsDistinct(table as table, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## Example  
  
```  
Table.IsDistinct  
  
(  
  
    Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
))  
  
equals true  
```  
