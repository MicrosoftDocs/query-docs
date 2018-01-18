---
title: "Table.FromColumns | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f32dc876-dcbe-41bf-9e8c-078515a981ce
caps.latest.revision: 9
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromColumns
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table from a list containing nested lists with the column names and values.  
  
```  
Table.FromColumns(lists as list, optional columns as any) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|lists|The List of lists to convert.|  
|optional columns|Optional parameter to provide names and types for the columns.|  
  
## <a name="__toc360789435"></a>Remarks  
  
-   If some columns have more values then others, the missing values will be filled with the default value, 'null', if the columns are nullable.  
  
## Examples  
  
```  
Table.FromColumns({  
  
    {1, "Bob", "123-4567"} , {2, "Jim", "987-6543"}, {3, "Paul", "543-7890"} })  
```  
  
|Column1|Column2|Column3|  
|-----------|-----------|-----------|  
|1|2|3|  
|Bob|Jim|Paul|  
|123-4567|987-6543|543-7890|  
  
