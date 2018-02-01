---
title: "Table.MatchesAllRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f7b68105-263e-45e1-8540-9ebb9af5747e
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
