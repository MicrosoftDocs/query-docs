---
title: "Type.TableRow | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.TableRow

## Syntax

<pre>
Type.TableRow(<b>table</b> as type) as type 
</pre>
  
## About  
Returns a row type from a table type.  

  
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
