---
description: "Learn more about: GroupKind.Type"
title: "GroupKind.Type"
ms.subservice: m-source
ms.topic: reference
---

# GroupKind.Type

## About

Specifies the kind of grouping to apply to a table.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`GroupKind.Local`|0|A local group is formed from a consecutive sequence of rows from an input table with the same key value. Note that multiple local groups may be produced with the same key value.|
|`GroupKind.Global`|1|A global group is formed from all rows in an input table with the same key value. Note that only a single global group is produced for a given key value.|

## Related content

* [Table functions](table-functions.md)
