---
title: "Date.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: de657fe5-e60e-45d5-b024-46fc1860d8da
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.FromText

  
## About  
Returns a Date value from a set of date formats and culture value, following ISO 8601 format standard.  
  
```  
Date.FromText(date as nullable text, optional culture as nullable text) as nullable date  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|A string value to transorm.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### Supported formats  
  
-   yyyy-MM-dd  
  
-   YYYYMMDD  
  
-   M/d/yyyy  
  
### Terms  
  
-   Y = years  
  
-   M = months  
  
-   D = days  
  
## <a name="__toc360788938"></a>Remarks  
  
-   If the culture is not specified, the current user culture is used.  
  
## Example  
  
```  
Date.FromText("2010-02-19") equals Date,yyyy-MM-dd  
```  
