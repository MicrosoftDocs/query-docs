---
title: "Standard date and time format strings"
description: Learn how to use a standard date and time format string to define the text representation of a date and time value in Power Query M.
author: DougKlopfenstein
ms-author: dougklo
ms.date: 10/11/2024
ms.topic: reference
ms.subservice: m-background
---
# Standard date and time format strings

A standard date and time format string uses a single character as the format specifier to define the text representation of a time and date value. Any date and time format string that contains more than one character, including white space, is interpreted as a [custom date and time format string](custom-date-and-time-format-strings.md). A standard or custom format string can be used to define the text representation that results from a formatting operation.

## Table of format specifiers

<a name="table"></a> The following table describes the standard date and time format specifiers.

|Format specifier|Description|Examples|
|----------------------|-----------------|--------------|
|"d"|Short date pattern.<br /><br /> More information: [The short date ("d") format specifier](#ShortDate).|2009-06-15T13:45:30 -> 6/15/2009 (en-US)<br /><br /> 2009-06-15T13:45:30 -> 15/06/2009 (fr-FR)<br /><br /> 2009-06-15T13:45:30 -> 2009/06/15 (ja-JP)|
|"D"|Long date pattern.<br /><br /> More information: [The long date ("D") format specifier](#LongDate).|2009-06-15T13:45:30 -> Monday, June 15, 2009 (en-US)<br /><br /> 2009-06-15T13:45:30 -> понедельник, 15 июня 2009 г. (ru-RU)<br /><br /> 2009-06-15T13:45:30 -> Montag, 15. Juni 2009 (de-DE)|
|"f"|Full date/time pattern (short time).<br /><br /> More information: [The full date short time ("f") format specifier](#FullDateShortTime).|2009-06-15T13:45:30 -> Monday, June 15, 2009 1:45 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> den 15 juni 2009 13:45 (sv-SE)<br /><br /> 2009-06-15T13:45:30 -> Δευτέρα, 15 Ιουνίου 2009 1:45 μμ (el-GR)|
|"F"|Full date/time pattern (long time).<br /><br /> More information: [The full date long time ("F") format specifier](#FullDateLongTime).|2009-06-15T13:45:30 -> Monday, June 15, 2009 1:45:30 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> den 15 juni 2009 13:45:30 (sv-SE)<br /><br /> 2009-06-15T13:45:30 -> Δευτέρα, 15 Ιουνίου 2009 1:45:30 μμ (el-GR)|
|"g"|General date/time pattern (short time).<br /><br /> More information: [The general date short time ("g") format specifier](#GeneralDateShortTime).|2009-06-15T13:45:30 -> 6/15/2009 1:45 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> 15/06/2009 13:45 (es-ES)<br /><br /> 2009-06-15T13:45:30 -> 2009/6/15 13:45 (zh-CN)|
|"G"|General date/time pattern (long time).<br /><br /> More information: [The general date long time ("G") format specifier](#GeneralDateLongTime).|2009-06-15T13:45:30 -> 6/15/2009 1:45:30 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> 15/06/2009 13:45:30 (es-ES)<br /><br /> 2009-06-15T13:45:30 -> 2009/6/15 13:45:30 (zh-CN)|
|"M", "m"|Month/day pattern.<br /><br /> More information: [The month ("M", "m") format specifier](#MonthDay).|2009-06-15T13:45:30 -> June 15 (en-US)<br /><br /> 2009-06-15T13:45:30 -> 15. juni (da-DK)<br /><br /> 2009-06-15T13:45:30 -> 15 Juni (id-ID)|
|"O", "o"|round-trip date/time pattern.<br /><br /> More information: [The round-trip ("O", "o") format specifier](#Roundtrip).|2009-06-15T13:45:30 (Local) --> 2009-06-15T13:45:30.0000000-07:00<br /><br /> 2009-06-15T13:45:30 (Utc) --> 2009-06-15T13:45:30.0000000+00:00<br /><br /> 2009-06-15T13:45:30 (Unspecified) --> 2009-06-15T13:45:30.0000000|
|"R", "r"|RFC1123 pattern.<br /><br /> More information: [The RFC1123 ("R", "r") format specifier](#RFC1123).|2009-06-15T13:45:30 -> Mon, 15 Jun 2009 13:45:30 GMT |
|"s"|Sortable date/time pattern.<br /><br /> More information: [The sortable ("s") format specifier](#Sortable).|2009-06-15T13:45:30 (Local) -> 2009-06-15T13:45:30<br /><br /> 2009-06-15T13:45:30 (Utc) -> 2009-06-15T13:45:30|
|"t"|Short time pattern.<br /><br /> More information: [The short time ("t") format specifier](#ShortTime).|2009-06-15T13:45:30 -> 1:45 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> 13:45 (hr-HR)<br /><br /> 2009-06-15T13:45:30 -> 01:45 م (ar-EG)|
|"T"|Long time pattern.<br /><br /> More information: [The long time ("T") format specifier](#LongTime).|2009-06-15T13:45:30 -> 1:45:30 PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> 13:45:30 (hr-HR)<br /><br /> 2009-06-15T13:45:30 -> 01:45:30 م (ar-EG)|
|"u"|Universal sortable date/time pattern.<br /><br /> More information: [The universal sortable ("u") format specifier](#UniversalSortable).|2009-06-15T13:45:30 -> 2009-06-15 13:45:30Z|
|"Y", "y"|Year month pattern.<br /><br /> More information: [The year month ("Y") format specifier](#YearMonth).|2009-06-15T13:45:30 -> June 2009 (en-US)<br /><br /> 2009-06-15T13:45:30 -> juni 2009 (da-DK)<br /><br /> 2009-06-15T13:45:30 -> Juni 2009 (id-ID)|
|Any other single character|Unknown specifier.|Throws a run-time expression error.|

## How standard format strings work

In a formatting operation, a standard format string is simply an alias for a custom format string. The advantage of using an alias to refer to a custom format string is that, although the alias remains invariant, the custom format string itself can vary. This is important because the string representations of date and time values typically vary by culture. For example, the "d" standard format string indicates that a date and time value is to be displayed using a short date pattern. For the invariant culture, this pattern is "MM/dd/yyyy". For the fr-FR culture, it is "dd/MM/yyyy". For the ja-JP culture, it is "yyyy/MM/dd".

If a standard format string in a formatting operation maps to a particular culture's custom format string, your application can define the specific culture whose custom format strings are used in one of these ways:

- You can use the default (or current) culture. The following example displays a date using the current culture's short date format. In this case, the current culture is en-US.

  ```powerquery -m
  let
      Source =
      {
          Date.ToText(#date(2024, 3, 15), [Format = "d"])
          //Displays 3/15/2024
      }
  in
      Source
  ```

- You can pass a culture used to format the date according to the rules of that specific culture. The following example displays a date using the short date format of the pt-BR culture.

  ```powerquery-m
  let
      Source =
      {
          Date.ToText(#date(2024, 3, 15), [Format = "d", Culture = "pt-BR"])
          //Displays 15/03/2024
     }
  in
      Source
  ```

In some cases, the standard format string serves as a convenient abbreviation for a longer custom format string that is invariant. Four standard format strings fall into this category: "O" (or "o"), "R" (or "r"), "s", and "u". These strings correspond to custom format strings defined by the invariant culture. They produce string representations of date and time values that are intended to be identical across cultures. The following table provides information on these four standard date and time format strings.

|Standard format string|Defined by|Custom format string|
|----------------------|----------|--------------------|
|"O" or "o"|None|yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fffffffK|
|"R" or "r"|IETF RFC 1123 specification|ddd, dd MMM yyyy HH':'mm':'ss 'GMT'|
|"s"|ISO 8601|yyyy'-'MM'-'dd'T'HH':'mm':'ss|
|"u"|Sortable because it uses leading zeros for year, month, day, hour, minute, and second|yyyy'-'MM'-'dd HH':'mm':'ss'Z'|

Standard format strings can also be used in parsing operations, which require an input string to exactly conform to a particular pattern for the parse operation to succeed. Many standard format strings map to multiple custom format strings, so a date and time value can be represented in a variety of formats and the parse operation still succeeds.

The following sections describe the standard format specifiers for [Date](date-functions.md), [DateTime](datetime-functions.md), [DateTimeZone](datetimezone-functions.md), and [Time](time-functions.md) values.

## Date formats

This group includes the following formats:

- [The short date ("d") format specifier](#the-short-date-d-format-specifier)
- [The long date ("D") format specifier](#the-long-date-d-format-specifier)

<a name="ShortDate"></a>

### The short date ("d") format specifier

The "d" standard format specifier represents a custom date format defined by a specific culture. For example, the custom format text returned by the invariant culture is "MM/dd/yyyy".

The following example uses the "d" format specifier to display a date value.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(2024, 4, 10), [Format = "d", Culture = ""]),
        // Displays 04/10/2024

        Date.ToText(#date(2024, 4, 10), [Format = "d", Culture = "en-US"]),
        // Displays 4/10/2024

        Date.ToText(#date(2024, 4, 10), [Format = "d", Culture = "en-NZ"]),
        // Displays 10/4/2024

        Date.ToText(#date(2024, 4, 10), [Format = "d", Culture = "de-DE"])
        // Displays 10.4.2024
    }
in
    Source
```

[Back to table](#table)

<a name="LongDate"></a>

### The long date ("D") format specifier

The "D" standard format specifier represents a custom date format defined by a specific culture. For example, the custom format string for the invariant culture is "dddd, dd MMMM yyyy".

The following example uses the "D" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(2024, 4, 10), [Format = "D", Culture = ""]),
        // Displays Wednesday, 10 April, 2024

        Date.ToText(#date(2024, 4, 10), [Format = "D", Culture = "en-US"]),
        // Displays Wednesday, April 10, 2024

        Date.ToText(#date(2024, 4, 10), [Format = "D", Culture = "pt-BR"]),
        // Displays quarta-feira, 10 de abril de 2024

        Date.ToText(#date(2024, 4, 10), [Format = "D", Culture = "es-MX"])
        // Displays miércoles, 10 de abril de 2024
    }
in
    Source
```

[Back to table](#table)

## Date and time formats

This group includes the following formats:

- [The full date short time ("f") format specifier](#the-full-date-short-time-f-format-specifier)
- [The full date long time ("F") format specifier](#the-full-date-long-time-f-format-specifier)
- [The general date short time ("g") format specifier](#the-general-date-short-time-g-format-specifier)
- [The general date long time ("G") format specifier](#the-general-date-long-time-g-format-specifier)
- [The round-trip ("O", "o") format specifier](#the-round-trip-o-o-format-specifier)
- [The RFC1123 ("R", "r") format specifier](#the-rfc1123-r-r-format-specifier)
- [The sortable ("s") format specifier](#the-sortable-s-format-specifier)
- [The universal sortable ("u") format specifier](#the-universal-sortable-u-format-specifier)

<a name="FullDateShortTime"></a>

### The full date short time ("f") format specifier

The "f" standard format specifier represents a combination of the long date ("D") and short time ("t") patterns, separated by a space.

The result string is affected by the formatting information of a specific culture.

The following example uses the "f" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "f", Culture = "en-US"]),
        // Displays Wednesday, April 10, 2024 6:30 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "f", Culture = "fr-FR"])
        // Displays mercredi 10 avril 2024 06:30
    }
in
    Source
```

[Back to table](#table)

<a name="FullDateLongTime"></a>

### The full date long time ("F") format specifier

The "F" standard format specifier represents a custom date and time format defined by a specific culture. For example, the custom format string for the invariant culture is "dddd, dd MMMM yyyy HH:mm:ss".

The result string is affected by the formatting information of a specific culture.

The following example uses the "F" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "F", Culture = ""]),
        // Displays Wednesday, 10 April, 2024 06:30:00

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "F", Culture = "en-US"]),
        // Displays Wednesday, April 10, 2024 6:30:00 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "F", Culture = "fr-FR"])
        // Displays mercredi 10 avril 2024 06:30:00
    }
in
    Source
```

[Back to table](#table)

<a name="GeneralDateShortTime"></a>

### The general date short time ("g") format specifier

The "g" standard format specifier represents a combination of the short date ("d") and short time ("t") patterns, separated by a space. The resulting text is affected by the formatting information of a specific culture.

The result string is affected by the formatting information of a specific culture.

The following example uses the "g" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "g", Culture = ""]),
        // Displays 04/10/2024 06:30

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "g", Culture = "en-US"]),
        // Displays 4/10/2024 6:30 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "g", Culture = "fr-BE"])
        // Displays 10-04-24 06:30
    }
in
    Source
```

[Back to table](#table)

<a name="GeneralDateLongTime"></a>

### The general date long time ("G") format specifier

The "G" standard format specifier represents a combination of the short date ("d") and long time ("T") patterns, separated by a space. The resulting text is affected by the formatting information of a specific culture.

The result string is affected by the formatting information of a specific culture.

The following example uses the "G" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "G", Culture = ""]),
        // Displays 04/10/2024 06:30:00

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "G", Culture = "en-US"]),
        // Displays 4/10/2024 6:30:00 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "G", Culture = "nl-BE"])
        // Displays 10/04/2024 6:30:00
    }
in
    Source
```

[Back to table](#table)

<a name="Roundtrip"></a>

### The round-trip ("O", "o") format specifier

The "O" or "o" standard format specifier represents a custom date and time format string using a pattern that preserves time zone information and emits a result string that complies with ISO 8601. For **DateTimeZone** values, this format specifier is designed to preserve date, time, and timezone values in text.

The "O" or "o" standard format specifier corresponds to the "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fffffffxxx" custom format string for **DateTimeZone** values. In this text, the pairs of single quotation marks that delimit individual characters, such as the hyphens, the colons, and the letter "T", indicate that the individual character is a literal that can't be changed. The apostrophes don't appear in the output string.

The "O" or "o" standard format specifier (and the "yyyy'-'MM'-'dd'T'HH':'mm':'ss'.'fffffffxxx"  custom format) takes advantage of the ways that ISO 8601 represents time zone information to preserve the **DateTimeZone** values:

- The time zone component of [DateTimeZone.ToLocal](datetimezone-tolocal.md) date and time values is an offset from UTC (for example, +01:00, -07:00).

- The time zone component of [DateTimeZone.ToUtc](datetimezone-toutc.md) date and time values uses +00.00 to represent UTC.

Because the "O" or "o" standard format specifier conforms to an international standard, the formatting or parsing operation that uses the specifier always uses the invariant culture and the Gregorian calendar.

The following example uses the "o" format specifier to display a series of **DateTimeZone** values on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    date1 = #datetimezone(2024, 6, 15, 13, 45, 30, 0, 0),
    Source =
    {
        Text.Format("#{0} (Unspecified) --> #{1}", {date1, DateTimeZone.ToText(date1, [Format = "O"])}),
        Text.Format("#{0} (Utc) --> #{1}", {date1, DateTimeZone.ToText(DateTimeZone.ToUtc(date1), [Format = "O"])}),
        Text.Format("#{0} (Local) --> #{1}", {date1, DateTimeZone.ToText(DateTimeZone.ToLocal(date1), [Format = "O"])})
    }
in
    Source

// The example displays the following output:
//    6/15/2024 1:45:30 PM +00:00 (Unspecified) --> 2024-06-15T13:45:30.0000000+00:00
//    6/15/2024 1:45:30 PM +00:00 (Utc) --> 2024-06-15T13:45:30.0000000+00:00
//    6/15/2024 1:45:30 PM +00:00 (Local) --> 2024-06-15T08:45:30.0000000-07:00

```

> [!NOTE]
>The value returned by [DateTimeZone.ToLocal](datetimezone-tolocal.md) depends on whether you're running Power Query on a local machine or online. For example, in the sample above on a system in the U.S. Pacific Time zone, Power Query Desktop returns `-07:00` for the **Local** time because it's reading the time set on your local machine. However, Power Query Online returns `+00:00` because it's reading the time set on the cloud virtual machines, which are set to UTC.

The following example uses the "o" format specifier to create a formatted string, and then restores the original date and time value by calling a date and time parsing routine.

```powerquery-m
let
    // Round-trip a local time
    #"Origin Local Date" = DateTimeZone.ToLocal(
        #datetimezone(2024, 4, 10, 6, 30, 0, 0, 0)
    ),
    #"Local Date Text" = DateTimeZone.ToText(
        #"Origin Local Date", [Format = "o"]
    ),
    #"New Local Date" = DateTimeZone.FromText(#"Local Date Text"),
    #"Local Round Trip" = Text.Format(
        "Round-tripped #{0} Local to #{1} Local.", 
        {
            DateTimeZone.ToText(#"Origin Local Date"), 
            DateTimeZone.ToText(#"New Local Date")
        }
    ),

    // Round-trip a UTC time
    #"Origin UTC Date" = DateTimeZone.ToUtc(
        #datetimezone(2024, 4, 12, 9, 30, 0, 0, 0)
    ),
    #"UTC Date Text" = DateTimeZone.ToText(
        #"Origin UTC Date", [Format = "o"]
    ),
    #"New UTC Date" = DateTimeZone.FromText(#"UTC Date Text"),
    #"UTC Round Trip" = Text.Format(
        "Round-tripped #{0} UTC to #{1} UTC.", 
        {
            DateTimeZone.ToText(#"Origin UTC Date"), 
            DateTimeZone.ToText(#"New UTC Date")
        }
    ),

    // Round-trip an 18 hour offset time
    #"Origin Offset Date" = DateTimeZone.ToLocal(
        #datetimezone(2024, 4, 10, 6, 30, 0, 0, 0) + #duration(0, 18, 0, 0)
    ),
    #"Offset Date Text" = DateTimeZone.ToText(
        #"Origin Offset Date", [Format = "o"]
    ),
    #"New Offset Date" = DateTimeZone.FromText(#"Offset Date Text"),
    #"Offset Round Trip" = Text.Format(
        "Round-tripped #{0} to #{1}.", 
        {
            DateTimeZone.ToText(#"Origin Offset Date"), 
            DateTimeZone.ToText(#"New Offset Date")
        }
    ),

    #"Round Trip Results" = 
        {#"Local Round Trip", #"UTC Round Trip", #"Offset Round Trip"}
in
    #"Round Trip Results"

// The example displays the following output in Power Query Desktop:
//    Round-tripped 4/9/2024 11:30:00 PM -07:00 Local to 4/9/2024 11:30:00 PM -07:00 Local.
//    Round-tripped 4/12/2024 9:30:00 AM +00:00 UTC to 4/12/2024 9:30:00 AM +00:00 UTC.
//    Round-tripped 4/10/2024 5:30:00 PM -07:00 to 4/10/2024 5:30:00 PM -07:00.

// The example displays the following output in Power Query Online:
//    Round-tripped 4/10/2024 6:30:00 AM +00:00 Local to 4/10/2024 6:30:00 AM +00:00 Local.
//    Round-tripped 4/12/2024 9:30:00 AM +00:00 UTC to 4/12/2024 9:30:00 AM +00:00 UTC.
//    Round-tripped 4/11/2024 12:30:00 AM +00:00 to 4/11/2024 12:30:00 AM +00:00.
```

[Back to table](#table)

<a name="RFC1123"></a>

### The RFC1123 ("R", "r") format specifier

The "R" or "r" standard format specifier represents a custom date and time format string that's not defined by a specific culture. It is always the same, regardless of the culture used or the format provider supplied. The custom format string is "ddd, dd MMM yyyy HH':'mm':'ss 'GMT'". When this standard format specifier is used, the formatting or parsing operation always uses the invariant culture.

Although the RFC 1123 standard expresses a time as Coordinated Universal Time (UTC), the formatting operation doesn't modify the value of the date and time that's being formatted. Therefore, you must convert the DateTime value to UTC by calling the [DateTimeZone.ToUtc](datetimezone-toutc.md) function method before you perform the formatting operation.

The following example uses the "r" format specifier to display a time and date value on a system in the U.S. Pacific Time zone (seven hours behind UTC).

```powerquery-m
let
    date1 = #datetimezone(2024, 4, 10, 6, 30, 0, -7, 0),
    dateOffset = DateTimeZone.ToUtc(date1),
    Source = 
    {
        DateTimeZone.ToText(date1, [Format = "r"]),
        // Displays Wed, 10 Apr 2024 13:30:00 GMT

        DateTimeZone.ToText(dateOffset, [Format = "r"])
        // Displays Wed, 10 Apr 2024 13:30:00 GMT
    }
in
    Source
```

[Back to table](#table)

<a name="Sortable"></a>

### The sortable ("s") format specifier

The "s" standard format specifier represents a custom date and time format string that reflects a defined standard (ISO 8601), and is read-only. Therefore, it is always the same, regardless of the culture used or the format provider supplied. The custom format string is "yyyy'-'MM'-'dd'T'HH':'mm':'ss". The purpose of the "s" format specifier is to produce result strings that sort consistently in ascending or descending order based on date and time values.

When this standard format specifier is used, the formatting or parsing operation always uses the invariant culture.

The following example uses the "s" format specifier to display a date and time value on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "s", Culture = "en-US"])
        // Displays 2024-04-10T06:30:00
    }
in
    Source
```

[Back to table](#table)

<a name="UniversalSortable"></a>

### The universal sortable ("u") format specifier

The "u" standard format specifier represents a custom date and time format string that is always the same, regardless of the culture used or the format provider supplied. The custom format string is "yyyy'-'MM'-'dd HH':'mm':'ss'Z'".  The pattern reflects a defined standard, and the property is read-only. When this standard format specifier is used, the formatting or parsing operation always uses the invariant culture.

Although the result string should express a time as Coordinated Universal Time (UTC), no conversion of the original **DateTimeZone** value is performed during the formatting operation. Therefore, you must convert a **DateTimeZone** value to UTC by calling the [DateTimeZone.ToUtc](datetimezone-toutc.md) function before formatting it.

The following example uses the "u" format specifier to display a date and time value.

```powerquery-m
let
    date1 = #datetimezone(2024, 4, 10, 6, 30, 0, -7, 0),
    dateOffset = DateTimeZone.ToUtc(date1),
    Source =
    {
        DateTimeZone.ToText(dateOffset, [Format = "u"]),
        // Displays 2024-04-10 13:30:00Z
    }
in
    Source
```

[Back to table](#table)

## Time formats

This group includes the following formats:

- [The short time ("t") format specifier](#the-short-time-t-format-specifier)
- [The long time ("T") format specifier](#the-long-time-t-format-specifier)

<a name="ShortTime"></a>

### The short time ("t") format specifier

The "t" standard format specifier represents a custom date and time format string that is defined by the specified culture. For example, the custom format string for the invariant culture is "HH:mm".

The result string is affected by the formatting information of a specific culture.

The following example uses the "t" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "t", Culture = ""]),
        // Displays 06:30
        
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "t", Culture = "en-US"]),
        // Displays 6:30 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "t", Culture = "es-ES"])
        // Displays 6:30
    }
in
    Source
```

[Back to table](#table)

<a name="LongTime"></a>

### The long time ("T") format specifier

The "T" standard format specifier represents a custom date and time format string that is defined by the specific culture. For example, the custom format string for the invariant culture is "HH:mm:ss".

The following example uses the "T" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "T", Culture = ""]),
        // Displays 06:30:00
        
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "T", Culture = "en-US"]),
        // Displays 6:30:00 AM

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "T", Culture = "es-ES"])
        // Displays 6:30:00
    }
in
    Source
```
[Back to table](#table)

## Partial date formats

This group includes the following formats:

- [The month ("M", "m") format specifier](#the-month-m-m-format-specifier)
- [The year month ("Y", "y") format specifier](#the-year-month-y-y-format-specifier)

<a name="MonthDay"></a>

### The month ("M", "m") format specifier

The "M" or "m" standard format specifier represents a custom date and time format string that is defined by the specific culture. For example, the custom format string for the invariant culture is "MMMM dd".

The following example uses the "m" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "m", Culture = ""]),
        // Displays April 10
        
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "m", Culture = "en-US"]),
        // Displays April 10

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "m", Culture = "ms-MY"])
        // Displays 10 April
    }
in
    Source
```

[Back to table](#table)

<a name="YearMonth"></a>

### The year month ("Y", "y") format specifier

The "Y" or "y" standard format specifier represents a custom date format string that is defined by a specific culture. For example, the custom format string for the invariant culture is "yyyy MMMM".

The following example uses the "y" format specifier to display a date and time value.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "Y", Culture = ""]),
        // Displays 2024 April
        
        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "Y", Culture = "en-US"]),
        // Displays April 2024

        DateTime.ToText(#datetime(2024, 4, 10, 6, 30, 0), [Format = "y", Culture = "af-ZA"])
        // Displays April 2024
    }
in
    Source
```

[Back to table](#table)

## Related content

- [How culture affects text formatting](how-culture-affects-text-formatting.md)
- [Date, Time, DateTime, and DateTimeZone type conversion](type-conversion.md#date-time-datetime-and-datetimezone)
- [Date functions](date-functions.md)
- [DateTime functions](datetime-functions.md)
- [DateTimeZone functions](datetimezone-functions.md)
- [Time functions](time-functions.md)
- [Custom Date and Time Format Strings](custom-date-and-time-format-strings.md)
