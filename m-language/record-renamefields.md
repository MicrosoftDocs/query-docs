---
title: "Record.RenameFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c0c6e45d-37f2-4be9-b6db-28fd18b04450
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.RenameFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a new record that renames the fields specified. The resultant fields will retain their original order. This function supports swapping and chaining field names. However, all target names plus remaining field names must constitute a unique set or an error will occur.  
  
```  
Record.RenameFields(record as record,  renames as list,  optional missingField as nullable number) as record  
```  
  
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
  
```  
Record.RenameFields([OrderID = 1, CustomerID = 1, Item = "Fishing rod", UnitPrice = 100.0], {"UnitPrice","Price"})  
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
  
