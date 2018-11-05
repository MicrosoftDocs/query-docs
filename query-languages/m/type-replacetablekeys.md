---
title: "Type.ReplaceTableKeys | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.ReplaceTableKeys

  
## About  
Replaces the keys in a table type.  
  
## Syntax

<pre>  
Type.ReplaceTableKeys(tableType as type,  keys as list) as type  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|tableType|The table type to modify.|  
|keys|The list of keys to replace.|  
  
## Example  
  
```powerquery-m
Type.ReplaceTableKeys(tableType, {}) equals  returns type value with all keys removed  
```  
