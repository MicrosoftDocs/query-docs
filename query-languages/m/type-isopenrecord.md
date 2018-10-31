---
title: "Type.IsOpenRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.IsOpenRecord

  
## About  
Returns whether a record type is open.  
  
## Syntax

<pre>
Type.IsOpenRecord(#"type" as type) as logical  
</pre>
  
## Examples  
  
```powerquery-m 
Type.IsOpenRecord(type [ A = number,…]) equals true  
```  
  
```powerquery-m
Type.IsOpenRecord(type [ A = number]) equals false  
```  
