---
title: "Number.BitwiseShiftLeft | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 919c1f49-6aed-425f-b077-d209e375d037
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.BitwiseShiftLeft

  
## About  
Returns the result of a bitwise shift left operation on the operands.  
  
```  
Number.BitwiseShiftLeft(x as number, y as number) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The number to shift.|  
|y|The number of bits to shift.|  
  
## <a name="__toc360792371"></a>Remarks  
  
-   If y &gt; 0, the high-order bits shifted off are lost, and the low-order bits are filled with zeros.  
  
-   If y &lt; 0, the low-order bits shifted off are lost, and the high-order bits are filled with zeros.  
  
