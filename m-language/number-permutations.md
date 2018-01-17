---
title: "Number.Permutations | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 835d85bd-24a5-414e-a72f-bc1c2f03ee8c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.Permutations
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the number of total permutatons of a given number of items for the optional permutation size.  
  
```  
Number.Permutations(setSize as nullable number, permutationSize as nullable number)  as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|setSize|Number of permutation items.|  
|permutationSize|Size of permutations.|  
  
## Example  
  
```  
Number.Permutations(5, 3) equals 60  
```  
