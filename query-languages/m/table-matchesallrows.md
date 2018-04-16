---
title: "Table.MatchesAllRows | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.MatchesAllRows

  
## About  
Returns true if all of the rows in a table meet a condition.  
  
```  
Table.MatchesAllRows(table as table, condition as function) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|condition|The condition to match.|  
  
## Remark  
  
-   Table.MatchesAllRows is similar to List.MatchesAll but requires a table argument.  
  
## Example  
  
```  
Table.MatchesAllRows(Table.FromRecords (  
  
{  
  
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],  
  
      [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],  
  
      [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],  
  
      [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],  
  
      [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],  
  
      [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0]  
  
}), each Number.Mod([CustomerID], 3) = 0)  
  
equals false  
```  
