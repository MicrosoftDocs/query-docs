---
title: "Type.TableRow | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.TableRow

  
## About  
Returns a row type from a table type.  
  
## Syntax

<pre>
Type.TableRow(table as type) as type  
</pre>
  
## Example  
  
```powerquery-m 
Type.TableRow(   
Value.Type(     
Value.ReplaceType(   
Table.FromRecords({[A=1]}),   
type table [ A = number] ))   
)   
equals type [    A = number  ]  
```  
