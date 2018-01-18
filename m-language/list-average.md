---
title: "List.Average | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 04adad51-5731-481a-b022-79b7abb2ccc9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Average
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns an average value from a list in the datatype of the values in the list.  
  
```  
List.Average(list as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789372"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Examples  
  
```  
List.Average({1, 2, 3}) equals 2  
```  
  
```  
List.Average({#duration(0, 0, 30, 0), #duration(0, 0, 40, 0)}) equals #duration(0, 0, 35, 0)  
```  
  
```  
List.Average({#date(2011,1,1), #date(2011,1,2), #date(2011,1,3)})  equals #datetime(2011,1,2)  
```  
  
```  
List.Average({}) equals null  
```  
