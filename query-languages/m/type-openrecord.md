---
title: "Type.OpenRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.OpenRecord

  
## About  
Returns an opened version of a record type, or the same type, if it is already open.  
  
```  
Type.OpenRecord(#"type" as type) as type  
```  
  
## Example  
  
```  
Type.OpenRecord( type [ A = number] ) equals type [ A = number, …]  
```  
