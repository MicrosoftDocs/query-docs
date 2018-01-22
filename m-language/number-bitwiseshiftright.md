---
title: "Number.BitwiseShiftRight | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f3aeab4b-ae0c-4927-a08e-42a81955e0e4
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Number.BitwiseShiftRight

  
## About  
Returns the result of a bitwise shift right operation on the operands.  
  
```  
Number.BitwiseShiftRight(x as number, y as number) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The number to shift.|  
|y|The number of bits to shift.|  
  
## <a name="__toc360788807"></a>Remarks  
  
-   If y &gt; 0, the low-order bits shifted off are lost, and the high-order bits are filled with zeros.  
  
-   If y &lt; 0, the high-order bits shifted off are lost, and the low-order bits are filled with zeros.  
  
