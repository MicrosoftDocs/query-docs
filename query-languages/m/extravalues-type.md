---
description: "Learn more about: ExtraValues.Type"
title: "ExtraValues.Type"
---
# ExtraValues.Type

## Definition

Specifies the expected action for extra values in a row that contains columns less than expected.

## Allowed values

|Name|Value|Description|
| ------- | --- | ----------- |
|**ExtraValues.List**|0|If the splitter function returns more columns than the table expects, they should be collected into a list.|
|**ExtraValues.Error**|1| If the splitter function returns more columns than the table expects, an error should be raised.|
|**ExtraValues.Ignore**|2|If the splitter function returns more columns than the table expects, they should be ignored.|

## Applies to

* [Accessing data functions](accessing-data-functions.md)
* [Table functions](table-functions.md)
