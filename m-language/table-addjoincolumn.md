---
title: "Table.AddJoinColumn | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7a1aaa4f-5f29-4da8-b629-6cb4b1cf1137
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.AddJoinColumn
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Performs a nested join between table1 and table2 from specific columns and produces the join result as a newColumnName column for each row of table1.  
  
```  
Table.AddJoinColumn(table1 as table, key1 as any, table2 as function, key2 as any, newColumnName as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table1|The Table to modify.|  
|key1|The table1 column to join.|  
|table2|The Table to check against.|  
|key2|The table2 column to join.|  
|newColumnName|The name of the new column.|  
  
## <a name="__toc360789606"></a>Remarks  
  
-   Table.AddJoinColumn is similar to Table.Join except that the join results are presented in a nested rather than flattened table.  
  
-   Table.AddJoinColumn performs a left outer join by default, other join types are supported in Table.Join or Table.NestedJoin  
  
-   The type of the resulting table is computed by taking the type of table1 and appending a column newColumnName with a type that is the type of table2.  
  
-   For more information about joining tables, see [Table.Join](../PowerQuery/table-join.md).  
  
## Example  
  
```  
let  
  
    Query = let  
  
    Customers = Table.FromRecords({  
  
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],  
  
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
    }),  
  
    Orders = Table.FromRecords({  
  
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],  
  
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],  
  
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],  
  
        [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],  
  
        [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],  
  
        [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],  
  
        [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],  
  
        [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],  
  
        [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]  
  
    })  
  
in  
  
Table.AddJoinColumn(  
  
    Customers, {"CustomerID"},  
  
    Orders, {"CustomerID"},  
  
    "Orders"  
  
),  
  
    #"Expand Orders" = Table.ExpandTableColumn(Query, "Orders", {"OrderID", "CustomerID", "Item", "Price"}, {"Orders.OrderID", "Orders.CustomerID", "Orders.Item", "Orders.Price"})  
  
in  
  
    #"Expand Orders"  
```  
  
|CustomerID|Name|Phone|Orders.OrderID|Orders.CustomerID|Orders.Item|Orders.Price|  
|--------------|--------|---------|------------------|---------------------|---------------|----------------|  
|1|Bob|123-4567|1|1|Fishing rod|100|  
|1|Bob|123-4567|2|1|1 lb. worms|5|  
|2|Jim|987-6543|3|2|Fishing net|25|  
|3|Paul|543-7890|4|3|Fish tazer|200|  
|3|Paul|543-7890|5|3|Bandaids|2|  
|1|Bob|123-4567|6|1|Tackle box|20|  
|4|Ringo|232-1550|||||  
  
