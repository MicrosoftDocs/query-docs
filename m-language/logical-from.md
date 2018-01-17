---
title: "Logical.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2f18a410-229f-416b-b86e-8f1ea184ea3e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Logical.From
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
