---
title: "Record.RemoveFields | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.RemoveFields

  
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
  
