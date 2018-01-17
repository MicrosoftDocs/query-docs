---
title: "List.SingleOrDefault | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 846fa33f-2a7b-4630-8674-9e2b2fc0aa8f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.SingleOrDefault
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
