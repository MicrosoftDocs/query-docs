---
title: "Value.As | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 976d2e2e-ceaf-4920-9a59-f52834198c1c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Value.As

  
## About  
Value.As is the function corresponding to the as operator in the formula language. The expression  value as type  asserts that the value of a value argument is compatible with type as per the is operator. If it is not compatible, an error is raised.  
  
```  
Value.As(value as any, type as type) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value as.|  
|type|Asserts that the value of a value argument is compatible with type.|  
  
