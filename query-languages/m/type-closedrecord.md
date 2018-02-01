---
title: "Type.ClosedRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f1b7376e-a5e1-41a4-ae91-d6058ad609e9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.ClosedRecord

  
## About  
The given type must be a record type returns a closed version of the given record type (or the same type, if it is already closed)  
  
```  
Type.ClosedRecord(#"type" as type) as type  
```  
  
## Example  
  
```  
Type.ClosedRecord( type [ A = number,…] ) equals type [A=number]  
```  
