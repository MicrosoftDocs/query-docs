---
title: "Table.ColumnsOfType | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# Table.ColumnsOfType
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
