---
title: "Value.Metadata | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.Metadata

  
## About  
Returns a record containing the input’s metadata.  
  
## Syntax

<pre>
Value.Metadata(value as any) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to retrieve metadata for.|  
  
## Example  
  
```powerquery-m 
Value.Metadata(1 meta [meta = 1]) equals [ meta = 1]  
```  
