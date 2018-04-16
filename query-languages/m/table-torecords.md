---
title: "Table.ToRecords | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToRecords

  
## About  
Returns a list of records from an input table.  
  
```  
Table.ToRecords(table as table) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to convert.|  
  
## Example  
  
```  
Table.ToRecords(Table.FromRows({{"1", "2"}},{"a", "b"})) equals {[a = "1", b = "2"]}  
```  
