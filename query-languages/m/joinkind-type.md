---
description: "Learn more about: JoinKind.Type"
title: "JoinKind.Type"
ms.subservice: m-source
ms.topic: reference
---

# JoinKind.Type

## About

Specifies the kind of join operation.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`JoinKind.Inner`|0|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). The table resulting from an inner join contains a row for each pair of rows from the specified tables that were determined to match based on the specified key columns.|
|`JoinKind.LeftOuter`|1|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A left outer join ensures that all rows of the first table appear in the result.|
|`JoinKind.RightOuter`|2|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A right outer join ensures that all rows of the second table appear in the result.|
|`JoinKind.FullOuter`|3|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A full outer join ensures that all rows of both tables appear in the result. Rows that did not have a match in the other table are joined with a default row containing null values for all of its columns.|
|`JoinKind.LeftAnti`|4|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A left anti join returns all rows from the first table that do not have a match in the second table.|
|`JoinKind.RightAnti`|5|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A right anti join returns all rows from the second table that do not have a match in the first table.|
|`JoinKind.LeftSemi`|6|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A left semi join returns all rows from the first table that have a match in the second table.|
|`JoinKind.RightSemi`|7|A possible value for the optional `JoinKind` parameter in [`Table.Join`](table-join.md). A right semi join returns all rows from the second table that have a match in the first table.|
