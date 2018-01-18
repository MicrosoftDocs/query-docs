---
title: "List.Product | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 16a68e6d-a9e5-458f-ab28-38a686c0d1b7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Product
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
