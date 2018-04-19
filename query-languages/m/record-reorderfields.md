---
title: "Record.ReorderFields | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.ReorderFields

  
## About  
Returns a new record that reorders fields relative to each other.  Any fields not specified remain in their original locations. Requires two or more fields.  
  
```  
Record.ReorderFields(record as record,  fieldOrder as list,  optional missingField as nullable number) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|fieldOrder|The list of field orders to change to.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
-   `MissingField.Error = 0;`  
  
-   `MissingField.Ignore = 1;`  
  
-   `MissingField.UseNull = 2;`  
  
## Examples  
  
```  
Record.ReorderFields( [CustomerID= 1, OrderID = 1, Item = "Fishing rod", Price = 100.0], { "OrderID", "CustomerID" })  
```  
  
```  
equals [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
