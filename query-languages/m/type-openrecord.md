---
title: "Type.OpenRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8fe6ee0d-cb1f-4f6e-abc2-125f5e2f579f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
