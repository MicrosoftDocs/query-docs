---
title: "List.TransformMany | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 85e0d325-45f8-4bfc-a541-8a95dc6cb8e8
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.TransformMany
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a list whose elements are projected from the input list.  
  
```  
List.TransformMany(list as list, collectionTransform as Function, resultTransform as Function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|collectionTransform|The collectionTransform function is applied to each element, and the resultTransform function is invoked to construct the resulting list. The collectionSelector has the signature (x as any) =&gt; ? where x is an element in list.|  
|resultTransform|The resultTransform projects the shape of the result and has the signature (x as any, y as any) =&gt; ? where x is the element in list and y is the element obtained by applying the collectionTransform to that element.|  
  
## Example  
  
```  
List.TransformMany({1, 2}, (value) => {value + 1}, (oldValue, newValue) => oldValue * newValue) equals { 2, 6 }  
```  
