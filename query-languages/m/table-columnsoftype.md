---
title: "Table.ColumnsOfType | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ColumnsOfType

  
## About  
Returns a list with the names of the columns that match the specified types.  
  
```  
Table.ColumnsOfType(table as table, listOfTypes as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Table|The input table.|  
|listOfTypes|The types to match columns types on.|  
  
## Example  
  
```  
let  
  
  tableValue = Table.FromRecords({[a=1, b="hello"]}, type table[a=Number.Type, b=Text.Type])  
  
in  
  
  Table.ColumnsOfType(tableValue, {type number})  
  
equals {"a"}  
```  
