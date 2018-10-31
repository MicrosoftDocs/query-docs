---
title: "Value.ReplaceMetadata | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.ReplaceMetadata

  
## About  
Replaces the metadata on a value with the new metadata record provided and returns the original value with the new metadata attached.  
  
## Syntax

<pre>
Value.ReplaceMetadata(value as any, newMeta as record) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to modify.|  
|newMeta|The new metadata to replace the old metadata with..|  
  
## Example  
  
```powerquery-m
Value.ReplaceMetadata(1 meta [meta = 1], [meta=2]) equals  1 meta [meta = 2]  
```  
