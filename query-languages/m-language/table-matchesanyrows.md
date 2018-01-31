---
title: "Table.MatchesAnyRows | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 914c4107-32d3-4fbd-b99a-236ef69a8a36
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.MatchesAnyRows

  
## About  
Returns true if any of the rows in a table meet a condition.  
  
```  
Table.MatchesAnyRows( table as table, condition as function) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|condition|The condition to match.|  
  
## Remark  
  
-   Table.MatchesAnyRows is similar to List.MatchesAny but requires a table argument.  
  
## Example  
  
```  
Table.MatchesAnyRows(Table.FromRecords (  
  
{  
  
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],  
  
      [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],  
  
      [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],  
  
      [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],  
  
      [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],  
  
      [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0]  
  
}), each Number.Mod([CustomerID], 3) = 0)  
  
equals true  
```  
