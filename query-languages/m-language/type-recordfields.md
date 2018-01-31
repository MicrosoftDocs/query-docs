---
title: "Type.RecordFields | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: afaaee3e-a41c-4225-89b4-4ae7e06609f1
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.RecordFields

  
## About  
Returns a record describing the fields of a record type with each field of the returned record type having a corresponding name and a value that is a record of the form [ Type = type, Opional = logical ].  
  
```  
Type.RecordFields(#"type" as type) as record  
```  
  
## Example  
  
```  
Type.RecordFields(type [ A = number, optional B = any])  
equals [  
A = [Type = number, Optional = false],  
B = [Type = any, Optional = true]  
]  
```  
