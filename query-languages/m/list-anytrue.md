---
title: "List.AnyTrue | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1b2fa526-b967-41fa-a04b-20011494af1a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.AnyTrue

  
## About  
Returns true if any expression in a list in true  
  
`List.AnyTrue(list as list) as logical`  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```  
List.AnyTrue({2=0, false, 1 < 0 }) equals false  
```  
