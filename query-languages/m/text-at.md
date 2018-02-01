---
title: "Text.At | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c6dfb8bc-6ba6-46fd-9c9a-6ca9964bb404
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.At

  
## About  
Returns a character starting at a zero-based offset.  
  
```  
Text.At(value as nullable text, index as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to parse.|  
|index|The index of the character to return.|  
  
## <a name="__toc360788840"></a>Remarks  
  
-   If the offset is greater than index, an Expression.Error is thrown.  
  
## Examples  
  
```  
Text.At("abcd", 0) equals "a"  
```  
  
```  
Text.At("abcd", 5) equals error  
```  
