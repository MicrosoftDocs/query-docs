---
title: M Language values 
description: Describes using values in the Power Query M formula language
ms.topic: conceptual
ms.date: 11/29/2021
---

# Values

A value is data produced by evaluating an expression. This section describes the kinds of values in the M language. Each kind of value is associated with a literal syntax, a set of values that are of that kind, a set of operators defined over that set of values, and an intrinsic type ascribed to newly constructed values.

| Kind | Literal |
| ---- | ------- |
| _Null_ |  `null` |
| _Logical_ | `true`&nbsp;&nbsp;&nbsp;&nbsp;`false` |
| _Number_ | `0`&nbsp;&nbsp;&nbsp;&nbsp;`1`&nbsp;&nbsp;&nbsp;&nbsp;`-1`&nbsp;&nbsp;&nbsp;&nbsp;`1.5`&nbsp;&nbsp;&nbsp;&nbsp;`2.3e-5` |
| _Time_ | `#time(09,15,00)` |
| _Date_ | `#date(2013,02,26)` |
| _DateTime_ | `#datetime(2013,02,26, 09,15,00)` |
| _DateTimeZone_ | `#datetimezone(2013,02,26, 09,15,00, 09,00)` |
| _Duration_ | `#duration(0,1,30,0)` |
| _Text_ | `"hello"` |
| _Binary_ | `#binary("AQID")` |
| _List_ | `{1, 2, 3}` |
| _Record_ | `[ A = 1, B = 2 ]` |
| _Table_ | `#table({"X","Y"},{{0,1},{1,0}})` |
| _Function_ | `(x) => x + 1` |
| _Type_ | `type { number }`&nbsp;&nbsp;&nbsp;&nbsp;`type table [ A = any, B = text ]` |
| | |
 
The following sections cover each value kind in detail. Types and type ascription are defined formally in [Types](m-spec-types.md). Function values are defined in [Functions](m-spec-functions.md). The following sections list the operators defined for each value kind and give examples. The full definition of operator semantics follows in [Operators](m-spec-operators.md).

## Null

A _null value_ is used to represent the absence of a value, or a value of indeterminate or unknown state. A null value is written using the literal `null`. The following operators are defined for null values: 
 
| Operator | Result |
| -------- | ------ |
| `x > y` | Greater than |
| `x >= y` | Greater than or equal |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x ?? y` | Coalesce |
| | | 
 
The native type of the `null` value is the intrinsic type `null`.

## Logical

A _logical value_ is used for Boolean operations has the value true or false. A logical value is written using the literals `true` and `false`. The following operators are defined for logical values:

| Operator | Result |
| -------- | ------ |
| `x > y` | Greater than |
| `x >= y` | Greater than or equal |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x or y` | Conditional logical OR |
| `x ?? y` | Coalesce |
| `x and y` | Conditional logical AND |
| `not x` | Logical NOT |
| | |  
 
The native type of both logical values (`true` and `false`) is the intrinsic type `logical`.

## Number

A _number value_ is used for numeric and arithmetic operations. The following are examples of number literals:

```
3.14  // Fractional number 
-1.5  // Fractional number 
1.0e3 // Fractional number with exponent
123   // Whole number 
1e3   // Whole number with exponent 
0xff  // Whole number in hex (255)
```

A number is represented with at least the precision of a _Double_ (but may retain more precision). The _Double_ representation is congruent with the IEEE 64-bit double precision standard for binary floating point arithmetic defined in [IEEE 754-2008]. (The _Double_ representation have an approximate dynamic range from 5.0 x 10<sup>324</sup> to 1.7 x 10<sup>308</sup> with a precision of 15-16 digits.)

The following special values are also considered to be _number_ values:

* Positive zero and negative zero. In most situations, positive zero and negative zero behave identically as the simple value zero, but [certain operations distinguish between the two](m-spec-operators.md#arithmetic-operators).

* Positive infinity (`#infinity`) and negative infinity (`-#infinity`). Infinities are produced by such operations as dividing a non-zero number by zero. For example, `1.0 / 0.0` yields positive infinity, and `-1.0 / 0.0` yields negative infinity.

* The _Not-a-Number_ value (`#nan`), often abbreviated NaN. NaNs are produced by invalid floating-point operations, such as dividing zero by zero.

Binary mathematical operations are performed using a _Precision_. The precision determines the domain to which the operands are rounded and the domain in which the operation is performed. In the absence of an explicitly specified precision, such operations are performed using _Double Precision_.

* If the result of a mathematical operation is too small for the destination format, the result of the operation becomes positive zero or negative zero.

* If the result of a mathematical operation is too large for the destination format, the result of the operation becomes positive infinity or negative infinity.

* If a mathematical operation is invalid, the result of the operation becomes NaN.

* If one or both operands of a floating-point operation is NaN, the result of the operation becomes NaN.

The following operators are defined for number values:

| Operator | Result |
| -------- | ------ |
| `x > y` | Greater than |
| `x >= y` | Greater than or equal |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x + y` | Sum |
| `x - y` | Difference |
| `x * y` | Product |
| `x / y` | Quotient |
| `x ?? y` | Coalesce |
| `+x` | Unary plus |
| `-x` | Negation |
| | |

The native type of number values is the intrinsic type `number`.

## Time

A _time value_ stores an opaque representation of time of day. A time is encoded as the number of _ticks since midnight_, which counts the number of 100-nanosecond ticks that have elapsed on a 24-hour clock. The maximum number of _ticks since midnight_ corresponds to 23:59:59.9999999 hours.

Time values may be constructed using the #time instrinsic.

```
#time(hour, minute, second)
```

The following must hold or an error with reason code `Expression.Error` is raised:

0 &le; hour &le; 24<br/>
0 &le; minute &le; 59<br/>
0 &le; second &le; 59

In addition, if hour = 24, then minute and second must be zero.

The following operators are defined for time values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |

The following operators permit one or both of their operands to be a date:

| Operator | Left Operand | Right Operand | Meaning |
| -------- | ------------ | ------------- | ------- |
| `x + y` | `time` | `duration` | Date offset by duration |
| `x + y` | `duration` | `time` | Date offset by duration |
| `x - y` | `time` | `duration` | Date offset by negated duration |
| `x - y` | `time` | `time` | Duration between dates |
| `x & y` | `date` | `time` | Merged datetime |
| | | | |
 
The native type of time values is the intrinsic type `time`.

## Date

A _date value_ stores an opaque representation of a specific day. A date is encoded as a number of _days since epoch_, starting from January 1, 0001 Common Era on the Gregorian calendar. The maximum number of days since epoch is 3652058, corresponding to December 31, 9999.

Date values may be constructed using the `#date` intrinsic.

```
#date(year, month, day)
```

The following must hold or an error with reason code `Expression.Error` is raised:

1 &le; year &le; 9999<br/>
1 &le; month &le; 12<br/>
1 &le; day &le; 31

In addition, the day must be valid for the chosen month and year.

The following operators are defined for date values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |

The following operators permit one or both of their operands to be a date:

| Operator | Left Operand | Right Operand | Meaning |
| -------- | ------------ | ------------- | ------- |
| `x + y` | `date` | `duration` | Date offset by duration |
| `x + y` | `duration` | `date` | Date offset by duration |
| `x - y` | `date` | `duration` | Date offset by negated duration |
| `x - y` | `date` | `date` | Duration between dates |
| `x & y` | `date` | `time` | Merged datetime |
| | | | |

The native type of date values is the intrinsic type `date`.

## DateTime
A _datetime value_ contains both a date and time.

DateTime values may be constructed using the `#datetime` intrinsic.

```
#datetime(year, month, day, hour, minute, second)
```

The following must hold or an error with reason code Expression.Error is raised: 
1 &le; year &le; 9999<br/>
1 &le; month &le; 12<br/>
1 &le; day &le; 31<br/>
0 &le; hour &le; 23<br/>
0 &le; minute &le; 59<br/>
0 &le; second &le; 59

In addition, the day must be valid for the chosen month and year.

The following operators are defined for datetime values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |
 
The following operators permit one or both of their operands to be a datetime:
 
| Operator | Left Operand | Right Operand | Meaning |
| -------- | ------------ | ------------- | ------- |
| `x + y` | `datetime` | `duration` | Datetime offset by duration |
| `x + y` | `duration` | `datetime` | Datetime offset by duration |
| `x - y` | `datetime` | `duration` | Datetime offset by negated duration |
| `x - y` | `datetime` | `datetime` | Duration between datetimes |
| | | | |

The native type of datetime values is the intrinsic type `datetime`.

## DateTimeZone

A _datetimezone_ value contains a datetime and a timezone. A _timezone_ is encoded as a number of _minutes offset from UTC_, which counts the number of minutes the time portion of the _datetime_ should be offset from Universal Coordinated Time (UTC). The minimum number of _minutes offset from UTC_ is -840, representing a UTC offset of -14:00, or fourteen hours earlier than UTC. The maximum number of _minutes offset from UTC_ is 840, corresponding to a UTC offset of 14:00.

DateTimeZone values may be constructed using the `#datetimezone` intrinsic.

```
#datetimezone(
       year, month, day,
       hour, minute, second,
       offset-hours, offset-minutes)
```

The following must hold or an error with reason code `Expression.Error` is raised:

1 &le; year &le; 9999<br/>
1 &le; month &le; 12<br/>
1 &le; day &le; 31<br/>
0 &le; hour &le; 23<br/>
0 &le; minute &le; 59<br/>
0 &le; second &le; 59<br/>
-14 &le; offset-hours &le; 14<br/>
-59 &le; offset-minutes &le; 59

In addition, the day must be valid for the chosen month and year and, if offset-hours = 14, then offset-minutes <= 0 and, if offset-hours = -14, then offset-minutes >= 0.

The following operators are defined for datetimezone values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |
 
The following operators permit one or both of their operands to be a datetimezone:
 
| Operator | Left Operand | Right Operand | Meaning |
| -------- | ------------ | ------------- | ------- |
| `x + y` | `datetimezone` | `duration` | Datetimezone offset by duration |
| `x + y` | `duration` | `datetimezone` | Datetimezone offset by duration |
| `x - y` | `datetimezone` | `duration` | Datetimezone offset by negated duration |
| `x - y` | `datetimezone` | `datetimezone` | Duration between datetimezones |
| | | | |

The native type of datetimezone values is the intrinsic type `datetimezone`.

## Duration

A _duration value_ stores an opaque representation of the distance between two points on a timeline measured 100-nanosecond ticks. The magnitude of a _duration_ can be either positive or negative, with positive values denoting progress forwards in time and negative values denoting progress backwards in time. The minimum value that can be stored in a _duration_ is -9,223,372,036,854,775,808 ticks, or 10,675,199 days 2 hours 48 minutes 05.4775808 seconds backwards in time. The maximum value that can be stored in a _duration_ is 9,223,372,036,854,775,807 ticks, or 10,675,199 days 2 hours 48 minutes 
05.4775807 seconds forwards in time.

Duration values may be constructed using the `#duration` intrinsic function:

```
#duration(0, 0, 0, 5.5)          // 5.5 seconds 
#duration(0, 0, 0, -5.5)         // -5.5 seconds 
#duration(0, 0, 5, 30)           // 5.5 minutes 
#duration(0, 0, 5, -30)          // 4.5 minutes 
#duration(0, 24, 0, 0)           // 1 day 
#duration(1, 0, 0, 0)            // 1 day
```

The following operators are defined on duration values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |

Additionally, the following operators allow one or both of their operands to be a duration value:

| Operator | Left Operand | Right Operand | Meaning |
| -------- | ------------ | ------------- | ------- |
| `x + y` | `datetime` | `duration` | Datetime offset by duration |
| `x + y` | `duration` | `datetime` | Datetime offset by duration |
| `x + y` | `duration` | `duration` | Sum of durations |
| `x - y` | `datetime` | `duration` | Datetime offset by negated duration |
| `x - y` | `datetime` | `datetime` | Duration between datetimes |
| `x - y` | `duration` | `duration` | Difference of durations |
| `x * y` | `duration` | `number` | N times a duration |
| `x * y` | `number` | `duration` | N times a duration |
| `x / y` | `duration` | `number` | Fraction of a duration |
| | | | |

The native type of duration values is the intrinsic type `duration`.

## Text

A _text_ value represents a sequence of Unicode characters. Text values have a literal form conformant to the following grammar:

_text-literal:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"` text-literal-characters<sub>opt</sub>  `"`<br/>
_text-literal-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal-character text-literal-characters<sub>opt</sub><br/> 
text-literal-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-text-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;character-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;double-quote-escape-sequence<br/>
single-text-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`)<br/>
_double-quote-escape-sequence:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`""` (`U+0022`, `U+0022`)

The following is an example of a _text_ value:

```
"ABC" // the text value ABC
```

The following operators are defined on _text_ values: 
 
| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x & y` | Concatenation |
| `x ?? y` | Coalesce |
| | |

The native type of text values is the intrinsic type `text`.

## Binary

A _binary value_ represents a sequence of bytes. There is no literal format. Several standard library functions are provided to construct binary values. For example, `#binary` can be used to construct a binary value from a list of bytes:

```
#binary( {0x00, 0x01, 0x02, 0x03} )
```

The following operators are defined on _binary_ values:
 
| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x >= y` | Greater than or equal |
| `x > y` | Greater than |
| `x < y` | Less than |
| `x <= y` | Less than or equal |
| `x ?? y` | Coalesce |
| | |

The native type of binary values is the intrinsic type _binary_.

## List

A _list value_ is a value which produces a sequence of values when enumerated. A value produced by a list can contain any kind of value, including a list. Lists can be constructed using the initialization syntax, as follows:

_list-expression:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ _item-list<sub>opt</sub>_  }<br/>
_item-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item_ `,`  _item-list<br/>
item:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_  `..` _expression_

The following is an example  of a _list-expression_ that defines a list with three text values: `"A"`, `"B"`, and `"C"`.

```
{"A", "B", "C"}
```

The value `"A"` is the first item in the list, and the value `"C"` is the last item in the list.

* The items of a list are not evaluated until they are accessed.
* While list values constructed using the list syntax will produce items in the order they appear in _item-list_, in general, lists returned from library functions may produce a different set or a different number of values each time they are enumerated.

To include a sequence of whole number in a list, the `a..b` form can be used:

```
{ 1, 5..9, 11 }     // { 1, 5, 6, 7, 8, 9, 11 }
```

The number of items in a list, known as the _list count_, can be determined using the `List.Count` function.

```
List.Count({true, false})  // 2 
List.Count({})             // 0
```

A list may effectively have an infinite number of items; `List.Count` for such lists is undefined and may either raise an error or not terminate.

If a list contains no items, it is called an _empty list_. An empty list is written as:

```
{}  // empty list
```

The following operators are defined for lists:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x & y` | Concatenate |
| `x ?? y` | Coalesce |
| | |

For example:

```
{1, 2} & {3, 4, 5}   // {1, 2, 3, 4, 5} 
{1, 2} = {1, 2}      // true 
{2, 1} <> {1, 2}     // true
```

The native type of list values is the intrinsic type `list`, which specifies an item type of `any`.

## Record

A _record value_ is an ordered sequence of fields. A _field_ consists of a _field name_, which is a text value that uniquely identifies the field within the record, and a _field value_. The field value can be any kind of value, including record. Records can be constructed using initialization syntax, as follows:

_record-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`  _field-list<sub>opt</sub>_  `]`<br/> _field-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field_  `,`  _field-list<br/> 
field:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-name_  `=`  _expression<br/> 
field-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quoted-identifier_<br/>

The following example constructs a record with a field named `x` with value `1`, and a field named `y` with value `2`.

```
[ x = 1, y = 2 ]
```

The following example constructs a record with `a` field named a with a nested record value. The nested record has a field named `b` with value `2`.

```
[ a = [ b = 2 ] ]
```

The following holds when evaluating a record expression:

* The expression assigned to each field name is used to determine the value of the associated field.

* If the expression assigned to a field name produces a value when evaluated, then that becomes the value of the field of the resulting record.

* If the expression assigned to a field name raises an error when evaluated, then the fact that an error was raised is recorded with the field along with the error value that was raised. Subsequent access to that field will cause an error to be re-raised with the recorded error value.

* The expression is evaluated in an environment like the parent environment only with variables merged in that correspond to the value of every field of the record, except the one being initialized.

* A value in a record is not evaluated until the corresponding field is accessed.

* A value in a record is evaluated at most once.

* The result of the expression is a record value with an empty metadata record.

* The order of the fields within the record is defined by the order that they appear in the _record-initializer-expression_.

* Every field name that is specified must be unique within the record, or it is an error. Names are compared using an ordinal comparison.

```
    [ x = 1, x = 2 ] // error: field names must be unique 
    [ X = 1, x = 2 ] // OK
```
A record with no fields is called an _empty record_, and is written as follows:

```
[] // empty record
```

Although the order of the fields of a record is not significant when accessing a field or comparing two records, it is significant in other contexts such as when the fields of a record are enumerated.

The same two records produce different results when the fields are obtained:

```
Record.FieldNames([ x = 1, y = 2 ]) // [ "x", "y" ] 
Record.FieldNames([ y = 1, x = 2 ]) // [ "y", "x" ]
```

The number of fields in a record can be determined using the `Record.FieldCount` function. For example:

```
Record.FieldCount([ x = 1, y = 2 })  // 2 
Record.FieldCount([])                // 0
```

In addition to using the record initialization syntax `[ ]`, records can be constructed from a list of values, and a list of field names or a record type. For example:

```
Record.FromList({1, 2}, {"a", "b"})
```

The above is equivalent to:

```
[ a = 1, b = 2 ]
```

The following operators are defined for record values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x & y` | Merge |
| `x ?? y` | Coalesce |
| | |

The following examples illustrate the above operators. Note that record merge uses the fields from the right operand to override fields from the left operand, should there be an overlap in field names.

```
[ a = 1, b = 2 ] & [ c = 3 ]    // [ a = 1, b = 2, c = 3 ] 
[ a = 1, b = 2 ] & [ a = 3 ]    // [ a = 3, b = 2 ] 
[ a = 1, b = 2 ] = [ b = 2, a = 1 ]         // true 
[ a = 1, b = 2, c = 3 ] <> [ a = 1, b = 2 ] // true
```

The native type of record values is the intrinsic type `record`, which specifies an open empty list of fields.

## Table

A _table value_ is an ordered sequence of rows. A _row_ is an ordered sequence of value. The table's type determines the length of all rows in the table, the names of the table's columns, the types of the table's columns, and the structure of the table's keys (if any).

There is no literal syntax for tables. Several standard library functions are provided to construct binary values. For example, `#table` can be used to construct a table from a list of row lists and a list of header names:

```
#table({"x", "x^2"}, {{1,1}, {2,4}, {3,9}})
```

The above example constructs a table with two columns, both of which are of `type any`.

`#table` can also be used to specify a full table type:

```
#table(
    type table [Digit = number, Name = text],  
    {{1,"one"}, {2,"two"}, {3,"three"}} 
    )
```

Here the new table value has a table type that specifies column names and column types.

The following operators are defined for table values:

| Operator | Result |
| -------- | ------ |
| `x = y` | Equal |
| `x <> y` | Not equal |
| `x & y` | Concatenation |
| `x ?? y` | Coalesce |
| | |

Table concatenation aligns like-named columns and fills in `null` for columns appearing in only one of the operand tables. The following example illustrates table concatenation:

```
  #table({"A","B"}, {{1,2}}) 
& #table({"B","C"}, {{3,4}})
```

| A | B | C |
| --- | --- | ---|
| `1` | `2` | `null` |
| `null` | `3` | `4` |
| | |

The native type of table values is a custom table type (derived from the intrinsic type `table`) that lists the column names, specifies all column types to be any, and has no keys. (See [Table types](m-spec-types.md#table-types) for details on table types.)

## Function

A _function value_ is a value that maps a set of arguments to a single value. The details of _function_ values are described in [Functions](m-spec-functions.md).

## Type
A _type value_ is a value that classifies other values. The details of _type_ values are described in [Types](m-spec-types.md).
