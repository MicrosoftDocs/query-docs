---
title: "List.SingleOrDefault | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.SingleOrDefault

  
## About  
Returns a single item from a list.  
  
```  
List.SingleOrDefault(list as list, optional default as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|List|The List to check.|  
|optional default|Specifies a default value to be returned.|  
  
## <a name="__toc360789261"></a>Remarks  
  
-   If list is empty, a default value is returned instead.  
  
-   If default is not specified, the default value of null is assumed.  
  
-   If list has more than one item, an error is returned.  
  
## Examples  
  
```  
List.SingleOrDefault({1}) equals 1  
```  
  
```  
List.SingleOrDefault({1, 2, 3}) equals error  
```  
  
```  
List.SingleOrDefault({}, 0) equals 0  
```  
