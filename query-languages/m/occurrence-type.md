---
description: "Learn more about: Occurrence.Type"
title: "Occurrence.Type"
ms.subservice: m-source
ms.topic: reference
---
# Occurrence.Type

## Definition

Specifies the occurrence of an element in a sequence.

## Allowed values

|Name|Value|Description|
| ------- | --- | ----------- |
|**Occurrence.First**|0|The position of the first occurrence of the found value is returned.|
|**Occurrence.Last**|1|The position of the last occurrence of the found value is returned.|
|**Occurrence.All**|2|A list of positions of all occurrences of the found values is returned.|
|**Occurrence.Optional**|0|The item is expected to appear zero or one time in the input. Provided for backward compatibility in binary functions. In this case, use [BinaryOccurrence.Optional](binaryoccurrence-type.md) instead.|
|**Occurrence.Required**|1|The item is expected to appear once in the input. Provided for backward compatibility in binary functions. In this case, use [BinaryOccurrence.Required](binaryoccurrence-type.md) instead.|
|**Occurrence.Repeating**|2|The item is expected to appear zero or more times in the input. Provided for backward compatibility in binary functions. In this case, use [BinaryOccurrence.Repeating](binaryoccurrence-type.md) instead.|

## Applies to

* [Table functions](table-functions.md)
* [Text functions](text-functions.md)
