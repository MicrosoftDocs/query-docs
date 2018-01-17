---
title: "Record.SelectFields | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 070f9273-f10f-4e7a-9d5c-87ac82a3df7c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Record.SelectFields
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a new record that contains the fields selected from the input record. The original order of the fields is maintained.  
  
```  
Record.SelectFields(record as record,  fields as any,  optional missingField as nullable number) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The record to check.|  
|fields|A single field name or list of field names.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
-   MissingField.Error = 0;  
  
-   MissingField.Ignore = 1;  
  
-   MissingField.UseNull = 2;  
  
## Remarks  
  
-   The original order of the fields is maintained.  
  
## Examples  
  
```  
Record.SelectFields([A=1, B=2], "B") equals [B=2]  
```  
  
```  
Record.SelectFields([A=1, B=2, C=3], {"C", "B"}) equals [B=2, C=3]  
```  
