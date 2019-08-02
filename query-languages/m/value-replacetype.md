---
title: "Value.ReplaceType | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.ReplaceType

## Syntax

<pre>
Value.ReplaceType(<b>value</b> as any, <b>type</b> as type) as any
</pre>
  
## About  
A value may be ascribed a type using Value.ReplaceType. Value.ReplaceType either returns a new value with the type ascribed or raises an error if the new type is incompatible with the value’s native primitive type. In particular, the function raises an error when an attempt is made to ascribe an abstract type, such as any.  When replacing a the type of a record, the new type must have the same number of fields, and the new fields replace the old fields by ordinal position, not by name.  Similarly, when replacing the type of a table, the new type must have the same number of columns, and the new columns replace the old columns by ordinal position.  
  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to replace.|  
|replacedType|As type.|  
  
