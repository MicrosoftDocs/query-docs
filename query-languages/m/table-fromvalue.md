---
title: "Table.FromValue | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromValue

  
## About  
Returns a table with a column containing the provided value or list of values.  
  
```  
Table.FromValue (value as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Value|The value to convert.|  
  
## Example  
  
```  
Table.FromValue({1, "Bob", "123-4567"}) equals  
```  
  
|Value|  
|---------|  
|1|  
|Bob|  
|132-4567|  
  
