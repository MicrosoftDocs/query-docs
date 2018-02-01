---
title: "Type.TableRow | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b710243d-993b-47a5-8e81-7bc49ff51133
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.TableRow

  
## About  
Returns a row type from a table type.  
  
```  
Type.TableRow(table as type) as type  
```  
  
## Example  
  
```  
Type.TableRow(   
Value.Type(     
Value.ReplaceType(   
Table.FromRecords({[A=1]}),   
type table [ A = number] ))   
)   
equals type [    A = number  ]  
```  
