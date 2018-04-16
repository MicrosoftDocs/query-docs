---
title: "Table.UnpivotOtherColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
  
