---
title: "Record.RenameFields | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.RenameFields

  
## About  
Returns a new record that renames the fields specified. The resultant fields will retain their original order. This function supports swapping and chaining field names. However, all target names plus remaining field names must constitute a unique set or an error will occur.  
  
## Syntax

<pre>
Record.RenameFields(record as record,  renames as list,  optional missingField as nullable number) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to modify.|  
|renames|The list of renames to apply.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
-   `MissingField.Error = 0;`  
  
-   `MissingField.Ignore = 1;`  
  
-   `MissingField.UseNull = 2;`  
  
## <a name="__toc360789170"></a>Remarks  
  
-   Record.RenameFields swaps and chains field names.  If all target names plus remaining field names are not a unique set, an Expression.Error is thrown  
  
## Examples  
  
```powerquery-m
Record.RenameFields([OrderID = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0], {"UnitPrice","Price"})  
```  
  
```powerquery-m
equals [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
