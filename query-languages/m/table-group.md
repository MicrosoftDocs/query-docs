---
title: "Table.Group | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Group

  
## About  
Groups table rows by the values of key columns for each row.  
  
```  
Table.Group(table as table, key as any, aggregatedColumns as list, optional groupKind as nullable number, optional comparer as nullable function) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|key|The key columns.|  
|aggregatedColumns|Specifies the names and function return types.|  
|optional groupKind|The type of group. Possible values are GroupKind.Global (default) and GroupKind.Local.|  
|optional comparer|An optional argument that determines equality between group keys.|  
  
## <a name="__toc360789626"></a>Remarks  
  
-   The type of the resulting table is computed by preserving the columns that make up the group key, including their types, and appending new columns with names and types according to the names and function return types specified in the aggregatedColumns argument.  
  
-   For each group, a record is constructed containing the key columns, including their values, along with any aggregated columns from the aggregatedColumns argument.  A table of these group results is returned.  
  
-   A group can be local (GroupKind.Local) or global (GroupKind.Global).  A local group is formed from a consecutive sequence of rows from an input table with the same key value. A global group is formed from all rows in an input table with the same key value.  Multiple local groups may be produced with the same key value but only a single global group is produced for a given key value.  
  
-   The default groupKind value is GroupKind.Global.  
  
-   The Table.Group function may also be used to nest the rows in a group.  
  
## Examples  
  
```  
let  
  
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
  
    Table.Group(Orders, "CustomerID", {"Total", each List.Sum([Price])})  
```  
  
|CustomerID|Total|  
|--------------|---------|  
|1|125|  
|2|25|  
|3|202|  
|5|103.25|  
|6|3.25|  
  
