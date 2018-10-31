---
title: "Type.ListItem | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.ListItem

  
## About  
Returns an item type from a list type.  
  
## Syntax

<pre>
Type.ListItem(#"type" as type) as type  
</pre>
  
## Example  
  
```powerquery-m
Type.ListItem (type { number }) equals type number  
```  
