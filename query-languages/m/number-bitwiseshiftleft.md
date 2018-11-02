---
title: "Number.BitwiseShiftLeft | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.BitwiseShiftLeft

  
## About  
Returns the result of a bitwise shift left operation on the operands.  
  
## Syntax

<pre>
Number.BitwiseShiftLeft(x as number, y as number) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The number to shift.|  
|y|The number of bits to shift.|  
  
## <a name="__toc360792371"></a>Remarks  
  
-   If y &gt; 0, the high-order bits shifted off are lost, and the low-order bits are filled with zeros.  
  
-   If y &lt; 0, the low-order bits shifted off are lost, and the high-order bits are filled with zeros.  
  
