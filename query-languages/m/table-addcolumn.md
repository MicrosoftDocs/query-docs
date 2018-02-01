---
title: "Table.AddColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6c64d0a5-9654-4d15-bfb6-9cc380aaf3c0
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.AddColumn

  
## About  
Adds a column named newColumnName to a table.  
  
```  
Table.AddColumn(table as table, newColumnName as text, columnGenerator as function,  optional columnType as nullable type) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|newColumnName|The name of the new column to add.|  
|columnGenerator|New column generator function.|  
|optional columnType|Optional column type for new column|  
  
## <a name="__toc360789599"></a>Remarks  
The values for the column are computed using the specified function from each row.  
  
## Example  
  
```  
Table.AddColumn(Table.FromRecords(  
  
{  
  
      [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0, Shipping = 10.00],  
  
      [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping = 15.00],  
  
      [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping = 10.00]  
  
}  
  
), "TotalPrice", each [Price] + [Shipping])  
  
Table.AddColumn(Table.FromRecords(  
  
{  
  
      [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0, Shipping = 10.00],  
  
      [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping = 15.00],  
  
      [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping = 10.00]  
  
}  
  
), "TotalPrice", each [Price] + [Shipping])  
```  
  
|OrderID|CustomerID|Item|Price|Shipping|TotalPrice|  
|-----------|--------------|--------|---------|------------|--------------|  
|1|1|Fishing rod|100|10|110|  
|2|1|1 lb. worms|5|15|20|  
|3|2|Fishing net|25|10|35|  
  
