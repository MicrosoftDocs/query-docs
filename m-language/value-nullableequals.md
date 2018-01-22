---
title: "Value.NullableEquals | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c41d93f1-fc55-4c77-9815-d83ad648d6ec
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Value.NullableEquals

  
## About  
Returns a logical value or null based on two values .  
  
```  
Value.NullableEquals(value1 as any, value2 as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value1|The right value to compare.|  
|value2|The left value to compare.|  
  
## <a name="__toc360789738"></a>Remarks  
  
-   If either of the argument is null, it applies a nullable equality rules; otherwise, the same result as Value.Equals.  
  
## Example  
  
```  
Value.NullableEquals(1, null) equals null  
```  
