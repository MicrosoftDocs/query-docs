---
title: "Record.RemoveFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 07f3a2e2-7deb-4979-82da-d4a03017ed31
caps.latest.revision: 11
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.RemoveFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record that removes all the fields specified in a list. If the field specified does not exist, an exception is thrown.  
  
```  
Record.RemoveFields(record as record, fields as any, optional missingField as nullable number) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|fields|A list of two items with the names of the fields that need to exchange their order in the record.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
```  
MissingField.Error = 0;  
  
MissingField.Ignore = 1;  
  
MissingField.UseNull = 2;  
```  
  
## Examples  
  
```  
Record.RemoveFields([CustomerID=1, Item = "Fishing rod", Price=18.00] , "Price")  
  
equals [CustomerID=1, Item="Fishing rod"]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Item|Fishing rod|  
  
