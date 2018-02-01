---
title: "Table.Pivot | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ad64c7b5-1b3a-4776-83e3-2de553c4b493
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.Pivot

  
## About  
Given a table and attribute column containing pivotValues, creates new columns for each of the pivot values and assigns them values from the valueColumn. An optional aggregationFunction can be provided to handle multiple occurrence of the same key value in the attribute column.  
  
```  
Table.Pivot(table as table,  pivotValues as list,  attributeColumn as text,  valueColumn as text,  optional aggregationFunction as nullable function) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|pivotValues|The values to transform.|  
|attributeColumn|The column to make the attribute.|  
|valueColumn|The column to make the value.|  
|optional aggregationFunction|Function to aggregate values.|  
  
## Examples  
  
```  
// Simple input with no key + attribute conflicts.  In other words, (key,attribute) is unique.  
  
Table.Pivot(  
  
    Table.FromRecords({  
  
    [ key = "key1", attribute = "attribute1", value = 1 ],  
  
    [ key = "key1", attribute = "attribute3", value = 3 ],  
  
    [ key = "key2", attribute = "attribute1", value = 2 ],  
  
    [ key = "key2", attribute = "attribute2", value = 4 ]  
  
}), { "attribute1", "attribute2", "attribute3" }, "attribute", "value")  
```  
  
|key|attribute1|attribute2|attribute3|  
|-------|--------------|--------------|--------------|  
|key1|1|null|3|  
|key2|2|4|null|  
  
```  
// Same input as Example 2, but with an additional function specified to resolve the conflict – in this case, to take the minimum value.  Note that this resolution method is the same as the PIVOT clause in SQL Server and most other DBMS’s.  
  
Table.Pivot(  
  
    Table.FromRecords({  
  
    [ key = "key1", attribute = "attribute1" , value = 1 ],  
  
    [ key = "key1", attribute = "attribute3" , value = 3 ],  
  
    [ key = "key2" , attribute = "attribute1" , value = 2 ],  
  
    [ key = "key2", attribute = "attribute1", value = 8 ],  
  
    [ key = "key2", attribute = "attribute2", value = 4 ]  
  
}), { "attribute1", "attribute2", "attribute3" }, "attribute", "value", List.Min)  
```  
  
|key|attribute1|attribute2|attribute3|  
|-------|--------------|--------------|--------------|  
|key1|1|null|null|  
|key2|2|4|null|  
  
