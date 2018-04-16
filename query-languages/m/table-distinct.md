---
title: "Table.Distinct | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Distinct

  
## About  
Removes duplicate rows from a table, ensuring that all remaining rows are distinct.  
  
```  
Table.Distinct(table as table, optional equationCriteria as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table|  
  
## Examples  
  
```  
Table.Distinct(  
  
    Table.FromRecords(  
  
{  
  
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],  
  
    [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],  
  
    [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],  
  
    [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],  
  
    [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],  
  
    [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],  
  
    [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],  
  
    [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],  
  
    [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]  
  
}  
  
), "CustomerID")  
```  
  
|OrderID|CustomerID|Item|Price|  
|-----------|--------------|--------|---------|  
|1|1|Fishing rod|100|  
|3|2|Fishing net|25|  
|4|3|Fish tazer|200|  
|7|5|Bait|3.25|  
|9|6|Bait|3.25|  
  
