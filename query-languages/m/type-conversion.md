---
description: "Learn more about: Types and type conversion"
title: "Types and type conversion"
ms.topic: conceptual
ms.date: 12/20/2024
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Types and type conversion

Power Query M uses types to classify values to have a more structured data set. This article describes the most commonly-used M types and how to convert one type to another type.

## Commonly-used types

Data types refers to any type that's used to clarify the structure of specific data. The most commonly used data types are primitive types. These types include:

* `type any`, which classifies any value.
* `type null`, which classifies the null value.
* `type logical`, which classifies the values true and false.
* `type number`, which classifies number values.
* `type time`, which classifies time values.
* `type date`, which classifies date values.
* `type datetime`, which classifies datetime values.
* `type datetimezone`, which classifies datetimezone values.
* `type duration`, which classifies duration values.
* `type text`, which classifies text values.
* `type binary`, which classifies binary values.
* `type type`, which classifies type values.
* `type list`, which classifies list values.
* `type record`, which classifies record values.
* `type table`, which classifies table values.
* `type function`, which classifies function values.
* `type anynonnull`, which classifies all values excluding null.
* `type none`, which classifies no values.

For more information about these types, go to [Types](m-spec-types.md).

In addition to these common data types, there is also a set of data types using the format `*.Type`. The most commonly used data types of this format are:

* `Byte.Type`, which classifies an 8-bit number value.
* `Int8.Type`, which classifies an 8-bit number value.
* `Int16.Type`, which classifies a 16-bit number value.
* `Int32.Type`, which classifies a 32-bit number value.
* `Int64.Type`, which classifies a 64-bit number value.
* `Single.Type`, which classifies a 9-digit floating number value.
* `Double.Type`, which classifies a 17-digit floating number value.
* `Decimal.Type`, which classifies a 15-digit floating number value.
* `Currency.Type`, which classifies a 19-digit number value with four digits to the right of the "." separator.
* `Percentage.Type`, which classifies a 15-digit number value with a mask to format the value as a percentage.
* `Guid.Type`, which classifies a GUID text value.

The primitive types can also be written in the `*.Type` format as well. Therefore, you can write `number` as `Number.Type`, `record` as `Record.Type`, and so on.

When you use any of these types, be aware that, like all M code, these types are case-sensitive.

The following table contains more information about each of these types.

|Data type | Description|
|----------|------------|
|`any`|The `any` data type is the status given when a value doesn't have an explicit data type definition. The `any` type is the data type that classifies all values.|
|`binary`|The `binary` data type can be used to represent any other data with a binary format.|
|`type`| A value that classifies other values. For more information, go to [Types](m-spec-types.md). |
|`null`| Represents the absence of a value, or a value of indeterminate or unknown state. |
|`anynonnull`| Represents any type that is nonnullable.|
|`date` | Represents just a date (no time portion).|
|`time`|Represents just time (no date portion).|
|`datetime` |Represents both a date and time value. The time portion of a date is stored as a fraction to whole multiples of 1/300 seconds (3.33 ms). Dates between the years 1900 and 9999 are supported.|
|`datetimezone` |Represents a UTC date and time with a time-zone offset.|
|`duration`| Represents a length of time. This type can be added or subtracted from a `datetime` field with correct results. For more information, go to [Duration](m-spec-values.md#duration).|
|`text`|A Unicode character data string. Can be strings, numbers, or dates represented in a text format. Maximum string length is 268,435,456 Unicode characters (where each Unicode character is two bytes) or 536,870,912 bytes.|
|`logical`|A Boolean value of either `true` or `false`.|
|`list`| A value which produces a sequence of values when enumerated. For more information, go to [List types](m-spec-types.md#list-types) and [List values](m-spec-values.md#list).|
|`record`| An ordered sequence of fields. Each field contains a field name and field value. For more information, go to [Record types](m-spec-types.md#record-types) and [Record values](m-spec-values.md#record).|
|`table`| An ordered sequence of rows divided into columns. For more information, go to [Table types](m-spec-types.md#table-types) and [Table values](m-spec-values.md#table).|
|`function`| A value that maps a set of arguments to a single value. For more information, go to [Functions](m-spec-functions.md) and [Function types](m-spec-types.md#function-types).|
|`number`| Represents any number used for numeric and arithmetic operations. For more information, go to [Number](m-spec-values.md#number).|
|`Decimal.Type`|Represents a 64-bit (eight-byte) floating-point number. It's the most common number type, and corresponds to numbers as you usually think of them. Although designed to handle numbers with fractional values, it also handles whole numbers. The `Decimal.Type` can handle negative values from &ndash;1.79E +308 through &ndash;2.23E &ndash;308, 0, and positive values from 2.23E &ndash;308 through 1.79E + 308. For example, numbers like 34, 34.01, and 34.000367063 are valid decimal numbers. The largest precision that can be represented in a `Decimal.Type` is 15 digits long. The decimal separator can occur anywhere in the number. The `Decimal.Type` corresponds to how Excel stores its numbers. Note that a binary floating-point number can't represent all numbers within its supported range with 100% accuracy. Thus, minor differences in precision might occur when representing certain decimal numbers.|
| `Currency.Type` | This data type has a fixed location for the decimal separator. The decimal separator always has four digits to its right and allows for 19 digits of significance. The largest value it can represent is 922,337,203,685,477.5807 (positive or negative). Unlike `Decimal.Type`, the `Currency.Type` is always precise and is thus useful in cases where the imprecision of floating-point notation might introduce errors.|
|`Percentage.Type` | Fundamentally the same as a `Decimal.Type`, but it has a mask to format the values as a percentage value.|
|`Int8.Type`| Represents an 8-bit (one-byte) signed integer value. Because it's an integer, it has no digits to the right of the decimal place. It allows for 3 digits; a positive or negative whole number between &ndash;128 and 127. As with the `Currency.Type`, the `Int8.Type` can be useful in cases where you need to control rounding.|
|`Int16.Type`| Represents a 16-bit (two-byte) signed integer value. Because it's an integer, it has no digits to the right of the decimal place. It allows for 6 digits; a positive or negative whole number between &ndash;32,768 (&ndash;2^15) and 32,767 (2^15-1). As with the `Currency.Type`, the `Int16.Type` can be useful in cases where you need to control rounding.|
|`Int32.Type`| Represents a 32-bit (four-byte) signed integer value. Because it's an integer, it has no digits to the right of the decimal place. It allows for 10 digits; a positive or negative whole number between &ndash;2,147,483,648 (&ndash;2^31) and 2,147,483,647 (2^31&ndash;1). As with the `Currency.Type`, the `Int32.Type` can be useful in cases where you need to control rounding.|
|`Int64.Type` | Represents a 64-bit (eight-byte) signed integer value. Because it's an integer, it has no digits to the right of the decimal place. It allows for 19 digits; a positive or negative whole number between &ndash;9,223,372,036,854,775,808 (&ndash;2^63) and 9,223,372,036,854,775,807 (2^63&ndash;1). It can represent the largest possible precision of the various numeric data types. As with the `Currency.Type`, the `Int64.Type` can be useful in cases where you need to control rounding. |
|`Byte.Type`| Represents an 8-bit (one-byte) unsigned integer value. Because it's an unsigned integer, it has no digits to the right of the decimal place and can only contain positive values. It allows for 3 digits; a positive number between 0 and 255.|
|`Single.Type`| Represents a single-precision floating-point number. It has an approximate range of &ndash;3.99 X 10<sup>38</sup> to 3.99 X 10<sup>38</sup> and supports approximately 9 digits of precision. It can also represent positive and negative infinity, and NaN (Not a Number).|
|`Double.Type`| Represents a double-precision floating-point number. It has an approximate range of &ndash;1.7976931348623158 X 10<sup>307</sup> to 1.7976931348623158 X 10<sup>307</sup> and supports approximately 17 digits of precision. It can also represent positive and negative infinity, and NaN (Not a Number).|
|`Guid.Type`| Represents a 128-bit text value consisting of 32 hexadecimal values using the form factor of \<8 hex values>-\<4 hex values>-\<4 hex values>-\<4 hex values>-\<12 hex values>, which make up the GUID value.|
|`none`|The data type that classifies no values. |

The only other commonly used `*.Type` values are enumerations. For more information, go to [Enumerations](enumerations.md).

## Type conversion

The Power Query M formula language has formulas to convert between types. The following is a summary of conversion formulas in M.
  
### Number  
  
|Type conversion|Description|  
|-------------------|---------------|  
|Number.FromText(text as text) as number|Returns a number value from a text value.|  
|Number.ToText(number as number) as text|Returns a text value from a number value.|  
|Number.From(value as any) as number|Returns a number value from a value.|  
|Byte.From(value as any) as number|Returns an 8-bit integer number value from the given value.|
|Int8.From(value as any) as number|Returns an 8-bit integer number value from the given value.|
|Int16.From(value as any) as number|Returns a 16-bit integer number value from the given value.|
|Int32.From(value as any) as number|Returns a 32-bit integer number value from the given value.|  
|Int64.From(value as any) as number|Returns a 64-bit integer number value from the given value.|  
|Single.From(value as any) as number|Returns a Single number value from the given value.|  
|Double.From(value as any) as number|Returns a Double number value from the given value.|  
|Decimal.From(value as any) as number|Returns a Decimal number value from the given value.|  
|Currency.From(value as any) as number|Returns a Currency number value from the given value.|  
|Percentage.From(value as any) as number|Returns a Percentage number value from the given value.|
  
### Text  
  
|Type conversion|Description|  
|-------------------|---------------|  
|Text.From(value as any) as text|Returns the text representation of a number, date, time, datetime, datetimezone, logical, duration or binary value.|  
|Guid.From(value as text) as text|Returns the GUID representation of the specified text.|
  
### Logical  
  
|Type conversion|Description|  
|-------------------|---------------|  
|Logical.FromText(text as text) as logical|Returns a logical value of true or false from a text value.|  
|Logical.ToText(logical as logical) as text|Returns a text value from a logical value.|  
|Logical.From(value as any) as logical|Returns a logical value from a value.|  
  
### Date, Time, DateTime, and DateTimeZone  
  
|Type conversion|Description|  
|-------------------|---------------|  
|.FromText(text as text) as date, time, datetime, or datetimezone|Returns a date, time, datetime, or datetimezone value from a set of date formats and culture value.|  
|.ToText(date, time, dateTime, or dateTimeZone as date, time, datetime, or datetimezone) as text|Returns a text value from a date, time, datetime, or datetimezone value.|  
|.From(value as any)|Returns a date, time, datetime, or datetimezone value from a value.|  
|.ToRecord(date, time, dateTime, or dateTimeZone as date, time, datetime, or datetimezone)|Returns a record containing parts of a date, time, datetime, or datetimezone value.|  

## Related content

* [Types](m-spec-types.md)
* [Power Query M type system](power-query-m-type-system.md)
