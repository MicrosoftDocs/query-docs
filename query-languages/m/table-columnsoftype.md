---
title: "Table.ColumnsOfType | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 79336bbf-f807-45c6-89ac-72336f2edf9e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
