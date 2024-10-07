---
description: "Learn more about: Type conversion"
title: "Type conversion"
ms.topic: conceptual
ms.date: 10/7/2024
ms.custom: "nonautomated-date"
---

# Type conversion

The Power Query M formula language has formulas to convert between types. The following is a summary of conversion formulas in M.
  
## Number  
  
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
  
## Text  
  
|Type conversion|Description|  
|-------------------|---------------|  
|Text.From(value as any) as text|Returns the text representation of a number, date, time, datetime, datetimezone, logical, duration, or binary value.|  
  
## Logical  
  
|Type conversion|Description|  
|-------------------|---------------|  
|Logical.FromText(text as text) as logical|Returns a logical value of true or false from a text value.|  
|Logical.ToText(logical as logical) as text|Returns a text value from a logical value.|  
|Logical.From(value as any) as logical|Returns a logical value from a value.|  
  
## Date, Time, DateTime, and DateTimeZone  
  
|Type conversion|Description|  
|-------------------|---------------|  
|.FromText(text as text) as date, time, datetime, or datetimezone|Returns a date, time, datetime, or datetimezone value from a set of date formats and culture value.|  
|.ToText(date, time, dateTime, or dateTimeZone as <br />date, time, datetime, or datetimezone) as text|Returns a text value from a date, time, datetime, or datetimezone value.|  
|.From(value as any)|Returns a date, time, datetime, or datetimezone value from a value.|  
|.ToRecord(date, time, dateTime, or dateTimeZone as date, time, datetime, or datetimezone)|Returns a record containing parts of a date, time, datetime, or datetimezone value.|  
