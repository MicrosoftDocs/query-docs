---
title: "Binary.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 96fe975c-982e-41c9-9e6c-35b386ff344f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Binary.ToText

  
## About  
Encodes binary data into a text form.  
  
```  
Binary.ToText(binary as binary, encoding as number) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|The binary data to encode.|  
|encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
