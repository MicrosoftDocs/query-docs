---
title: Standard numeric format strings
description: In this article, learn to use standard numeric format strings to format common numeric types into text representations in Power Query M.
ms.date: 9/30/2024
ms.topic: reference
---

# Standard numeric format strings

Standard numeric format strings are used to format common numeric types. A standard numeric format string takes the form *`[format specifier][precision specifier]`*, where:

- *Format specifier* is a single alphabetic character that specifies the type of number format, for example, currency or percent. Any numeric format string that contains more than one alphabetic character, including white space, is interpreted as a custom numeric format string. For more information, go to [Custom numeric format strings](custom-numeric-format-strings.md).

- *Precision specifier* is an optional integer that affects the number of digits in the resulting string. The precision specifier controls the number of digits in the string representation of a number.

  When the precision specifier controls the number of fractional digits in the result string, the result string reflects a number that is rounded to a representable result nearest to the infinitely precise result.

  > [!NOTE]
  > The precision specifier determines the number of digits in the result string. To pad a result string with leading or trailing spaces or other characters (such a 0), use the [Text.PadStart](text-padstart.md) and [Text.PadEnd](text-padend.md) functions and use the overall length `count` in these functions to pad the result string.

Standard numeric format strings are supported by the [Number.ToText](number-totext.md) function.

## Standard format specifiers

The following table describes the standard numeric format specifiers and displays sample output produced by each format specifier. Go to the [Notes](#notes) section for additional information about using standard numeric format strings, and the [Code example](#code-example) section for a comprehensive illustration of their use.

> [!NOTE]
> The result of a formatted string for a specific culture might differ from the following examples. Operating system settings, user settings, environment variables, and other settings on the system you use can all affect the format.

| Format specifier | Name | Description | Examples |
|--|--|--|--|
| "C" or "c" | Currency | Result: A currency value.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: Defined by the culture.<br /><br /> More information: [The Currency ("C") Format Specifier](#CFormatString). | 123.456 ("C", en-US)<br />-> \\$123.46<br /><br /> 123.456 ("C", fr-FR)<br />-> 123,46 &euro;<br /><br /> 123.456 ("C", ja-JP)<br />-> ¥123<br /><br /> -123.456 ("C3", en-US)<br />-> (\\$123.456)<br /><br /> -123.456 ("C3", fr-FR)<br />-> -123,456 &euro;<br /><br /> -123.456 ("C3", ja-JP)<br />-> -¥123.456 |
| "D" or "d" | Decimal | Result: Integer digits with optional negative sign.<br /><br /> Supported by: Integral types only.<br /><br /> Precision specifier: Minimum number of digits.<br /><br /> Default precision specifier: Minimum number of digits required.<br /><br /> More information: [The Decimal("D") Format Specifier](#DFormatString). | 1234 ("D")<br />-> 1234<br /><br /> -1234 ("D6")<br />-> -001234 |
| "E" or "e" | Exponential (scientific) | Result: Exponential notation.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: 6.<br /><br /> More information: [The Exponential ("E") Format Specifier](#EFormatString). | 1052.0329112756 ("E", en-US)<br />-> 1.052033E+003<br /><br /> 1052.0329112756 ("e", fr-FR)<br />-> 1,052033e+003<br /><br /> -1052.0329112756 ("e2", en-US)<br />-> -1.05e+003<br /><br /> -1052.0329112756 ("E2", fr-FR)<br />-> -1,05E+003 |
| "F" or "f" | Fixed-point | Result: Integral and decimal digits with optional negative sign.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: Defined by the culture.<br /><br /> More information: [The Fixed-Point ("F") Format Specifier](#FFormatString). | 1234.567 ("F", en-US)<br />-> 1234.57<br /><br /> 1234.567 ("F", de-DE)<br />-> 1234,57<br /><br /> 1234 ("F1", en-US)<br />-> 1234.0<br /><br /> 1234 ("F1", de-DE)<br />-> 1234,0<br /><br /> -1234.56 ("F4", en-US)<br />-> -1234.5600<br /><br /> -1234.56 ("F4", de-DE)<br />-> -1234,5600 |
| "G" or "g" | General | Result: The more compact of either fixed-point or scientific notation.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of significant digits.<br /><br /> Default precision specifier: Depends on numeric type.<br /><br /> More information: [The General ("G") Format Specifier](#GFormatString). | -123.456 ("G", en-US)<br />-> -123.456<br /><br /> -123.456 ("G", sv-SE)<br />-> -123,456<br /><br /> 123.4546 ("G4", en-US)<br />-> 123.5<br /><br /> 123.4546 ("G4", sv-SE)<br />-> 123,5<br /><br /> -1.234567890e-25 ("G", en-US)<br />-> -1.23456789E-25<br /><br /> -1.234567890e-25 ("G", sv-SE)<br />-> -1,23456789E-25 |
| "N" or "n" | Number | Result: Integral and decimal digits, group separators, and a decimal separator with optional negative sign.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Desired number of decimal places.<br /><br /> Default precision specifier: Defined by the culture.<br /><br /> More information: [The Numeric ("N") Format Specifier](#NFormatString). | 1234.567 ("N", en-US)<br />-> 1,234.57<br /><br /> 1234.567 ("N", ru-RU)<br />-> 1 234,57<br /><br /> 1234 ("N1", en-US)<br />-> 1,234.0<br /><br /> 1234 ("N1", ru-RU)<br />-> 1 234,0<br /><br /> -1234.56 ("N3", en-US)<br />-> -1,234.560<br /><br /> -1234.56 ("N3", ru-RU)<br />-> -1 234,560 |
| "P" or "p" | Percent | Result: Number multiplied by 100 and displayed with a percent symbol.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Desired number of decimal places.<br /><br /> Default precision specifier: Defined by the culture.<br /><br /> More information: [The Percent ("P") Format Specifier](#PFormatString). | 1 ("P", en-US)<br />-> 100.00 %<br /><br /> 1 ("P", fr-FR)<br />-> 100,00 %<br /><br /> -0.39678 ("P1", en-US)<br />-> -39.7 %<br /><br /> -0.39678 ("P1", fr-FR)<br />-> -39,7 % |
| "X" or "x" | Hexadecimal | Result: A hexadecimal string.<br /><br /> Supported by: Integral types only.<br /><br /> Precision specifier: Number of digits in the result string.<br /><br /> More information: [The Hexadecimal ("X") Format Specifier](#XFormatString). | 255 ("X")<br />-> FF<br /><br /> -1 ("x")<br />-> ff<br /><br /> 255 ("x4")<br />-> 00ff<br /><br /> -1 ("X4")<br />-> 00FF |
| Any other single character | Unknown specifier | Result: Throws an Expression error at run time. |  |

## Use standard numeric format strings

A standard numeric format string can be used to define the formatting of a numeric value. It can be passed to the [Number.ToText](number-totext.md) `format` parameter. The following example formats a numeric value as a currency string in the current culture (in this case, the en-US culture).

```powerquery-m
Number.ToText(123.456, "C2")
// Displays $123.46
```

Optionally, you can supply a `count` argument in the [Text.PadStart](text-padstart.md) and [Text.PadEnd](text-padend.md) functions to specify the width of the numeric field and whether its value is right- or left-aligned. For example, the following sample left-aligns a currency value in a 28-character field, and it right-aligns a currency value in a 14-character field (when using a monospaced font).

```powerquery-m
let
    amounts = {16305.32, 18794.16},
    result = Text.Format("    Beginning Balance           Ending Balance#(cr,lf)    #{0}#{1}",
    {
        Text.PadEnd(Number.ToText(amounts{0}, "C2"), 28), 
        Text.PadStart(Number.ToText(amounts{1}, "C2"), 14)
    })
in
    result

// Displays:
//    Beginning Balance           Ending Balance
//    $16,305.32                      $18,794.16

```

The following sections provide detailed information about each of the standard numeric format strings.

<a name="CFormatString"></a>

## Currency format specifier (C)

The "C" (or currency) format specifier converts a number to a string that represents a currency amount. The precision specifier indicates the desired number of decimal places in the result string. If the precision specifier is omitted, the default number of decimal places to use in currency values is 2.

If the value to be formatted has more than the specified or default number of decimal places, the fractional value is rounded in the result string. If the value to the right of the number of specified decimal places is 5 or greater, the last digit in the result string is rounded away from zero.

The result string is affected by the formatting information of the current culture.

The following example formats a value with the currency format specifier:

```powerquery-m
let
    Source = 
    {
        Number.ToText(12345.6789, "C"),
        Number.ToText(12345.6789, "C3"),
        Number.ToText(12345.6789, "C3", "da-DK")
    }
in
    Source 

// The example displays the following list on a system whose
// current culture is English (United States):
//       $12,345.68
//       $12,345.679
//       12.345,679 kr.
```

<a name="DFormatString"></a>

## Decimal format specifier (D)

The "D" (or decimal) format specifier converts a number to a string of decimal digits (0-9), prefixed by a minus sign if the number is negative. This format is supported only for integral types.

The precision specifier indicates the minimum number of digits desired in the resulting string. If required, the number is padded with zeros to its left to produce the number of digits given by the precision specifier. If no precision specifier is specified, the default is the minimum value required to represent the integer without leading zeros.

The result string is affected by the formatting information of the current culture.

The following example formats a value with the decimal format specifier.

```powerquery-m
let
    Source = 
    { 
        Number.ToText(12345, "D"),
        // Displays 12345

        Number.ToText(12345, "D8"),
        // Displays 00012345

        Number.ToText(-12345, "D"),
        // Displays -12345

        Number.ToText(-12345, "D8")
        // Displays -00012345
    }
in
    Source 
```

<a name="EFormatString"></a>

## Exponential format specifier (E)

The exponential ("E") format specifier converts a number to a string of the form "-d.ddd…E+ddd" or "-d.ddd…e+ddd", where each "d" indicates a digit (0-9). The string starts with a minus sign if the number is negative. Exactly one digit always precedes the decimal point.

The precision specifier indicates the desired number of digits after the decimal point. If the precision specifier is omitted, a default of six digits after the decimal point is used.

The case of the format specifier indicates whether to prefix the exponent with an "E" or an "e". The exponent always consists of a plus or minus sign and a minimum of three digits. The exponent is padded with zeros to meet this minimum, if required.

The result string is affected by the formatting information of the current culture.

The following example formats a value with the exponential format specifier:

```powerquery-m
let
    Source = 
    { 
        Number.ToText(12345.6789, "E", ""),
        // Displays 1.234568E+004

        Number.ToText(12345.6789, "E10", ""),
        // Displays 1.2345678900E+004

        Number.ToText(12345.6789, "e4", ""),
        // 1.2346e+004

        Number.ToText(12345.6789, "E", "fr-FR")
        // Displays 1,234568E+004
    }
in
    Source 
```

> [!NOTE]
> The blank text value ("") in the last parameter of [Number.ToText](number-totext.md) in the previous sample refers to the invariant culture.

<a name="FFormatString"></a>

## Fixed-point format specifier (F)

The fixed-point ("F") format specifier converts a number to a string of the form "-ddd.ddd…" where each "d" indicates a digit (0-9). The string starts with a minus sign if the number is negative.

The precision specifier indicates the desired number of decimal places. If the precision specifier is omitted, the default number of decimal places to use in numeric values is 2.

The result string is affected by the formatting information of the current culture.

The following example formats a double and an integer value with the fixed-point format specifier:

```powerquery-m
let
    Source =
    {
        Number.ToText(17843, "F", ""),
        // Displays 17843.00

        Number.ToText(-29541, "F3", ""),
        // Displays -29541.000

        Number.ToText(18934.1879, "F", ""),
        // Displays 18934.19

        Number.ToText(18934.1879, "F0", ""),
        // Displays 18934

        Number.ToText(-1898300.1987, "F1", ""),
        // Displays -1898300.2

        Number.ToText(-1898300.1987, "F3", "es-ES")
        // Displays -1898300,199
    }
in
    Source
```

<a name="GFormatString"></a>

## General format specifier (G)

The general ("G") format specifier converts a number to the more compact of either fixed-point or scientific notation, depending on the type of the number and whether a precision specifier is present. The precision specifier defines the maximum number of significant digits that can appear in the result string. If the precision specifier is omitted or zero, the type of the number determines the default precision, as indicated in the following table.

|Numeric type                | Default precision |
|----------------------------|-------------------|
|`Byte.Type`  or `Int8.Type` |3 digits|
|`Int16.Type`                |5 digits|
|`Int32.Type`                |10 digits|
|`Int64.Type`                |19 digits|
|`Single.Type`               |9 digits|
|`Double.Type`               |17 digits|
|`Decimal.Type`              |15 digits|

Fixed-point notation is used if the exponent that would result from expressing the number in scientific notation is greater than -5 and less than the precision specifier; otherwise, scientific notation is used. The result contains a decimal point if required, and trailing zeros after the decimal point are omitted. If the precision specifier is present and the number of significant digits in the result exceeds the specified precision, the excess trailing digits are removed by rounding.

However, if the number is a `Decimal.Type` and the precision specifier is omitted, fixed-point notation is always used and trailing zeros are preserved.

If scientific notation is used, the exponent in the result is prefixed with "E" if the format specifier is "G", or "e" if the format specifier is "g". The exponent contains a minimum of two digits. This differs from the format for scientific notation that is produced by the exponential format specifier, which includes a minimum of three digits in the exponent.

The result string is affected by the formatting information of the current culture.

The following example formats assorted floating-point values with the general format specifier:

```powerquery-m
let
    Source =
    {
        Number.ToText(12345.6789, "G", ""),
        // Displays 12345.6789

        Number.ToText(12345.6789, "G", "fr-FR"),
        // Displays 12345,6789

        Number.ToText(12345.6789, "G7", ""),
        // Displays 12345.68

        Number.ToText(.0000023, "G", ""),
        // Displays 2.3E-06

        Number.ToText(.0000023, "G", "fr-FR"),
        // Displays 2,3E-06

        Number.ToText(.0023, "G", ""),
        // Displays 0.0023

        Number.ToText(1234, "G2", ""),
        // Displays 1.2E+03

        Number.ToText(Number.PI, "G5", "")
        // Displays 3.1416
    }
in
    Source
```

<a name="NFormatString"></a>

## Numeric format specifier (N)

The numeric ("N") format specifier converts a number to a string of the form "-d,ddd,ddd.ddd…", where "-" indicates a negative number symbol if required, "d" indicates a digit (0-9), "," indicates a group separator, and "." indicates a decimal point symbol. The precision specifier indicates the desired number of digits after the decimal point. If the precision specifier is omitted, the number of decimal places is defined by the current culture.

The result string is affected by the formatting information of the current culture.

The following example formats assorted floating-point values with the number format specifier:

```powerquery-m
let
    Source =
    {
        Number.ToText(-12445.6789, "N", ""),
        // Displays -12,445.68

        Number.ToText(-12445.6789, "N1", "sv-SE"),
        // Displays -12 445,7

        Number.ToText(123456789, "N1", "")
        // Displays 123,456,789.0
    }
in
    Source
```

<a name="PFormatString"></a>

## Percent format specifier (P)

The percent ("P") format specifier multiplies a number by 100 and converts it to a string that represents a percentage. The precision specifier indicates the desired number of decimal places. If the precision specifier is omitted, the default numeric precision supplied by the current culture is used.

The following example formats floating-point values with the percent format specifier:

```powerquery-m
let
    Source =
    {
        Number.ToText(.2468013, "P", ""),
        // Displays 24.68 %

        Number.ToText(.2468013, "P", "hr-HR"),
        // Displays 24,68 %

        Number.ToText(.2468013, "P1", "en-US")
        // Displays 24.7%
    }
in
    Source
```

<a name="XFormatString"></a>

## Hexadecimal format specifier (X)

The hexadecimal ("X") format specifier converts a number to a string of hexadecimal digits. The case of the format specifier indicates whether to use uppercase or lowercase characters for hexadecimal digits that are greater than 9. For example, use "X" to produce "ABCDEF", and "x" to produce "abcdef". This format is supported only for integral types.

The precision specifier indicates the minimum number of digits desired in the resulting string. If required, the number is padded with zeros to its left to produce the number of digits given by the precision specifier.

The result string isn't affected by the formatting information of the current culture.

The following example formats values with the hexadecimal format specifier.

```powerquery-m
let
    Source =
    {
        Number.ToText(0x2045e, "x"),
        // Displays 2045e

        Number.ToText(0x2045e, "X"),
        // Displays 2045E

        Number.ToText(0x2045e, "X8"),
        // Displays 0002045E

        Number.ToText(123456789, "X"),
        // Displays 75BCD15

        Number.ToText(123456789, "X2")
        // Displays 75BCD15
    }
in
    Source
```

## Notes

This section contains additional information about using standard numeric format strings.

### How culture affects numeric format strings

Different countries and language groups have different conventions for formatting numbers. In Power Query, *culture* refers to the locale whose conventions are used to format numbers in Power Query M.

The culture is set to the system locale (Windows, MacOS) when your queries are first authored. If you move your query to a different location that uses a different default culture, your query still uses the culture of the original location.

However, you can change the default culture in the Power Query settings dialog where you create the query. For example, if you are running Power Query from Excel:

1. In Power Query, select **File** > **Options and settings** > **Query options**.
1. Under **Current Workbook**, select **Regional Settings**.
1. Select the locale you want to use.

Other versions of Power Query work similarly. In general, within Power Query you select **Options**, which opens the **Options** dialog. Then select **Regional Settings** and select the locale you want to use.

> [!NOTE]
> The current default culture is different than the invariant culture. To use the current default culture, no culture setting is required in your Power Query M code. To use the invariant culture, you use the blank text value ("") in the number functions that support culture.

### Integral and floating-point numeric types

Some descriptions of standard numeric format specifiers refer to integral or floating-point numeric types. The integral numeric types are `Byte.Type`, `Int8.Type`, `Int16.Type`, `Int32.Type`, and`Int64.Type`. The floating-point numeric types are `Decimal.Type`, `Single.Type`, and `Double.Type`.

### Floating-point infinities and NaN

Regardless of the format string, if the value of a `Decimal.Type`, `Single.Type` or `Double.Type` floating-point type is positive infinity, negative infinity, or not a number (NaN), the formatted string is the value of the respective [Number.PositiveInfinity](number-positiveinfinity.md), [Number.NegativeInfinity](number-negativeinfinity.md), or [Number.NaN](number-nan.md) constants specified by the currently applicable culture.

## Code example

The following example formats a floating point and an integral numeric value using the en-US culture and all the standard numeric format specifiers. This example uses two particular numeric types (`Double.Type` and `Int32.Type`), but would yield similar results for any of the other numeric base types (`Byte.Type`, `Decimal.Type`, `Int8.Type`, `Int16.Type`, `Int64.Type`, and `Single.Type`).

```powerquery-m
let
    // Display text representations of numbers for en-US culture
    culture = "en-US",

    // Output floating point values
    floating = Double.From(10761.937554),
    #"Floating results" = 
    {
        Text.Format("C: #{0}", {Number.ToText(floating, "C", culture)}),         // Displays "C: $10,761.94"
        Text.Format("E: #{0}", {Number.ToText(floating, "E03", culture)}),       // Displays "E: 1.076E+004"
        Text.Format("F: #{0}", {Number.ToText(floating, "F04", culture)}),       // Displays "F: 10761.9376"
        Text.Format("G: #{0}", {Number.ToText(floating, "G", culture)}),         // Displays "G: 10761.937554"
        Text.Format("N: #{0}", {Number.ToText(floating, "N03", culture)}),       // Displays "N: 10,761.938"
        Text.Format("P: #{0}", {Number.ToText(floating/10000, "P02", culture)})  // Displays "P: 107.62%"
    },
    
    // Output integral values
    integral = Int32.From(8395),
    #"Integral results" =
    {
        Text.Format("C: #{0}", {Number.ToText(integral, "C", culture)}),         // Displays "C: $8,395.00"
        Text.Format("D: #{0}", {Number.ToText(integral, "D6", culture)}),        // Displays "D: 008395"
        Text.Format("E: #{0}", {Number.ToText(integral, "E03", culture)}),       // Displays "E: 8.395E+003"
        Text.Format("F: #{0}", {Number.ToText(integral, "F01", culture)}),       // Displays "F: 8395.0"
        Text.Format("G: #{0}", {Number.ToText(integral, "G", culture)}),         // Displays "G: 8395"
        Text.Format("N: #{0}", {Number.ToText(integral, "N01", culture)}),       // Displays "N: 8,395.0"
        Text.Format("P: #{0}", {Number.ToText(integral/10000, "P02", culture)}), // Displays "P: 83.95%"
        Text.Format("X: 0x#{0}", {Number.ToText(integral, "X", culture)})        // Displays "X: 0x20CB"
    },
    results = #"Floating results" & #"Integral results"

in
    results
```

## Related content

- [Number type conversion](type-conversion.md#number)
- [Data Types in Power Query](/power-query/data-types)
- [Custom Numeric Format Strings](custom-numeric-format-strings.md)
