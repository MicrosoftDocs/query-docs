---
title: "Table.UnpivotOtherColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9f4b3acf-0304-4b20-90ae-f9588b2bea7c
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.UnpivotOtherColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Translates all columns other than a specified set into attribute-value pairs, combined with the rest of the values in each row.  
  
```  
Table.UnpivotOtherColumns(table as table, pivotColumns as list, attributeColumn as text,  valueColumn as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|pivotColumns|The columns to skip transformation.|  
|attributeColumn|The column to make the attribute.|  
|valueColumn|The column to make the value.|  
  
## Remarks  
  
-   The transformation is patterned after the SQL UNPIVOT operator.  
  
## Example  
  
```  
Table.UnpivotOtherColumns(Table.FromRecords({   [ key = "key1", attribute1 = 1, attribute2 = 2, attribute3 = 3 ],   [ key = "key2", attribute1 = 4, attribute2 = 5, attribute3 = 6 ]  }), { "key" }, "column1", "column2")  
```  
  
|key|column1|column2|  
|-------|-----------|-----------|  
|key1|attribute1|1|  
|key1|attribute2|2|  
|key1|attribute3|3|  
|key2|attribute1|4|  
|key2|attribute2|5|  
|key2|attribute3|6|  
  
