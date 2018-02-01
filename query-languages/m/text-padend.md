---
title: "Text.PadEnd | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7e6048a7-6fd2-4eac-b62f-5a89914eb13f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.PadEnd

  
## About  
Returns a text value padded at the end with pad to make it at least length characters.  
  
```  
Text.PadEnd(text as nullable text, length as number, pad as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|length|The length to pad to.|  
|pad|The text to pad with.|  
  
## <a name="__toc360788905"></a>Remarks  
  
-   If pad is not specified, whitespace is used as pad.  
  
## Example  
  
```  
Text.PadEnd("abc", 5, "a") equals "abcaa"  
```  
