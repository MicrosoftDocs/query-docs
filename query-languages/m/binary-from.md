---
title: "Binary.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e636399e-f91a-48b3-8b6f-a154ce72f5a0
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Binary.From

  
## About  
Returns a binary value from the given value.  
  
```  
Binary.From(Value as any, optional encoding as nullable number) as nullable binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|A binary value from the text representation. For more information, see Binary.FromText.|  
|optional encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
## <a name="__toc360789856"></a>Remarks  
  
-   If the given value is null, Binary.From returns null.  If the given value is binary, the same value is returned.  
  
-   Values of the following types can be converted to a binary value:  
  
-   If value is of any other type, an error is returned.  
  
## Example  
  
```  
Binary.From("1011")equals Binary.FromText("1011", BinaryEncoding.Base64)  
```  
