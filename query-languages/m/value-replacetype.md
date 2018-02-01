---
title: "Value.ReplaceType | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9f67a2c0-a251-423a-b93f-2a610df30744
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Value.ReplaceType

  
## About  
A value may be ascribed a type using Value.ReplaceType. Value.ReplaceType either returns a new value with the type ascribed or raises an error if the new type is incompatible with the value’s native primitive type. In particular, the function raises an error when an attempt is made to ascribe an abstract type, such as any.  When replacing a the type of a record, the new type must have the same number of fields, and the new fields replace the old fields by ordinal position, not by name.  Similarly, when replacing the type of a table, the new type must have the same number of columns, and the new columns replace the old columns by ordinal position.  
  
```  
Value.Replacetype(value as any, replacedType as type) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to replace.|  
|replacedType|As type.|  
  
