---
title: "Table.UnpivotOtherColumns | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Table.UnpivotOtherColumns

  
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
  
