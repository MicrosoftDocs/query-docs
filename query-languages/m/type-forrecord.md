---
title: "Type.ForRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0bbaa332-a3b4-4cc2-8311-1a11a837957f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Type.ForRecord

  
## About  
Returns a Record type from a fields record.  
  
```  
Type.ForRecord(fields as record, open as logical) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|fields|The record to convert.|  
|open|A logical value indicating if the returned type should be an open record.|  
  
## Example  
  
```  
Type.ForRecord(  
[  
X = [Type = type number, Optional = false],   
Y = [Type = type number, Optional = true]], true)  
equals type [ X = number, optional Y = number,...   
]  
```  
