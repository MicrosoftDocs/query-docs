---
title: "Custom date and time format strings"
description: Learn to use custom date and time format strings to convert date and time values into text representations, or to parse strings for dates and times.
author: DougKlopfenstein
ms.author: dougklo
ms.date: 10/7/2024
ms.topic: reference
---

# Custom date and time format strings

A date and time format string defines the text representation of a [Date](date-functions.md), [DateTime](datetime-functions.md), [DateTimeZone](datetimezone-functions.md), or [Time](time-functions.md) value that results from a formatting operation. It can also define the representation of a date and time value that is required in a parsing operation in order to successfully convert the string to a date and time. A custom format string consists of one or more custom date and time format specifiers. Any string that isn't a [standard date and time format string](standard-date-and-time-format-strings.md) is interpreted as a custom date and time format string.

In formatting operations, custom date and time format strings can be used with the `ToText` method of a date and time and timezone instance. The following example illustrates its uses.

```powerquery-m
let
    Source = 
    {
        Text.From("Today is " & Date.ToText(#date(2011, 6, 10), [Format = "MMMM dd yyyy"]) & "."),
        Text.Format("The current date and time: #{0}", {DateTimeZone.ToText(
            #datetimezone(2011, 6, 10, 15, 24, 16, 0, 0), [Format = "MM/dd/yy H:mm:ss zzz"])}
        )
    }
in
    Source

// The example displays the following output:
//    Today is June 10, 2011.
//    The current date and time: 06/10/11 15:24:16 +00:00
```

In parsing operations, custom date and time format strings can be used with the **Date**, **DateTime**, **Time**, and **DateTimeZone** functions. These functions require that an input string conforms exactly to a particular pattern for the parse operation to succeed. The following example illustrates a call to the [DateTime.FromText](datetime-fromtext.md) function to parse a date that must include a month, a day, and a two-digit year.

```powerquery-m
let
    dateValues = { "30-12-2011", "12-30-2011", "30-12-11", "12-30-11"},
    pattern = "MM-dd-yy",
    convertedDates = List.Transform(dateValues, (dateValue) => 
        try Text.Format("Converted '#{0}' to #{1}.", {dateValue, DateTime.FromText(dateValue, [Format=pattern])}) 
        otherwise Text.Format("Unable to convert '#{0}' to a date and time.", {dateValue}))
in
    convertedDates

// The example displays the following output:
//    Unable to convert '30-12-2011' to a date and time.
//    Unable to convert '12-30-2011' to a date and time.
//    Unable to convert '30-12-11' to a date and time.
//    Converted '12-30-11' to 12/30/2011.
```

<a name="table"></a> The following table describes the custom date and time format specifiers and displays a result string produced by each format specifier. By default, result strings reflect the formatting conventions of the en-US culture. If a particular format specifier produces a localized result string, the example also notes the culture to which the result string applies. For more information about using custom date and time format strings, go to the [Notes](#notes) section.

| Format specifier | Description | Examples |
|--|--|--|
| "d" | The day of the month, from 1 to 31.<br /><br /> More information: [The "d" custom format specifier](#dSpecifier). | 2009-06-01T13:45:30 -> 1<br /><br /> 2009-06-15T13:45:30 -> 15 |
| "dd" | The day of the month, from 01 to 31.<br /><br /> More information: [The "dd" custom format specifier](#ddSpecifier). | 2009-06-01T13:45:30 -> 01<br /><br /> 2009-06-15T13:45:30 -> 15 |
| "ddd" | The abbreviated name of the day of the week.<br /><br /> More information: [The "ddd" custom format specifier](#dddSpecifier). | 2009-06-15T13:45:30 -> Mon (en-US)<br /><br /> 2009-06-15T13:45:30 -> Пн (ru-RU)<br /><br /> 2009-06-15T13:45:30 -> lun. (fr-FR) |
| "dddd" | The full name of the day of the week.<br /><br /> More information: [The "dddd" custom format specifier](#ddddSpecifier). | 2009-06-15T13:45:30 -> Monday (en-US)<br /><br /> 2009-06-15T13:45:30 -> понедельник (ru-RU)<br /><br /> 2009-06-15T13:45:30 -> lundi (fr-FR) |
| "f" | The tenths of a second in a date and time value.<br /><br /> More information: [The "f" custom format specifier](#fSpecifier). | 2009-06-15T13:45:30.6170000 -> 6<br /><br /> 2009-06-15T13:45:30.05 -> 0 |
| "ff" | The hundredths of a second in a date and time value.<br /><br /> More information: [The "ff" custom format specifier](#ffSpecifier). | 2009-06-15T13:45:30.6170000 -> 61<br /><br /> 2009-06-15T13:45:30.0050000 -> 00 |
| "fff" | The milliseconds in a date and time value.<br /><br /> More information: [The "fff" custom format specifier](#fffSpecifier). | 6/15/2009 13:45:30.617 -> 617<br /><br /> 6/15/2009 13:45:30.0005 -> 000 |
| "ffff" | The ten thousandths of a second in a date and time value.<br /><br /> More information: [The "ffff" custom format specifier](#ffffSpecifier). | 2009-06-15T13:45:30.6175000 -> 6175<br /><br /> 2009-06-15T13:45:30.0000500  -> 0000 |
| "fffff" | The hundred thousandths of a second in a date and time value.<br /><br /> More information: [The "fffff" custom format specifier](#fffffSpecifier). | 2009-06-15T13:45:30.6175400 -> 61754<br /><br /> 6/15/2009 13:45:30.000005 -> 00000 |
| "ffffff" | The millionths of a second in a date and time value.<br /><br /> More information: [The "ffffff" custom format specifier](#ffffffSpecifier). | 2009-06-15T13:45:30.6175420 -> 617542<br /><br /> 2009-06-15T13:45:30.0000005 -> 000000 |
| "fffffff" | The ten millionths of a second in a date and time value.<br /><br /> More information: [The "fffffff" custom format specifier](#fffffffSpecifier). | 2009-06-15T13:45:30.6175425 -> 6175425<br /><br /> 2009-06-15T13:45:30.0001150 -> 0001150 |
| "F" | If non-zero, the tenths of a second in a date and time value.<br /><br /> More information: [The "F" custom format specifier](#F_Specifier). | 2009-06-15T13:45:30.6170000 -> 6<br /><br /> 2009-06-15T13:45:30.0500000 -> (no output) |
| "FF" | If non-zero, the hundredths of a second in a date and time value.<br /><br /> More information: [The "FF" custom format specifier](#FF_Specifier). | 2009-06-15T13:45:30.6170000 -> 61<br /><br /> 2009-06-15T13:45:30.0050000 -> (no output) |
| "FFF" | If non-zero, the milliseconds in a date and time value.<br /><br /> More information: [The "FFF" custom format specifier](#FFF_Specifier). | 2009-06-15T13:45:30.6170000 -> 617<br /><br /> 2009-06-15T13:45:30.0005000 -> (no output) |
| "FFFF" | If non-zero, the ten thousandths of a second in a date and time value.<br /><br /> More information: [The "FFFF" custom format specifier](#FFFF_Specifier). | 2009-06-15T13:45:30.5275000 -> 5275<br /><br /> 2009-06-15T13:45:30.0000500 -> (no output) |
| "FFFFF" | If non-zero, the hundred thousandths of a second in a date and time value.<br /><br /> More information: [The "FFFFF" custom format specifier](#FFFFF_Specifier). | 2009-06-15T13:45:30.6175400 -> 61754<br /><br /> 2009-06-15T13:45:30.0000050 -> (no output) |
| "FFFFFF" | If non-zero, the millionths of a second in a date and time value.<br /><br /> More information: [The "FFFFFF" custom format specifier](#FFFFFF_Specifier). | 2009-06-15T13:45:30.6175420 -> 617542<br /><br /> 2009-06-15T13:45:30.0000005 -> (no output) |
| "FFFFFFF" | If non-zero, the ten millionths of a second in a date and time value.<br /><br /> More information: [The "FFFFFFF" custom format specifier](#FFFFFFF_Specifier). | 2009-06-15T13:45:30.6175425 -> 6175425<br /><br /> 2009-06-15T13:45:30.0001150 -> 000115 |
| "g", "gg" | The period or era.<br /><br /> More information: [The "g" or "gg" custom format specifier](#gSpecifier). | 2009-06-15T13:45:30.6170000 -> A.D. |
| "h" | The hour, using a 12-hour clock from 1 to 12.<br /><br /> More information: [The "h" custom format specifier](#hSpecifier). | 2009-06-15T01:45:30 -> 1<br /><br /> 2009-06-15T13:45:30 -> 1 |
| "hh" | The hour, using a 12-hour clock from 01 to 12.<br /><br /> More information: [The "hh" custom format specifier](#hhSpecifier). | 2009-06-15T01:45:30 -> 01<br /><br /> 2009-06-15T13:45:30 -> 01 |
| "H" | The hour, using a 24-hour clock from 0 to 23.<br /><br /> More information: [The "H" custom format specifier](#H_Specifier). | 2009-06-15T01:45:30 -> 1<br /><br /> 2009-06-15T13:45:30 -> 13 |
| "HH" | The hour, using a 24-hour clock from 00 to 23.<br /><br /> More information: [The "HH" custom format specifier](#HH_Specifier). | 2009-06-15T01:45:30 -> 01<br /><br /> 2009-06-15T13:45:30 -> 13 |
| "K" | Time zone information.<br /><br /> More information: [The "K" custom format specifier](#KSpecifier). | 2009-06-15T13:45:30, Unspecified -><br /><br /> 2009-06-15T13:45:30, Utc -> +00:00<br /><br />2009-06-15T13:45:30, Local -> -07:00 (depends on local or cloud computer settings) |
| "m" | The minute, from 0 to 59.<br /><br /> More information: [The "m" custom format specifier](#mSpecifier). | 2009-06-15T01:09:30 -> 9<br /><br /> 2009-06-15T13:29:30 -> 29 |
| "mm" | The minute, from 00 to 59.<br /><br /> More information: [The "mm" custom format specifier](#mmSpecifier). | 2009-06-15T01:09:30 -> 09<br /><br /> 2009-06-15T01:45:30 -> 45 |
| "M" | The month, from 1 to 12.<br /><br /> More information: [The "M" custom format specifier](#M_Specifier). | 2009-06-15T13:45:30 -> 6 |
| "MM" | The month, from 01 to 12.<br /><br /> More information: [The "MM" custom format specifier](#MM_Specifier). | 2009-06-15T13:45:30 -> 06 |
| "MMM" | The abbreviated name of the month.<br /><br /> More information: [The "MMM" custom format specifier](#MMM_Specifier). | 2009-06-15T13:45:30 -> Jun (en-US)<br /><br /> 2009-06-15T13:45:30 -> juin (fr-FR)<br /><br /> 2009-06-15T13:45:30 -> Jun (zu-ZA) |
| "MMMM" | The full name of the month.<br /><br /> More information: [The "MMMM" custom format specifier](#MMMM_Specifier). | 2009-06-15T13:45:30 -> June (en-US)<br /><br /> 2009-06-15T13:45:30 -> juni (da-DK)<br /><br /> 2009-06-15T13:45:30 -> Juni (zu-ZA) |
| "s" | The second, from 0 to 59.<br /><br /> More information: [The "s" custom format specifier](#sSpecifier). | 2009-06-15T13:45:09 -> 9 |
| "ss" | The second, from 00 to 59.<br /><br /> More information: [The "ss" custom format specifier](#ssSpecifier). | 2009-06-15T13:45:09 -> 09 |
| "t" | The first character of the AM/PM designator.<br /><br /> More information: [The "t" custom format specifier](#tSpecifier). | 2009-06-15T13:45:30 -> P (en-US)<br /><br /> 2009-06-15T13:45:30 -> 午 (ja-JP)<br /><br /> 2009-06-15T13:45:30 ->  (fr-FR) |
| "tt" | The AM/PM designator.<br /><br /> More information: [The "tt" custom format specifier](#ttSpecifier). | 2009-06-15T13:45:30 -> PM (en-US)<br /><br /> 2009-06-15T13:45:30 -> 午後 (ja-JP)<br /><br /> 2009-06-15T13:45:30 ->  (fr-FR) |
| "y" | The year, from 0 to 99.<br /><br /> More information: [The "y" custom format specifier](#ySpecifier). | 0001-01-01T00:00:00 -> 1<br /><br /> 0900-01-01T00:00:00 -> 0<br /><br /> 1900-01-01T00:00:00 -> 0<br /><br /> 2009-06-15T13:45:30 -> 9<br /><br /> 2019-06-15T13:45:30 -> 19 |
| "yy" | The year, from 00 to 99.<br /><br /> More information: [The "yy" custom format specifier](#yySpecifier). | 0001-01-01T00:00:00 -> 01<br /><br /> 0900-01-01T00:00:00 -> 00<br /><br /> 1900-01-01T00:00:00 -> 00<br /><br /> 2019-06-15T13:45:30 -> 19 |
| "yyy" | The year, with a minimum of three digits.<br /><br /> More information: [The "yyy" custom format specifier](#yyySpecifier). | 0001-01-01T00:00:00 -> 001<br /><br /> 0900-01-01T00:00:00 -> 900<br /><br /> 1900-01-01T00:00:00 -> 1900<br /><br /> 2009-06-15T13:45:30 -> 2009 |
| "yyyy" | The year as a four-digit number.<br /><br /> More information: [The "yyyy" custom format specifier](#yyyySpecifier). | 0001-01-01T00:00:00 -> 0001<br /><br /> 0900-01-01T00:00:00 -> 0900<br /><br /> 1900-01-01T00:00:00 -> 1900<br /><br /> 2009-06-15T13:45:30 -> 2009 |
| "yyyyy" | The year as a five-digit number.<br /><br /> More information: [The "yyyyy" custom format specifier](#yyyyySpecifier). | 0001-01-01T00:00:00 -> 00001<br /><br /> 2009-06-15T13:45:30 -> 02009 |
| "z" | Hours offset from UTC, with no leading zeros.<br /><br /> More information: [The "z" custom format specifier](#zSpecifier). | 2009-06-15T13:45:30-07:00 -> -7 |
| "zz" | Hours offset from UTC, with a leading zero for a single-digit value.<br /><br /> More information: [The "zz" custom format specifier](#zzSpecifier). | 2009-06-15T13:45:30-07:00 -> -07 |
| "zzz" | Hours and minutes offset from UTC.<br /><br /> More information: [The "zzz" custom format specifier](#zzzSpecifier). | 2009-06-15T13:45:30-07:00 -> -07:00 |
| ":" | The time separator.<br /><br /> More information: [The ":" custom format specifier](#timeSeparator). | 2009-06-15T13:45:30 -> : (en-US)<br /><br /> 2009-06-15T13:45:30 -> . (it-IT)<br /><br /> 2009-06-15T13:45:30 -> : (ja-JP) |
| "/" | The date separator.<br /><br /> More Information: [The "/" custom format specifier](#dateSeparator). | 2009-06-15T13:45:30 -> / (en-US)<br /><br /> 2009-06-15T13:45:30 -> - (ar-DZ)<br /><br /> 2009-06-15T13:45:30 -> . (tr-TR) |
| "*string*"<br /><br /> '*string*' | Literal string delimiter.<br /><br /> More information: [Character literals](#Literals). | 2009-06-15T13:45:30 (""arr:"" h:m t) -> arr: 1:45 P<br /><br /> 2009-06-15T13:45:30 ('arr:' h:m t) -> arr: 1:45 P |
| % | Defines the following character as a custom format specifier.<br /><br /> More information: [Using single custom format specifiers](#using-single-custom-format-specifiers). | 2009-06-15T13:45:30 (%h) -> 1 |
| &#92;, "", ' | The escape sequences.<br /><br /> More information: [Character literals](#Literals) and [Using the escape sequences](#escape). | 2009-06-15T13:45:30 (h \h) -> 1 h<br /><br />2009-06-15T13:45:30 (h ""h"") -> 1 h<br /><br />2009-06-15T13:45:30 (h 'h') -> 1 h |
| Any other character | The character is copied to the result string unchanged.<br /><br /> More information: [Character literals](#Literals). | 2009-06-15T01:45:30 (arr hh:mm t) -> arr 01:45 A |

The following sections provide additional information about each custom date and time format specifier. Unless otherwise noted, each specifier produces an identical string representation regardless of whether it's used with a **Date**, **DateTime**, **DateTimeZone**, or **Time** value.

## Day "d" format specifier

### <a name="dSpecifier"></a> The "d" custom format specifier

The "d" custom format specifier represents the day of the month as a number from 1 to 31. A single-digit day is formatted without a leading zero.

If the "d" format specifier is used without other custom format specifiers, it's interpreted as the "d" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "d" custom format specifier in several format strings.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "d, M", Culture = ""]),
        // Displays 29, 8 

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "d, MMMM", Culture = "en-US"]),
        // Displays 29, August

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "d, MMMM", Culture = "es-MX"])
        // Displays 29, agosto
    }
in
    Source
```

[Back to table](#table)

### <a name="ddSpecifier"></a> The "dd" custom format specifier

The "dd" custom format string represents the day of the month as a number from 01 to 31. A single-digit day is formatted with a leading zero.

The following example includes the "dd" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 2, 6, 30, 15), [Format = "dd, MM", Culture = ""])
        // Displays 02, 01 
    }
in
    Source
```

[Back to table](#table)

### <a name="dddSpecifier"></a> The "ddd" custom format specifier

The "ddd" custom format specifier represents the abbreviated name of the day of the week. The localized abbreviated name of the day of the week is retrieved from the current or specified culture.

The following example includes the "ddd" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "ddd d MMM", Culture = "en-US"]),
        // Displays Thu 29 Aug

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "ddd d MMM", Culture = "fr-FR"])
        // Displays jeu. 29 août
    }
in
    Source
```

[Back to table](#table)

### <a name="ddddSpecifier"></a> The "dddd" custom format specifier

The "dddd" custom format specifier (plus any number of additional "d" specifiers) represents the full name of the day of the week. The localized name of the day of the week is retrieved from the current or specified culture.

The following example includes the "dddd" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "dddd dd MMMM", Culture = "en-US"]),
        // Displays Thursday 29 August

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "dddd dd MMMM", Culture = "it-IT"])
        // Displays giovedì 29 agosto
    }
in
    Source
```

[Back to table](#table)

## Lowercase seconds "f" fraction specifier

### <a name="fSpecifier"></a> The "f" custom format specifier

The "f" custom format specifier represents the most significant digit of the seconds fraction; that is, it represents the tenths of a second in a date and time value.

If the "f" format specifier is used without other format specifiers, it's interpreted as the "f" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

When you use "f" format specifiers as part of a format string supplied to parse the number of fractional seconds, the number of "f" format specifiers indicates the number of most significant digits of the seconds fraction that must be present to successfully parse the string.

The following example includes the "f" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:f", Culture = ""]),
        // Displays 07:27:15:0

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:F", Culture = ""])
        // Displays 07:27:15:
    }
in
    Source
```

[Back to table](#table)

### <a name="ffSpecifier"></a> The "ff" custom format specifier

The "ff" custom format specifier represents the two most significant digits of the seconds fraction; that is, it represents the hundredths of a second in a date and time value.

following example includes the "ff" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:ff", Culture = ""]),
        // Displays 07:27:15:01

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:FF", Culture = ""])
        // Displays 07:27:15:01
    }
in
    Source
```

[Back to table](#table)

### <a name="fffSpecifier"></a> The "fff" custom format specifier

The "fff" custom format specifier represents the three most significant digits of the seconds fraction; that is, it represents the milliseconds in a date and time value.

The following example includes the "fff" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:fff", Culture = ""]),
        // Displays 07:27:15:018

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:FFF", Culture = ""])
        // Displays 07:27:15:018
    }
in
    Source
```

[Back to table](#table)

### <a name="ffffSpecifier"></a> The "ffff" custom format specifier

The "ffff" custom format specifier represents the four most significant digits of the seconds fraction; that is, it represents the ten thousandths of a second in a date and time value.

Although it's possible to display the ten thousandths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="fffffSpecifier"></a> The "fffff" custom format specifier

The "fffff" custom format specifier represents the five most significant digits of the seconds fraction; that is, it represents the hundred thousandths of a second in a date and time value.

Although it's possible to display the hundred thousandths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="ffffffSpecifier"></a> The "ffffff" custom format specifier

The "ffffff" custom format specifier represents the six most significant digits of the seconds fraction; that is, it represents the millionths of a second in a date and time value.

Although it's possible to display the millionths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="fffffffSpecifier"></a> The "fffffff" custom format specifier

The "fffffff" custom format specifier represents the seven most significant digits of the seconds fraction; that is, it represents the ten millionths of a second in a date and time value.

Although it's possible to display the ten millionths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

## Uppercase seconds "F" fraction specifier

### <a name="F_Specifier"></a> The "F" custom format specifier

The "F" custom format specifier represents the most significant digit of the seconds fraction; that is, it represents the tenths of a second in a date and time value. Nothing is displayed if the digit is zero, and the decimal point that follows the number of seconds is also not displayed.

If the "F" format specifier is used without other format specifiers, it's interpreted as the "F" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The number of "F" format specifiers used when parsing indicates the maximum number of most significant digits of the seconds fraction that can be present to successfully parse the string.

The following example includes the "F" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:f", Culture = ""]),
        // Displays 07:27:15:0

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:F", Culture = ""])
        // Displays 07:27:15:
    }
in
    Source
```

[Back to table](#table)

### <a name="FF_Specifier"></a> The "FF" custom format specifier

The "FF" custom format specifier represents the two most significant digits of the seconds fraction; that is, it represents the hundredths of a second in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the two significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

The following example includes the "FF" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:ff", Culture = ""]),
        // Displays 07:27:15:01

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:FF", Culture = ""])
        // Displays 07:27:15:01
    }
in
    Source
```

[Back to table](#table)

### <a name="FFF_Specifier"></a> The "FFF" custom format specifier

The "FFF" custom format specifier represents the three most significant digits of the seconds fraction; that is, it represents the milliseconds in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the three significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

The following example includes the "FFF" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:fff", Culture = ""]),
        // Displays 07:27:15:018

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15.018), [Format = "hh:mm:ss:FFF", Culture = ""])
        // Displays 07:27:15:018
    }
in
    Source
```

[Back to table](#table)

### <a name="FFFF_Specifier"></a> The "FFFF" custom format specifier

The "FFFF" custom format specifier represents the four most significant digits of the seconds fraction; that is, it represents the ten thousandths of a second in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the four significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

Although it's possible to display the ten thousandths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="FFFFF_Specifier"></a> The "FFFFF" custom format specifier

The "FFFFF" custom format specifier represents the five most significant digits of the seconds fraction; that is, it represents the hundred thousandths of a second in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the five significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

Although it's possible to display the hundred thousandths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="FFFFFF_Specifier"></a> The "FFFFFF" custom format specifier

The "FFFFFF" custom format specifier represents the six most significant digits of the seconds fraction; that is, it represents the millionths of a second in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the six significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

Although it's possible to display the millionths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

### <a name="FFFFFFF_Specifier"></a> The "FFFFFFF" custom format specifier

The "FFFFFFF" custom format specifier represents the seven most significant digits of the seconds fraction; that is, it represents the ten millionths of a second in a date and time value. Trailing zeros aren't displayed. Nothing is displayed if the seven significant digits are zero, and in that case the decimal point that follows the number of seconds is also not displayed.

Although it's possible to display the ten millionths of a second component of a time value, that value might not be meaningful. The precision of date and time values depends on the resolution of the system clock. On the Windows Server 2019 and Windows 11 operating systems, the clock's resolution is approximately 1 millisecond.

[Back to table](#table)

## Era "g" format specifier

### <a name="gSpecifier"></a> The "g" or "gg" custom format specifier

The "g" or "gg" custom format specifiers (plus any number of additional "g" specifiers) represents the period or era, such as A.D. The formatting operation ignores this specifier if the date to be formatted doesn't have an associated period or era string.

If the "g" format specifier is used without other custom format specifiers, it's interpreted as the "g" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "g" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(70, 08, 04), [Format = "MM/dd/yyyy g", Culture = ""]),
        // Displays 08/04/0070 A.D.

        Date.ToText(#date(70, 08, 04), [Format = "MM/dd/yyyy g", Culture = "fr-FR"])
        // Displays 08/04/0070 ap. J.-C.
    }
in
    Source
```

[Back to table](#table)

## Lowercase hour "h" format specifier

### <a name="hSpecifier"></a> The "h" custom format specifier

The "h" custom format specifier represents the hour as a number from 1 to 12; that is, the hour is represented by a 12-hour clock that counts the whole hours since midnight or noon. A particular hour after midnight is indistinguishable from the same hour after noon. The hour isn't rounded, and a single-digit hour is formatted without a leading zero. For example, given a time of 5:43 in the morning or afternoon, this custom format specifier displays "5".

If the "h" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "h" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 6:9:1 P

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = "el-GR"]),
        // Displays 6:9:1 μ

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 9:18:1.5 A

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = "el-GR"])
        // Displays 9:18:1.5 π
    }
in
    Source
```

[Back to table](#table)

### <a name="hhSpecifier"></a> The "hh" custom format specifier

The "hh" custom format specifier (plus any number of additional "h" specifiers) represents the hour as a number from 01 to 12; that is, the hour is represented by a 12-hour clock that counts the whole hours since midnight or noon. A particular hour after midnight is indistinguishable from the same hour after noon. The hour isn't rounded, and a single-digit hour is formatted with a leading zero. For example, given a time of 5:43 in the morning or afternoon, this format specifier displays "05".

The following example includes the "hh" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = ""]),
        // Displays 06:09:01 PM

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = "hu-HU"]),
        // Displays 06:09:01 du.

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = ""]),
        // Displays 09:18:01.50 AM

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = "hu-HU"])
        // Displays 09:18:01.50 de.
    }
in
    Source
```

[Back to table](#table)

## Uppercase hour "H" format specifier

### <a name="H_Specifier"></a> The "H" custom format specifier

The "H" custom format specifier represents the hour as a number from 0 to 23; that is, the hour is represented by a zero-based 24-hour clock that counts the hours since midnight. A single-digit hour is formatted without a leading zero.

If the "H" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "H" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 6, 9, 1), [Format = "H:mm:ss", Culture = ""])
        // Displays 6:09:01
    }
in
    Source
```

[Back to table](#table)

### <a name="HH_Specifier"></a> The "HH" custom format specifier

The "HH" custom format specifier (plus any number of additional "H" specifiers) represents the hour as a number from 00 to 23; that is, the hour is represented by a zero-based 24-hour clock that counts the hours since midnight. A single-digit hour is formatted with a leading zero.

The following example includes the "HH" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 6, 9, 1), [Format = "HH:mm:ss", Culture = ""])
        // Displays 06:09:01
    }
in
    Source
```

[Back to table](#table)

## Time zone "K" format specifier

### <a name="KSpecifier"></a> The "K" custom format specifier

The "K" custom format specifier represents the time zone information of a date and time value. When this format specifier is used with **DateTimeZone** values, the result string is defined as:

- For the local time zone, this specifier produces a result string containing the local offset from Coordinated Universal Time (UTC), for example, "-07:00", if your query runs in Power Query Desktop. If your query runs in Power Query Online, the result string produces no offset from UTC time, that is, "+00:00".

- For a UTC time, the result string produces no offset from UTC time; that is, "+00:00 to represent a UTC date.

- For a time from an unspecified time zone, the result is empty.

If the "K" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example displays the string that results from using the "K" custom format specifier with various values on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    Source =
    {
        DateTimeZone.ToText(DateTimeZone.LocalNow(),[Format="%K"]),
        // Displays -07:00 (Desktop) or +00:00 (Online)

        DateTimeZone.ToText(DateTimeZone.UtcNow(),[Format="%K"]),
        // Displays +00:00

        Text.Format("'#{0}'", {DateTime.ToText(DateTime.LocalNow(),[Format="%K"])})
        // Displays ''
    }
in
    Source
```

> [!NOTE]
>The value returned by [DateTimeZone.LocalNow](datetimezone-localnow.md) depends on whether you're running Power Query on a local machine or online. For example, in the sample above on a system in the U.S. Pacific Time zone, Power Query Desktop returns `-07:00` because it's reading the time set on your local machine. However, Power Query Online returns `+00:00` because it's reading the time set on the cloud virtual machines, which are set to UTC.

[Back to table](#table)

## Minute "m" format specifier

### <a name="mSpecifier"></a> The "m" custom format specifier

The "m" custom format specifier represents the minute as a number from 0 to 59. The minute represents whole minutes that have passed since the last hour. A single-digit minute is formatted without a leading zero.

If the "m" format specifier is used without other custom format specifiers, it's interpreted as the "m" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "m" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 6:9:1 P

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = "el-GR"]),
        // Displays 6:9:1 μ

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 9:18:1.5 A

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = "el-GR"])
        // Displays 9:18:1.5 π
    }
in
    Source
```

[Back to table](#table)

### <a name="mmSpecifier"></a> The "mm" custom format specifier

The "mm" custom format specifier (plus any number of additional "m" specifiers) represents the minute as a number from 00 to 59. The minute represents whole minutes that have passed since the last hour. A single-digit minute is formatted with a leading zero.

The following example includes the "mm" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = ""]),
        // Displays 06:09:01 PM

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = "hu-HU"]),
        // Displays 06:09:01 du.

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = ""]),
        // Displays 09:18:01.50 AM

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = "hu-HU"])
        // Displays 09:18:01.50 de.
    }
in
    Source
```

[Back to table](#table)

## Month "M" format specifier

### <a name="M_Specifier"></a> The "M" custom format specifier

The "M" custom format specifier represents the month as a number from 1 to 12 (or from 1 to 13 for calendars that have 13 months). A single-digit month is formatted without a leading zero.

If the "M" format specifier is used without other custom format specifiers, it's interpreted as the "M" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "M" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(2024, 8, 18), [Format = "(M) MMM, MMMM", Culture = "en-US"]),
        // Displays (8) Aug, August

        Date.ToText(#date(2024, 8, 18), [Format = "(M) MMM, MMMM", Culture = "nl-NL"]),
        // Displays (8) aug, augustus

        Date.ToText(#date(2024, 8, 18), [Format = "(M) MMM, MMMM", Culture = "lv-LV"])
        // Displays (8) aug., augusts
    }
in
    Source
```

[Back to table](#table)

### <a name="MM_Specifier"></a> The "MM" custom format specifier

The "MM" custom format specifier represents the month as a number from 01 to 12 (or from 1 to 13 for calendars that have 13 months). A single-digit month is formatted with a leading zero.

The following example includes the "MM" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 2, 6, 30, 15), [Format = "dd, MM", Culture = ""])
        // Displays 02, 01
    }
in
    Source
```

[Back to table](#table)

### <a name="MMM_Specifier"></a> The "MMM" custom format specifier

The "MMM" custom format specifier represents the abbreviated name of the month. The localized abbreviated name of the month is retrieved from the abbreviated month names of the current or specified culture. If there is a "d" or "dd" custom format specifier in the custom format string, the month name is retrieved from the abbreviated genitive names instead.

The following example includes the "MMM" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "ddd d MMM", Culture = "en-US"]),
        // Displays Thu 29 Aug

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "ddd d MMM", Culture = "fr-FR"])
        // Displays jeu. 29 août
    }
in
    Source
```

[Back to table](#table)

### <a name="MMMM_Specifier"></a> The "MMMM" custom format specifier

The "MMMM" custom format specifier represents the full name of the month. The localized name of the month is retrieved from the current or specified culture. If there is a "d" or "dd" custom format specifier in the custom format string, the month name is retrieved from the abbreviated genitive names instead.

The following example includes the "MMMM" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "dddd dd MMMM", Culture = "en-US"]),
        // Displays Thursday 29 August

        DateTime.ToText(#datetime(2024, 8, 29, 19, 27, 15), [Format = "dddd dd MMMM", Culture = "it-IT"])
        // Displays giovedì 29 agosto
    }
in
    Source
```

[Back to table](#table)

## Seconds "s" format specifier

### <a name="sSpecifier"></a> The "s" custom format specifier

The "s" custom format specifier represents the seconds as a number from 0 to 59. The result represents whole seconds that have passed since the last minute. A single-digit second is formatted without a leading zero.

If the "s" format specifier is used without other custom format specifiers, it's interpreted as the "s" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "s" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 6:9:1 P

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = "el-GR"]),
        // Displays 6:9:1 μ

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 9:18:1.5 A

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = "el-GR"])
        // Displays 9:18:1.5 π
    }
in
    Source
```

[Back to table](#table)

### <a name="ssSpecifier"></a> The "ss" custom format specifier

The "ss" custom format specifier (plus any number of additional "s" specifiers) represents the seconds as a number from 00 to 59. The result represents whole seconds that have passed since the last minute. A single-digit second is formatted with a leading zero.

The following example includes the "ss" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = ""]),
        // Displays 06:09:01 PM

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = "hu-HU"]),
        // Displays 06:09:01 du.

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = ""]),
        // Displays 09:18:01.50 AM

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = "hu-HU"])
        // Displays 09:18:01.50 de.
    }
in
    Source
```

[Back to table](#table)

## Meridiem "t" format specifier

### <a name="tSpecifier"></a> The "t" custom format specifier

The "t" custom format specifier represents the first character of the AM/PM designator. The appropriate localized designator is retrieved from the current or specific culture. The AM designator is used for all times from 0:00:00 (midnight) to 11:59:59.999. The PM designator is used for all times from 12:00:00 (noon) to 23:59:59.999.

If the "t" format specifier is used without other custom format specifiers, it's interpreted as the "t" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "t" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 6:9:1 P

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "h:m:s.F t", Culture = "el-GR"]),
        // Displays 6:9:1 μ

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = ""]),
        // Displays 9:18:1.5 A

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "h:m:s.F t", Culture = "el-GR"])
        // Displays 9:18:1.5 π
    }
in
    Source
```

[Back to table](#table)

### <a name="ttSpecifier"></a> The "tt" custom format specifier

The "tt" custom format specifier (plus any number of additional "t" specifiers) represents the entire AM/PM designator. The appropriate localized designator is retrieved from the current or specific culture. The AM designator is used for all times from 0:00:00 (midnight) to 11:59:59.999. The PM designator is used for all times from 12:00:00 (noon) to 23:59:59.999.

Make sure to use the "tt" specifier for languages for which it's necessary to maintain the distinction between AM and PM. An example is Japanese, for which the AM and PM designators differ in the second character instead of the first character.

The following example includes the "tt" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = ""]),
        // Displays 06:09:01 PM

        DateTime.ToText(#datetime(2024, 1, 1, 18, 9, 1), [Format = "hh:mm:ss tt", Culture = "hu-HU"]),
        // Displays 06:09:01 du.

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = ""]),
        // Displays 09:18:01.50 AM

        DateTime.ToText(#datetime(2024, 1, 1, 9, 18, 1.500), [Format = "hh:mm:ss.ff tt", Culture = "hu-HU"])
        // Displays 09:18:01.50 de.
    }
in
    Source
```

[Back to table](#table)

## Year "y" format specifier

### <a name="ySpecifier"></a> The "y" custom format specifier

The "y" custom format specifier represents the year as a one-digit or two-digit number. If the year has more than two digits, only the two low-order digits appear in the result. If the first digit of a two-digit year begins with a zero (for example, 2008), the number is formatted without a leading zero.

If the "y" format specifier is used without other custom format specifiers, it's interpreted as the "y" standard date and time format specifier. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "y" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(1, 12, 1), [Format = "%y"]),
        // Displays 1

        Date.ToText(#date(2024, 1, 1), [Format = "%y"])
        // Displays 24
    }
in
    Source
```

[Back to table](#table)

### <a name="yySpecifier"></a> The "yy" custom format specifier

The "yy" custom format specifier represents the year as a two-digit number. If the year has more than two digits, only the two low-order digits appear in the result. If the two-digit year has fewer than two significant digits, the number is padded with leading zeros to produce two digits.

In a parsing operation, a two-digit year that is parsed using the "yy" custom format specifier is interpreted based on the format provider's current calendar. The following example parses the string representation of a date that has a two-digit year by using the default Gregorian calendar of the en-US culture, which, in this case, is the current culture. The values returned for the four-digit date depend on the 100 year range set by the operating system.

```powerquery-m
let
    // Define the date format and value
    fmt = "dd-MMM-yy",

    // Convert year 49 to a 4-digit year
    firstDate = Text.Format("#{0}", { Date.FromText("24-Jan-49", [Format = fmt]) }),

    // Convert year 50 to a 4-digit year
    finalDate = Text.Format("#{0}", { Date.FromText("24-Jan-50", [Format = fmt]) }),
    Heading = "Default Two Digit Year Range: 1950 - 2049",
    result = {Heading, firstDate, finalDate}
in
    result

// The example displays the following output:
//       Default Two Digit Year Range: 1950 - 2049
//       1/24/2049
//       1/24/1950
```

The following example includes the "yy" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(1, 12, 1), [Format = "yy"]),
        // Displays 01

        Date.ToText(#date(2024, 1, 1), [Format = "yy"])
        // Displays 24
    }
in
    Source
```

[Back to table](#table)

### <a name="yyySpecifier"></a> The "yyy" custom format specifier

The "yyy" custom format specifier represents the year with a minimum of three digits. If the year has more than three significant digits, they are included in the result string. If the year has fewer than three digits, the number is padded with leading zeros to produce three digits.

> [!NOTE]
> For the Thai Buddhist calendar, which can have five-digit years, this format specifier displays all significant digits.

The following example includes the "yyy" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(1, 12, 1), [Format = "yyy"]),
        // Displays 001

        Date.ToText(#date(2024, 1, 1), [Format = "yyy"])
        // Displays 2024
    }
in
    Source
```

[Back to table](#table)

### <a name="yyyySpecifier"></a> The "yyyy" custom format specifier

The "yyyy" custom format specifier represents the year with a minimum of four digits. If the year has more than four significant digits, they are included in the result string. If the year has fewer than four digits, the number is padded with leading zeros to produce four digits.

> [!NOTE]
> For the Thai Buddhist calendar, which can have five-digit years, this format specifier displays a minimum of four digits.

The following example includes the "yyyy" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(1, 12, 1), [Format = "yyyy"]),
        // Displays 0001

        Date.ToText(#date(2024, 1, 1), [Format = "yyyy"])
        // Displays 2024
    }
in
    Source
```

[Back to table](#table)

### <a name="yyyyySpecifier"></a> The "yyyyy" custom format specifier

The "yyyyy" custom format specifier (plus any number of additional "y" specifiers) represents the year with a minimum of five digits. If the year has more than five significant digits, they are included in the result string. If the year has fewer than five digits, the number is padded with leading zeros to produce five digits.

If there are additional "y" specifiers, the number is padded with as many leading zeros as necessary to produce the number of "y" specifiers.

The following example includes the "yyyyy" custom format specifier in a custom format string.

```powerquery-m
let
    Source =
    {
        Date.ToText(#date(1, 12, 1), [Format = "yyyyy"]),
        // Displays 00001

        Date.ToText(#date(2024, 1, 1), [Format = "yyyyy"])
        // Displays 02024
    }
in
    Source
```

[Back to table](#table)

## Offset "z" format specifier

### <a name="zSpecifier"></a> The "z" custom format specifier

With **DateTimeZone** values, the "z" custom format specifier represents the signed offset of the specified time zone from Coordinated Universal Time (UTC), measured in hours. The offset is always displayed with a leading sign. A plus sign (+) indicates hours ahead of UTC, and a minus sign (-) indicates hours behind UTC. A single-digit offset is formatted *without* a leading zero.

The following table shows how the offset value changes depending on the **DateTimeZone** function.

| DateTimeZone value | Offset value |
| --- | --- |
| [DateTimeZone.LocalNow](datetimezone-localnow.md) | On Power Query Desktop, the signed offset of the local operating system's time zone from UTC. On Power Query Online, returns `+00`. |
| [DateTimeZone.UtcNow](datetimezone-utcnow.md) | Returns `+0`. |

If the "z" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

The following example includes the "z" custom format specifier in a custom format string on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    Source = 
    {
        DateTimeZone.ToText(DateTimeZone.LocalNow(), [Format="{0:%z}"]),
        // Displays {0:-7} on Power Query Desktop
        // Displays {0:+0} on Power Query Online

        DateTimeZone.ToText(DateTimeZone.UtcNow(),[Format="{0:%z}"]),
        // Displays {0:+0}

        DateTimeZone.ToText(DateTimeZone.SwitchZone(
            #datetimezone(2024, 8, 1, 0, 0, 0, 0, 0), 6), 
            [Format = "{0:%z}"]
        )
        // Displays {0:+6}
    }
in
    Source
```

> [!NOTE]
>The value returned by [DateTimeZone.LocalNow](datetimezone-localnow.md) depends on whether you're running Power Query on a local machine or online. For example, in the sample above on a system in the U.S. Pacific Time zone, Power Query Desktop returns `{0:-7}` because it's reading the time set on your local machine. However, Power Query Online returns `{0:+0}` because it's reading the time set on the cloud virtual machines, which are set to UTC.

[Back to table](#table)

### <a name="zzSpecifier"></a> The "zz" custom format specifier

With **DateTimeZone** values, the "zz" custom format specifier represents the signed offset of the specified time zone from UTC, measured in hours. The offset is always displayed with a leading sign. A plus sign (+) indicates hours ahead of UTC, and a minus sign (-) indicates hours behind UTC. A single-digit offset is formatted *with* a leading zero.

The following table shows how the offset value changes depending on the **DateTimeZone** function.

| DateTimeZone value | Offset value |
| --- | --- |
| [DateTimeZone.LocalNow](datetimezone-localnow.md) | On Power Query Desktop, the signed offset of the local operating system's time zone from UTC. On Power Query Online, returns `+00`. |
| [DateTimeZone.UtcNow](datetimezone-utcnow.md) | Returns `+00`. |

The following example includes the "zz" custom format specifier in a custom format string on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    Source = 
    {
        DateTimeZone.ToText(DateTimeZone.LocalNow(), [Format="{0:zz}"]),
        // Displays {0:-07} on Power Query Desktop
        // Displays {0:+00} on Power Query Online

        DateTimeZone.ToText(DateTimeZone.UtcNow(),[Format="{0:zz}"]),
        // Displays {0:+00}

        DateTimeZone.ToText(DateTimeZone.SwitchZone(
            #datetimezone(2024, 8, 1, 0, 0, 0, 0, 0), 6), 
            [Format = "{0:zz}"]
        )
        // Displays {0:+06}
    }
in
    Source
```

> [!NOTE]
>The value returned by [DateTimeZone.LocalNow](datetimezone-localnow.md) depends on whether you're running Power Query on a local machine or online. For example, in the sample above on a system in the U.S. Pacific Time zone, Power Query Desktop returns `{0:-07}` because it's reading the time set on your local machine. However, Power Query Online returns `{0:+00}` because it's reading the time set on the cloud virtual machines, which are set to UTC.

[Back to table](#table)

### <a name="zzzSpecifier"></a> The "zzz" custom format specifier

With **DateTimeZone** values, the "zzz" custom format specifier represents the signed offset of the specified time zone from UTC, measured in hours and minutes. The offset is always displayed with a leading sign. A plus sign (+) indicates hours ahead of UTC, and a minus sign (-) indicates hours behind UTC. A single-digit offset is formatted with a leading zero.

The following table shows how the offset value changes depending on the **DateTimeZone** function.

| DateTimeZoneValue value | Offset value |
| --- | --- |
| [DateTimeZone.LocalNow](datetimezone-localnow.md) | On Power Query Desktop, the signed offset of the local operating system's time zone from UTC. On Power Query Online, returns `+00`.|
| [DateTimeZone.UtcNow](datetimezone-utcnow.md) | Returns `+00:00`. |

The following example includes the "zzz" custom format specifier in a custom format string on a system in the U.S. Pacific Time zone.

```powerquery-m
let
    Source = 
    {
        DateTimeZone.ToText(DateTimeZone.LocalNow(), [Format="{0:zzz}"]),
        // Displays {0:-07:00} on Power Query Desktop
        // Displays {0:+00:00} on Power Query Online

        DateTimeZone.ToText(DateTimeZone.UtcNow(),[Format="{0:zzz}"]),
        // Displays {0:+00:00}

        DateTimeZone.ToText(DateTimeZone.SwitchZone(
            #datetimezone(2024, 8, 1, 0, 0, 0, 0, 0), 6), 
            [Format = "{0:zzz}"]
        )
        // Displays {0:+06:00}
    }
in
    Source
```

> [!NOTE]
>The value returned by [DateTimeZone.LocalNow](datetimezone-localnow.md) depends on whether you're running Power Query on a local machine or online. For example, in the sample above on a system in the U.S. Pacific Time zone, Power Query Desktop returns `{0:-07:00}` because it's reading the time set on your local machine. However, Power Query Online returns `{0:+00:00}` because it's reading the time set on the cloud virtual machines, which are set to UTC.

[Back to table](#table)

## Date and time separator specifiers

### <a name="timeSeparator"></a> The ":" custom format specifier

The ":" custom format specifier represents the time separator, which is used to differentiate hours, minutes, and seconds. The appropriate localized time separator is retrieved from the current or specified culture.

> [!NOTE]
> To change the time separator for a particular date and time string, specify the separator character within a literal string delimiter. For example, the custom format string `hh_dd_ss` produces a result string in which "_" (an underscore) is always used as the time separator.

If the ":" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

[Back to table](#table)

### <a name="dateSeparator"></a> The "/" custom format specifier

The "/" custom format specifier represents the date separator, which is used to differentiate years, months, and days. The appropriate localized date separator is retrieved from the current or specified culture.

> [!NOTE]
> To change the date separator for a particular date and time string, specify the separator character within a literal string delimiter. For example, the custom format string `mm/dd/yyyy` produces a result string in which "/" is always used as the date separator.

If the "/" format specifier is used without other custom format specifiers, it's interpreted as a standard date and time format specifier and throws an expression error. For more information about using a single format specifier, go to [Using Single Custom Format Specifiers](#using-single-custom-format-specifiers) later in this article.

[Back to table](#table)

## <a name="Literals"></a> Character literals

The following characters in a custom date and time format string are reserved and are always interpreted as formatting characters or, in the case of `"`, `'`, `/`, and `\`, as special characters.

- `F`
- `H`
- `K`
- `M`
- `d`
- `f`
- `g`
- `h`
- `m`
- `s`
- `t`
- `y`
- `z`
- `%`
- `:`
- `/`
- `"`
- `'`
- `\`

All other characters are always interpreted as character literals and, in a formatting operation, are included in the result string unchanged.  In a parsing operation, they must match the characters in the input string exactly; the comparison is case-sensitive.

The following example includes the literal characters "PST" (for Pacific Standard Time) and "PDT" (for Pacific Daylight Time) to represent the local time zone in a format string. Note that the string is included in the result string, and that a string that includes the local time zone string also parses successfully.

```powerquery-m
let
    #"Date Formats" = {"dd MMM yyyy hh:mm tt PST", "dd MMM yyyy hh:mm tt PDT"},
    Source = 
    {
        DateTime.ToText(#datetime(2024, 8, 18, 16, 50, 0), [Format = #"Date Formats"{1}]),
        try DateTime.ToText(DateTime.FromText(
            "25 Dec 2023 12:00 pm PST", [Format = #"Date Formats"{0}])) 
            otherwise "Unable to parse '" & "25 Dec 2023 12:00 pm PST" & "'"
    }
in
    Source

// The example displays the following output text:
//       18 Aug 2024 04:50 PM PDT
//       12/25/2023 12:00:00 PM
```

There are two ways to indicate that characters are to be interpreted as literal characters and not as reserve characters, so that they can be included in a result string or successfully parsed in an input string:

- By escaping each reserved character. For more information, go to [Using the escape sequences](#escape).

  The following example includes the literal characters "pst" (for Pacific Standard time) to represent the local time zone in a format string. Because both "s" and "t" are custom format strings, both characters must be escaped to be interpreted as character literals.

  ```powerquery-m
  let
        #"Date Format" = "dd MMM yyyy hh:mm tt p's''t'",
        Source = 
        {
            DateTime.ToText(#datetime(2024, 8, 18, 16, 50, 0), [Format = #"Date Format"]),
            try DateTime.ToText(DateTime.FromText(
                "25 Dec 2023 12:00 pm pst", [Format = #"Date Format"]))
                otherwise "Unable to parse '" & "25 Dec 2023 12:00 pm pst" & "'"
        }
  in
        Source

  // The example displays the following output text:
  //       18 Aug 2024 04:50 PM pst
  //       12/25/2016 12:00:00 PM
  ```

- By enclosing the entire literal string in apostrophes. The following example is like the previous one, except that "pst" is enclosed in apostrophes to indicate that the entire delimited string should be interpreted as character literals.

  ```powerquery-m
  let
        #"Date Format" = "dd MMM yyyy hh:mm tt 'pst'",
        Source = 
        {
            DateTime.ToText(#datetime(2024, 8, 18, 16, 50, 0), [Format = #"Date Format"]),
            try DateTime.ToText(DateTime.FromText(
                "25 Dec 2023 12:00 pm pst", [Format = #"Date Format"]))
                otherwise "Unable to parse '" & "25 Dec 2023 12:00 pm pst" & "'"
        }
  in
        Source

  // The example displays the following output text:
  //       18 Aug 2024 04:50 PM pst
  //       12/25/2016 12:00:00 PM
  ```

## Notes

### Using single custom format specifiers

A custom date and time format string consists of two or more characters. Date and time formatting methods interpret any single-character string as a standard date and time format string. If they don't recognize the character as a valid format specifier, they throw an expression error. For example, a format string that consists only of the specifier "h" is interpreted as a standard date and time format string. However, in this particular case, an exception is thrown because there is no "h" standard date and time format specifier.

To use any of the custom date and time format specifiers as the only specifier in a format string (that is, to use the "d", "f", "F", "g", "h", "H", "K", "m", "M", "s", "t", "y", "z", ":", or "/" custom format specifier by itself), include a space before or after the specifier, or include a percent ("%") format specifier before the single custom date and time specifier.

For example, "`%h`" is interpreted as a custom date and time format string that displays the hour represented by the current date and time value. You can also use the " h" or "h " format string, although this includes a space in the result string along with the hour. The following example illustrates these three format strings.

```powerquery-m
let
    date = #datetime(2024, 6, 15, 13, 45, 0),
    Source =
    {
        Text.Format("'#{0}'", {DateTime.ToText(date, [Format = "%h"])}),
        Text.Format("'#{0}'", {DateTime.ToText(date, [Format = " h"])}),
        Text.Format("'#{0}'", {DateTime.ToText(date, [Format = "h "])})
    }
in
    Source

// The example displays a list with the following output text, 
//   with <sp> representing a space:
//       '1'
//       ' 1'
//       '1 ' 
```

#### <a name="escape"></a> Using the escape sequences

The "d", "f", "F", "g", "h", "H", "K", "m", "M", "s", "t", "y", "z", ":", or "/" characters in a format string are interpreted as custom format specifiers rather than as literal characters.

To prevent a character from being interpreted as a format specifier, you can:

- Precede it with a backslash.
- Surround it with a single quote.
- Surround it with two double quotes.

Each of these characters acts as an escape sequence. The escape sequence signifies that the following character or surrounded character is a text literal that should be included in the result string unchanged.

To include a double quote in a result string, you must escape it with another double quote (`""`).

The following example uses different escape sequences to prevent the formatting operation from interpreting the "h" and "m" characters as format specifiers.

```powerquery-m
let
    date = #datetime(2024, 6, 15, 13, 45, 30.90),
    format1 = "h \h m \m",
    format2 = "h ""h"" m ""m""",
    format3 = "h 'h' m 'm'",
    Source = 
    {
        Text.Format("#{0} (#{1}) -> #{2}", {DateTime.ToText(date), format1, DateTime.ToText(date, format1)}),
        Text.Format("#{0} (#{1}) -> #{2}", {DateTime.ToText(date), format2, DateTime.ToText(date, format2)}),
        Text.Format("#{0} (#{1}) -> #{2}", {DateTime.ToText(date), format3, DateTime.ToText(date, format3)})
    }
in
    Source

// The example displays the following output text:
//       6/15/2024 1:45:30 PM (h \h m \m) -> 1 h 45 m
//       6/15/2024 1:45:30 PM (h "h" m "m") -> 1 h 45 m
//       6/15/2024 1:45:30 PM (h 'h' m 'm') -> 1 h 45 m
```

## Related content

- [How culture affects text formatting](how-culture-affects-text-formatting.md)
- [Date, Time, DateTime, and DateTimeZone type conversion](type-conversion.md#date-time-datetime-and-datetimezone)
- [Date functions](date-functions.md)
- [DateTime functions](datetime-functions.md)
- [DateTimeZone functions](datetimezone-functions.md)
- [Time functions](time-functions.md)
- [Standard Date and Time format strings](standard-date-and-time-format-strings.md)
