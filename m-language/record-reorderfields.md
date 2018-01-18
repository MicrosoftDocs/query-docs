---
title: "Record.ReorderFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8c92dd93-a0c4-4b8c-b214-c40f5f55268c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.ReorderFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
