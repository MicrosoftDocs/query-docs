---
title: "Table.FromValue | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromValue

  
## About  
Returns a table with a column containing the provided value or list of values.  
  
## Syntax

<pre>
Table.FromValue (value as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Value|The value to convert.|  
  
## Example  
  
```powerquery-m
Table.FromValue({1, "Bob", "123-4567"}) equals  
```  
  
|Value|  
|---------|  
|1|  
|Bob|  
|132-4567|  
  
