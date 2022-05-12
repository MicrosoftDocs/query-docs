---
description: "Learn more about: JoinKind.Type"
title: "JoinKind.Type | Microsoft Docs"
ms.date: 5/11/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# JoinKind.Type

## Definition

Specifies the kind of join operation.

## Allowed values

|Allowed values|Value|Description|
| ------- | --- | ----------- |
|**Inner**|0| The table resulting from an inner join contains a row for each pair of rows from the specified tables that were determined to match based on the specified key columns.|
|**LeftOuter**|1| A left outer join ensures that all rows of the first table appear in the result.|
|**RightOuter**|2| A right outer join ensures that all rows of the second table appear in the result.|
|**FullOuter**|3| A full outer join ensures that all rows of both tables appear in the result. Rows that did not have a match in the other table are joined with a default row containing null values for all of its columns.|
|**LeftAnti**|4| A left anti join returns that all rows from the first table which do not have a match in the second table.|
|**RightAnti**|5| A right anti join returns that all rows from the second table which do not have a match in the first table.|

## Remarks

The fields of this enumeration are possible values for the optional `JoinKind` parameter in [Table.Join](table-join.md).

## Applies to

* [Table functions](table-functions.md)
