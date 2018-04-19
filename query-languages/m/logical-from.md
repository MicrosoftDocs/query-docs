---
title: "Logical.From | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.From

  
## About  
Returns a logical value from a value.  
  
`Logical.From(value as any) as nullable logical`  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
  
## Type to convert  
  
|**Type**|**Description**|  
|------------|-------------------|  
|text|Returns a logical value of "true" or "false" from the text value. For more details, see **Logical.FromText**.|  
|number|If value equals 0, true; otherwise, false.|  
|any other type|An Expression.Error is thrown.|  
  
## <a name="__toc360788933"></a>Remarks  
  
-   If value is null, Logical.From returns null.  
  
-   If a value is logical, the same value is returned.  
  
## Example  
  
```  
Logical.From(2) equals true  
```  
