---
description: "Learn more about: LimitClauseKind.Type"
title: "LimitClauseKind.Type"
ms.date: 5/16/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# LimitClauseKind.Type

## Definition

Describes the type of limit clause supported by the SQL dialect used by this data source.

## Allowed values

|Name|Value|Description|  
|------------|--|---------------|  
|**LimitClauseKind.None**|0|This SQL dialect does not support a limit clause.|
|**LimitClauseKind.Top**|1|This SQL dialect supports a TOP specifier to limit the number of rows returned.|
|**LimitClauseKind.LimitOffset**|2|This SQL dialect supports LIMIT and OFFSET specifiers to limit the number of rows returned.|
|**LimitClauseKind.Limit**|3|This SQL dialect supports a LIMIT specifier to limit the number of rows returned.|
|**LimitClauseKind.AnsiSql2008**|4|This SQL dialect supports an ANSI SQL-compatible LIMIT N ROWS specifier to limit the number of rows returned.|

## Applies to

* [Accessing data functions](accessing-data-functions.md)
