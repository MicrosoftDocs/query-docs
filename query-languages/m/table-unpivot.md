---
title: "Table.Unpivot | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Unpivot

  
## About  
Given a list of table columns, transforms those columns into attribute-value pairs.  
  
```  
Table.Unpivot(table as table, pivotColumns as list, attributeColumn as text, valueColumn as text) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|pivotColumns|The columns to transform.|  
|attributeColumn|The column to make the attribute.|  
|valueColumn|The column to make the value.|  
  
## <a name="__toc360789588"></a>Remarks  
  
-   The transformation is patterned after the SQL UNPIVOT operator.  
  
## Examples  
  
```  
Table.Unpivot(Table.FromRecords({  
  
    [ key = "key1", attribute1 = 1, attribute2 = null, attribute3 = 3 ]}),  
  
    { "attribute1", "attribute2", "attribute3" }, "attribute", "value")  
```  
  
|key|attribute|value|  
|-------|-------------|---------|  
|key1|attribute1|1|  
|key1|attribute3|3|  
  
