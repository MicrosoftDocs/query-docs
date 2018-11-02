---
title: "Type.RecordFields | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.RecordFields

  
## About  
Returns a record describing the fields of a record type with each field of the returned record type having a corresponding name and a value that is a record of the form [ Type = type, Opional = logical ].  
  
## Syntax

<pre>
Type.RecordFields(#"type" as type) as record  
</pre> 
  
## Example  
  
```powerquery-m
Type.RecordFields(type [ A = number, optional B = any])  
equals [  
A = [Type = number, Optional = false],  
B = [Type = any, Optional = true]  
]  
```  
