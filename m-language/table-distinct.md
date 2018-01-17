---
title: "Table.Distinct | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2d9184b6-44c2-4db9-aadc-22fb57a9217c
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Distinct
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
