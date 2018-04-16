---
title: "List.Product | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Product

  
## About  
Returns the product from a list of numbers.  
  
```  
List.Product(list as list) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789396"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Examples  
  
```  
List.Product({2, 3, 4}) equals 24  
```  
  
```  
List.Product({}) equals error  
```  
