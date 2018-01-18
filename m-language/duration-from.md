---
title: "Duration.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b396d035-4c1c-4fcb-b603-c83da4121d2d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Duration.From
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a duration value from a value.  
  
```  
Duration.From(value as any) as nullable duration  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
  
Values of the following types can be converted to a duration value:  
  
|**Type to Convert**|**Description**|  
|-----------------------|-------------------|  
|text|Returns a duration value from a text value in a elapsed time format of d.h:m:s. For more details, see Duration.FromText.|  
|number|A duration equivalent to the number of whole and fractional days expressed by value.|  
|Any other type|An error is returned|  
  
## <a name="__toc360789120"></a>Remarks  
  
-   If a value is null, Duration.From returns null.  
  
-   If a value is duration, the same value is returned.  
  
## Example  
  
```  
Duration.From(2.525) equals #duration(2,12,36,0)  
```  
