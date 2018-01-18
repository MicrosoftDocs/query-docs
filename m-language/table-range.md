---
title: "Table.Range | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 957ab404-0a6f-4ad3-8f95-c135459a9043
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.Range
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the specified number of rows from a table starting at an offset.  
  
```  
Table.Range( table as table, offset as number, optional count as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|Source table.|  
|Offset|Starting row offset.|  
|optional count|Optional number of rows to return. If count is not provided, all rows are returned starting from offset.|  
  
## Remark  
  
-   Table.Range is similar to List.Range but requires a table as input.  
  
## Example  
  
```  
Table.Range(Table.FromRecords({  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}), 1, 2)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
  
