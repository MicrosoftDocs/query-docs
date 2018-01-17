---
title: "Table.FromPartitions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 03934fd6-b962-49b7-b4aa-ce88caab177b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Table.FromPartitions
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a table that is the result of combining a set of partitioned tables into new columns. The type of the column can optionally be specified, the default is any.  
  
```  
Table.FromPartitions ( partitionColumn as text, partitions as list, optional partitionColumnType as nullable type) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|partitionColumn|The name of the column where the values from the paritions will added.|  
|partitions|The list of partitions to combine, specificed in  {value, table} pairs.|  
|Optional partitionColumnType|The type of the resulting column (default is any).|  
  
## Example  
  
```  
Table.FromPartitions("Year",  
  
{{1994, Table.FromPartitions("Month", {  
  
    {"Jan", Table.FromPartitions("Day", {  
  
        {1, #table({"Column1"},{{"Column1 Value 1"}})},  
  
        {2, #table({"Column1"},{{"Column1 Value 2"}})}})},  
  
        {"Feb", Table.FromPartitions("Day",  
  
        {{3, #table({"Column1"},{{"Column1 Value 3"}})},  
  
        {4,  #table({"Column1"},{{"Column1 Value 4"}  
  
})}})}})}})  
  
equals  
```  
  
|Column1|Day|Month|Year|  
|-----------|-------|---------|--------|  
|Column1 Value 1|1|Jan|1994|  
|Column1 Value 2|2|Jan|1994|  
|Column1 Value 3|3|Feb|1994|  
|Column1 Value 4|4|Feb|1994|  
  
