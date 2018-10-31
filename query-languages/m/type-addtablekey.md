---
title: "Type.AddTableKey | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.AddTableKey

  
## About  
Add a key to a table type.  
  
## Syntax

<pre>
Type.AddTableKey (table as type, columns as list,  isPrimary as logical) as type  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The table type to modify.|  
|columns|Columns that define the key.|  
|isPrimary|Logical stating whether or not it is the primary key.|  
  
## Example  
  
```powerquery-m
Type.AddTableKey(tableType, {"A", "B"}, false) equals  add a non-primary key that combines values from columns A and B  
```  
