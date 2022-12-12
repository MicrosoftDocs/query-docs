---
description: "Learn more about: New DAX functions"
title: "New DAX functions | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/20/2022
ms.subservice: dax 
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false
---
# New DAX functions

DAX is continuously being improved with new functions and functionality to support new features. New functions and updates are included in service, application, and tool updates which in most cases are monthly.

While functions and functionality are being updated all the time, only those updates that have a visible and functional change exposed to users are described in documentation. New functions and updates to existing functions within the past year are shown here.

> [!IMPORTANT]
> Not all functions are supported in all versions of Power BI Desktop, Analysis Services, and Power Pivot in Excel. New and updated functions are typically first introduced in Power BI Desktop, and then later in Analysis Services, Power Pivot in Excel, and tools.
  
## New functions

|Function  |Month  | Description |
|---------|---------|---------|
|[INDEX](index-function-dax.md)| December, 2022 | Returns a row at an absolute position, specified by the position parameter, within the specified partition, sorted by the specified order or on the specified axis.|
|[OFFSET](offset-function-dax.md)| December, 2022 | Returns a single row that is positioned either before or after the *current row* within the same table, by a given offset.|
|[ORDERBY](orderby-function-dax.md)| December, 2022 | Defines the columns that determine the sort order within each of a WINDOW function’s partitions.|
|[PARTITIONBY](partitionby-function-dax.md)| December, 2022 | Defines the columns that are used to partition a WINDOW function’s \<relation> parameter.|
|[WINDOW](window-function-dax.md)| December, 2022 | Returns multiple rows which are positioned within the given interval.  |
|[EVALUATEANDLOG](evaluateandlog-function-dax.md)| November, 2022 |  Returns the value of the first argument and logs it in a DAX Evaluation Log profiler event. |
|[TOCSV](tocsv-function-dax.md) | November, 2022 |  Returns a table as a string in CSV format. This function applies to Power BI Desktop only. |
|[TOJSON](tojson-function-dax.md) | November, 2022 |  Returns a table as a string in JSON format. This function applies to Power BI Desktop only. |
|[NETWORKDAYS](networkdays-dax.md)| July, 2022 |  Returns the number of whole workdays between two dates. |
