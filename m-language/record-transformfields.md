---
title: "Record.TransformFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c1bee5ce-4aeb-49b7-9bf7-efb7c63772c2
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.TransformFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Transforms fields by applying **transformOperations**. For more more information about  values supported by **transformOperations**, see Parameter Values.  
  
```  
Record.TransformFields(record as record,  transformOperations as list,  optional missingField as nullable number) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|transformOperations|The list of transformations to make.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
```  
MissingField.Error = 0;  
```  
  
```  
MissingField.Ignore = 1;  
```  
  
```  
MissingField.UseNull = 2;  
```  
  
## Examples  
  
```  
Record.TransformFields([OrderID = 1, CustomerID= 1, Item = "Fishing rod", Price = "100.0"], {"Price", Number.FromText})  
```  
  
```  
equals [OrderID =1, CustomerID  =1, Item = "Fishing rod", Price=100 ]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
```  
Record.TransformFields(  
```  
  
```  
[OrderID ="1", CustomerID= 1, Item = "Fishing rod", Price = "100.0"],  
```  
  
```  
{{"OrderID", Number.FromText}, {"Price",Number.FromText}})  
```  
  
```  
equals [OrderID =1, CustomerID  =1, Item = "Fishing rod", Price=100 ]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
