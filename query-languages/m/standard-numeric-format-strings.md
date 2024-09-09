---
title: Standard numeric format strings
description: In this article, learn to use standard numeric format strings to format common numeric types into text representations in Power Query M.
ms.date: 9/5/2024
ms.topic: reference
---

# Standard numeric format strings

Standard numeric format strings are used to format common numeric types. A standard numeric format string takes the form *`[format specifier][precision specifier]`*, where:

- *Format specifier* is a single alphabetic character that specifies the type of number format, for example, currency or percent. Any numeric format string that contains more than one alphabetic character, including white space, is interpreted as a custom numeric format string. For more information, go to [Custom numeric format strings](custom-numeric-format-strings.md).

- *Precision specifier* is an optional integer that affects the number of digits in the resulting string. <!-- Reviewers - what is the maximum precision value in Power Query M? In .NET 7 and later versions, the maximum precision value is 999,999,999. In .NET 6, the maximum precision value is <xref:System.Int32.MaxValue?displayProperty=nameWithType>. In previous .NET versions, the precision can range from 0 to 99. -->The precision specifier controls the number of digits in the string representation of a number. It doesn't round the number itself. To perform a rounding operation, use the [Number.RoundDown](number-rounddown.md), [Number.RoundUp](number-roundup.md), [Number.RoundAwayFromZero](number-roundawayfromzero.md), or [Number.RoundTowardZero](number-roundtowardzero.md) function.

  When *precision specifier* controls the number of fractional digits in the result string, the result string reflects a number that is rounded to a representable result nearest to the infinitely precise result. <!-- Reviewers - does Power Query M have an equivalent to the following? If there are two equally near representable results: -->
  <!--- **On .NET Framework and .NET Core up to .NET Core 2.0**, the runtime selects the result with the greater least significant digit (that is, using <xref:System.MidpointRounding.AwayFromZero?displayProperty=nameWithType>).
  - **On .NET Core 2.1 and later**, the runtime selects the result with an even least significant digit (that is, using <xref:System.MidpointRounding.ToEven?displayProperty=nameWithType>). -->

  > [!NOTE]
  > The precision specifier determines the number of digits in the result string. To pad a result string with leading or trailing spaces, use the [Text.PadStart](text-padstart.md) and [Text.PadEnd](text-padend.md) functions and define an *alignment component* in the `count` parameter.

Standard numeric format strings are supported by:

- Some overloads of the `ToString` method of all numeric types. For example, you can supply a numeric format string to the <xref:System.Int32.ToString%28System.String%29?displayProperty=nameWithType> and <xref:System.Int32.ToString%28System.String%2CSystem.IFormatProvider%29?displayProperty=nameWithType> methods.

- The `TryFormat` method of all numeric types, for example, <xref:System.Int32.TryFormat(System.Span{System.Char},System.Int32@,System.ReadOnlySpan{System.Char},System.IFormatProvider)?displayProperty=nameWithType> and <xref:System.Single.TryFormat(System.Span{System.Char},System.Int32@,System.ReadOnlySpan{System.Char},System.IFormatProvider)?displayProperty=nameWithType>.
<!-- don't work in Power Query M
- The .NET [composite formatting feature](composite-formatting.md), which is used by some `Write` and `WriteLine` methods of the <xref:System.Console> and <xref:System.IO.StreamWriter> classes, the <xref:System.String.Format%2A?displayProperty=nameWithType> method, and the <xref:System.Text.StringBuilder.AppendFormat%2A?displayProperty=nameWithType> method. The composite format feature allows you to include the string representation of multiple data items in a single string, to specify field width, and to align numbers in a field. For more information, see [Composite Formatting](composite-formatting.md).

- [Interpolated strings](../../csharp/language-reference/tokens/interpolated.md) in C# and Visual Basic, which provide a simplified syntax when compared to composite format strings.

> [!TIP]
> You can download the **Formatting Utility**, a .NET Core Windows Forms application that lets you apply format strings to either numeric or date and time values and displays the result string. Source code is available for [C#](/samples/dotnet/samples/windowsforms-formatting-utility-cs) and [Visual Basic](/samples/dotnet/samples/windowsforms-formatting-utility-vb). -->

## Standard format specifiers

The following table describes the standard numeric format specifiers and displays sample output produced by each format specifier. See the [Notes](#notes) section for additional information about using standard numeric format strings, and the [Code example](#code-example) section for a comprehensive illustration of their use.

> [!NOTE]
> The result of a formatted string for a specific culture might differ from the following examples. Operating system settings, user settings, environment variables, and the .NET version you're using can all affect the format. For example, starting with .NET 5, .NET tries to unify cultural formats across platforms. For more information, see [.NET globalization and ICU](../../core/extensions/globalization-icu.md).

| Format specifier | Name | Description | Examples |
|--|--|--|--|
| "B" or "b" | Binary | Result: A binary string.<br /><br /> Supported by: Integral types only (.NET 8+).<br /><br /> Precision specifier: Number of digits in the result string.<br /><br /> More information: [The Binary ("B") Format Specifier](#BFormatString). | 42 ("B")<br />-> 101010<br /><br /> 255 ("b16")<br />-> 0000000011111111 | 
| "C" or "c" | Currency | Result: A currency value.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: Defined by <xref:System.Globalization.NumberFormatInfo.CurrencyDecimalDigits%2A?displayProperty=nameWithType>.<br /><br /> More information: [The Currency ("C") Format Specifier](#CFormatString). | 123.456 ("C", en-US)<br />-> \\$123.46<br /><br /> 123.456 ("C", fr-FR)<br />-> 123,46 &euro;<br /><br /> 123.456 ("C", ja-JP)<br />-> ¥123<br /><br /> -123.456 ("C3", en-US)<br />-> (\\$123.456)<br /><br /> -123.456 ("C3", fr-FR)<br />-> -123,456 &euro;<br /><br /> -123.456 ("C3", ja-JP)<br />-> -¥123.456 |
| "D" or "d" | Decimal | Result: Integer digits with optional negative sign.<br /><br /> Supported by: Integral types only.<br /><br /> Precision specifier: Minimum number of digits.<br /><br /> Default precision specifier: Minimum number of digits required.<br /><br /> More information: [The Decimal("D") Format Specifier](#DFormatString). | 1234 ("D")<br />-> 1234<br /><br /> -1234 ("D6")<br />-> -001234 |
| "E" or "e" | Exponential (scientific) | Result: Exponential notation.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: 6.<br /><br /> More information: [The Exponential ("E") Format Specifier](#EFormatString). | 1052.0329112756 ("E", en-US)<br />-> 1.052033E+003<br /><br /> 1052.0329112756 ("e", fr-FR)<br />-> 1,052033e+003<br /><br /> -1052.0329112756 ("e2", en-US)<br />-> -1.05e+003<br /><br /> -1052.0329112756 ("E2", fr-FR)<br />-> -1,05E+003 |
| "F" or "f" | Fixed-point | Result: Integral and decimal digits with optional negative sign.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of decimal digits.<br /><br /> Default precision specifier: Defined by <xref:System.Globalization.NumberFormatInfo.NumberDecimalDigits%2A?displayProperty=nameWithType>.<br /><br /> More information: [The Fixed-Point ("F") Format Specifier](#FFormatString). | 1234.567 ("F", en-US)<br />-> 1234.57<br /><br /> 1234.567 ("F", de-DE)<br />-> 1234,57<br /><br /> 1234 ("F1", en-US)<br />-> 1234.0<br /><br /> 1234 ("F1", de-DE)<br />-> 1234,0<br /><br /> -1234.56 ("F4", en-US)<br />-> -1234.5600<br /><br /> -1234.56 ("F4", de-DE)<br />-> -1234,5600 |
| "G" or "g" | General | Result: The more compact of either fixed-point or scientific notation.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Number of significant digits.<br /><br /> Default precision specifier: Depends on numeric type.<br /><br /> More information: [The General ("G") Format Specifier](#GFormatString). | -123.456 ("G", en-US)<br />-> -123.456<br /><br /> -123.456 ("G", sv-SE)<br />-> -123,456<br /><br /> 123.4546 ("G4", en-US)<br />-> 123.5<br /><br /> 123.4546 ("G4", sv-SE)<br />-> 123,5<br /><br /> -1.234567890e-25 ("G", en-US)<br />-> -1.23456789E-25<br /><br /> -1.234567890e-25 ("G", sv-SE)<br />-> -1,23456789E-25 |
| "N" or "n" | Number | Result: Integral and decimal digits, group separators, and a decimal separator with optional negative sign.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Desired number of decimal places.<br /><br /> Default precision specifier: Defined by <xref:System.Globalization.NumberFormatInfo.NumberDecimalDigits%2A?displayProperty=nameWithType>.<br /><br /> More information: [The Numeric ("N") Format Specifier](#NFormatString). | 1234.567 ("N", en-US)<br />-> 1,234.57<br /><br /> 1234.567 ("N", ru-RU)<br />-> 1 234,57<br /><br /> 1234 ("N1", en-US)<br />-> 1,234.0<br /><br /> 1234 ("N1", ru-RU)<br />-> 1 234,0<br /><br /> -1234.56 ("N3", en-US)<br />-> -1,234.560<br /><br /> -1234.56 ("N3", ru-RU)<br />-> -1 234,560 |
| "P" or "p" | Percent | Result: Number multiplied by 100 and displayed with a percent symbol.<br /><br /> Supported by: All numeric types.<br /><br /> Precision specifier: Desired number of decimal places.<br /><br /> Default precision specifier: Defined by  <xref:System.Globalization.NumberFormatInfo.PercentDecimalDigits%2A?displayProperty=nameWithType>.<br /><br /> More information: [The Percent ("P") Format Specifier](#PFormatString). | 1 ("P", en-US)<br />-> 100.00 %<br /><br /> 1 ("P", fr-FR)<br />-> 100,00 %<br /><br /> -0.39678 ("P1", en-US)<br />-> -39.7 %<br /><br /> -0.39678 ("P1", fr-FR)<br />-> -39,7 % |
| "R" or "r" | Round-trip | Result: A string that can round-trip to an identical number.<br /><br /> Supported by: <xref:System.Single>, <xref:System.Double>, and <xref:System.Numerics.BigInteger>.<br /><br /> Note: Recommended for the <xref:System.Numerics.BigInteger> type only. For <xref:System.Double> types, use "G17"; for <xref:System.Single> types, use "G9". <br> Precision specifier: Ignored.<br /><br /> More information: [The Round-trip ("R") Format Specifier](#RFormatString). | 123456789.12345678 ("R")<br />-> 123456789.12345678<br /><br /> -1234567890.12345678 ("R")<br />-> -1234567890.1234567 |
| "X" or "x" | Hexadecimal | Result: A hexadecimal string.<br /><br /> Supported by: Integral types only.<br /><br /> Precision specifier: Number of digits in the result string.<br /><br /> More information: [The Hexadecimal ("X") Format Specifier](#XFormatString). | 255 ("X")<br />-> FF<br /><br /> -1 ("x")<br />-> ff<br /><br /> 255 ("x4")<br />-> 00ff<br /><br /> -1 ("X4")<br />-> 00FF |
| Any other single character | Unknown specifier | Result: Throws a <xref:System.FormatException> at run time. |  |

## Use standard numeric format strings

[!INCLUDE[interactive-note](~/includes/csharp-interactive-note.md)]

A standard numeric format string can be used to define the formatting of a numeric value. It can be passed to the [Number.ToText](number-totext.md) that has a `format` parameter. The following example formats a numeric value as a currency string in the current culture (in this case, the en-US culture).

```powerquery-m
value = 123.456,
result = Number.ToText(value, "C2")
// Displays $123.46
```

<!-- don't think the other methods described here work in Power Query M
- It can be supplied as the `formatString` argument in a format item used with such methods as <xref:System.String.Format%2A?displayProperty=nameWithType>, <xref:System.Console.WriteLine%2A?displayProperty=nameWithType>, and <xref:System.Text.StringBuilder.AppendFormat%2A?displayProperty=nameWithType>. For more information, see [Composite Formatting](composite-formatting.md). The following example uses a format item to insert a currency value in a string.

  [!code-cpp[Formatting.Numeric.Standard#11](../../../samples/snippets/cpp/VS_Snippets_CLR/Formatting.Numeric.Standard/cpp/standardusage1.cpp#11)]
  [!code-csharp-interactive[Formatting.Numeric.Standard#11](../../../samples/snippets/csharp/VS_Snippets_CLR/Formatting.Numeric.Standard/cs/standardusage1.cs#11)]
  [!code-vb[Formatting.Numeric.Standard#11](../../../samples/snippets/visualbasic/VS_Snippets_CLR/Formatting.Numeric.Standard/vb/standardusage1.vb#11)]

  Optionally, you can supply an `alignment` argument to specify the width of the numeric field and whether its value is right- or left-aligned. The following example left-aligns a currency value in a 28-character field, and it right-aligns a currency value in a 14-character field.

  [!code-cpp[Formatting.Numeric.Standard#12](../../../samples/snippets/cpp/VS_Snippets_CLR/Formatting.Numeric.Standard/cpp/standardusage1.cpp#12)]
  [!code-csharp-interactive[Formatting.Numeric.Standard#12](../../../samples/snippets/csharp/VS_Snippets_CLR/Formatting.Numeric.Standard/cs/standardusage1.cs#12)]
  [!code-vb[Formatting.Numeric.Standard#12](../../../samples/snippets/visualbasic/VS_Snippets_CLR/Formatting.Numeric.Standard/vb/standardusage1.vb#12)]

- It can be supplied as the `formatString` argument in an interpolated expression item of an interpolated string. For more information, see the [String interpolation](../../csharp/language-reference/tokens/interpolated.md) article in the C# reference or the [Interpolated strings](../../visual-basic/programming-guide/language-features/strings/interpolated-strings.md) article in the Visual Basic reference.
-->
The following sections provide detailed information about each of the standard numeric format strings.

<!-- Using the "B" format string returns an expression error - not used in Power Query M?
<a name="BFormatString"></a>

## Binary format specifier (B)

The binary ("B") format specifier converts a number to a string of binary digits. This format is supported only for integral types and only on .NET 8+.

The precision specifier indicates the minimum number of digits desired in the resulting string. If required, the number is padded with zeros to its left to produce the number of digits given by the precision specifier.

The result string is not affected by the formatting information of the current <xref:System.Globalization.NumberFormatInfo> object.
-->
<a name="CFormatString"></a>

## Currency format specifier (C)

The "C" (or currency) format specifier converts a number to a string that represents a currency amount. The precision specifier indicates the desired number of decimal places in the result string. If the precision specifier is omitted, the default number of decimal places to use in currency values is 2.

If the value to be formatted has more than the specified or default number of decimal places, the fractional value is rounded in the result string. If the value to the right of the number of specified decimal places is 5 or greater, the last digit in the result string is rounded away from zero.

The result string is affected by the formatting information of the current culture.<!-- Not used in Power Query The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the returned string. -->
<!--
|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.CurrencyPositivePattern%2A>|Defines the placement of the currency symbol for positive values.|
|<xref:System.Globalization.NumberFormatInfo.CurrencyNegativePattern%2A>|Defines the placement of the currency symbol for negative values, and specifies whether the negative sign is represented by parentheses or the <xref:System.Globalization.NumberFormatInfo.NegativeSign%2A> property.|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the negative sign used if <xref:System.Globalization.NumberFormatInfo.CurrencyNegativePattern%2A> indicates that parentheses are not used.|
|<xref:System.Globalization.NumberFormatInfo.CurrencySymbol%2A>|Defines the currency symbol.|
|<xref:System.Globalization.NumberFormatInfo.CurrencyDecimalDigits%2A>|Defines the default number of decimal digits in a currency value. This value can be overridden by using the precision specifier.|
|<xref:System.Globalization.NumberFormatInfo.CurrencyDecimalSeparator%2A>|Defines the string that separates integral and decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.CurrencyGroupSeparator%2A>|Defines the string that separates groups of integral numbers.|
|<xref:System.Globalization.NumberFormatInfo.CurrencyGroupSizes%2A>|Defines the number of integer digits that appear in a group.| -->

The following example formats a value with the currency format specifier:

```powerquery-m
let
    value = 12345.6789,
    result1 = Number.ToText(value, "C"),
    result2 = Number.ToText(value, "C3"),
    result3 = Number.ToText(value, "C3", "da-DK"),
    output = result1 & "#(cr,lf)" & result2 & "#(cr,lf)" & result3

in
    output

// The example displays the following output on a system whose
// current culture is English (United States):
//       $12,345.68
//       $12,345.679
//       12.345,679 kr.
```

<a name="DFormatString"></a>

## Decimal format specifier (D)

The "D" (or decimal) format specifier converts a number to a string of decimal digits (0-9), prefixed by a minus sign if the number is negative. This format is supported only for integral types.

The precision specifier indicates the minimum number of digits desired in the resulting string. If required, the number is padded with zeros to its left to produce the number of digits given by the precision specifier. If no precision specifier is specified, the default is the minimum value required to represent the integer without leading zeros.

The result string is affected by the formatting information of the current culture. <!--As the following table shows, a single property affects the formatting of the result string.
-->
<!--|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|-->

The following example formats a value with the decimal format specifier.

```powerquery-m
value = 12345,
result1 = Number.ToText(value, "D"),
// Displays 12345

result2 = Number.ToText(value, "D8"),
// Displays 00012345

value2 = -12345,
result3 = Number.ToText(value2, "D"),
// Displays -12345

result4 = Number.ToText(value2, "D8"),
// Displays -00012345
```

<a name="EFormatString"></a>

## Exponential format specifier (E)

The exponential ("E") format specifier converts a number to a string of the form "-d.ddd…E+ddd" or "-d.ddd…e+ddd", where each "d" indicates a digit (0-9). The string starts with a minus sign if the number is negative. Exactly one digit always precedes the decimal point.

The precision specifier indicates the desired number of digits after the decimal point. If the precision specifier is omitted, a default of six digits after the decimal point is used.

The case of the format specifier indicates whether to prefix the exponent with an "E" or an "e". The exponent always consists of a plus or minus sign and a minimum of three digits. The exponent is padded with zeros to meet this minimum, if required.

The result string is affected by the formatting information of the current culture. <!--The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the returned string.
-->
<!--|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative for both the coefficient and exponent.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalSeparator%2A>|Defines the string that separates the integral digit from decimal digits in the coefficient.|
|<xref:System.Globalization.NumberFormatInfo.PositiveSign%2A>|Defines the string that indicates that an exponent is positive.| -->

The following example formats a value with the exponential format specifier:

```powerquery-m
    value = 12345.6789,
    result1 = Number.ToText(value, "E"),
    // Displays 1.234568E+004

    result2 = Number.ToText(value, "E10"),
    // Displays 1.2345678900E+004

    result3 = Number.ToText(value, "e4"),
    // Displays 1.2346e+004

    result4 = Number.ToText(value, "E", "fr-FR"),
    // Displays 1,234568E+004
```

<a name="FFormatString"></a>

## Fixed-point format specifier (F)

The fixed-point ("F") format specifier converts a number to a string of the form "-ddd.ddd…" where each "d" indicates a digit (0-9). The string starts with a minus sign if the number is negative.

The precision specifier indicates the desired number of decimal places. If the precision specifier is omitted, the default number of decimal places to use in numeric values is 2.

The result string is affected by the formatting information of the current culture. <!--The following table lists the properties of the <xref:System.Globalization.NumberFormatInfo> object that control the formatting of the result string.-->
<!--
|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalSeparator%2A>|Defines the string that separates integral digits from decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalDigits%2A>|Defines the default number of decimal digits. This value can be overridden by using the precision specifier.| -->

The following example formats a double and an integer value with the fixed-point format specifier:

```powerquery-m
    integerNumber = 17843,
    result = Number.ToText(integerNumber, "F"),
    // Displays 17843.00

    integerNumber2 = -29541,
    result2 = Number.ToText(integerNumber2, "F3"),
    // Displays -29541.000

    doubleNumber = 18934.1879,
    result3 = Number.ToText(doubleNumber, "F"),
    // Displays 18934.19

    result4 = Number.ToText(doubleNumber, "F0"),
    // Displays 18934

    doubleNumber2 = -1898300.1987,
    result5 = Number.ToText(doubleNumber2, "F1"),
    // Displays -1898300.2

    result6 = Number.ToText(doubleNumber2, "F3", "es-ES"),
    // Displays -1898300,199
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
|`Single.Type`               |Smallest round-trippable number of digits to represent the number (G7 is the default)|
|`Double.Type`               |Smallest round-trippable number of digits to represent the number (G15 is the default)|
|`Decimal.Type`              |Smallest round-trippable number of digits to represent the number (G30 is the default)|

<!-- Note to reviewers - Is the default precision for the last three types correct? Double is mentioned as G15 here, but later on states G17 ensures the Double value successfully round-trips. Ditto for Single.Type and G7 in the table and G9 to successfully round-trip. Please clarify.-->

Fixed-point notation is used if the exponent that would result from expressing the number in scientific notation is greater than -5 and less than the precision specifier; otherwise, scientific notation is used. The result contains a decimal point if required, and trailing zeros after the decimal point are omitted. If the precision specifier is present and the number of significant digits in the result exceeds the specified precision, the excess trailing digits are removed by rounding.

However, if the number is a `Decimal.Type` and the precision specifier is omitted, fixed-point notation is always used and trailing zeros are preserved.

If scientific notation is used, the exponent in the result is prefixed with "E" if the format specifier is "G", or "e" if the format specifier is "g". The exponent contains a minimum of two digits. This differs from the format for scientific notation that is produced by the exponential format specifier, which includes a minimum of three digits in the exponent.

When used with a `Double.Type` value, the "G17" format specifier ensures that the original `Double.Type` value successfully round-trips. This is because `Double.Type` is an IEEE 754-2008-compliant double-precision (`binary64`) floating-point number that gives up to 17 significant digits of precision. On .NET Framework, we recommend its use instead of the ["R" format specifier](#RFormatString), since in some cases "R" fails to successfully round-trip double-precision floating point values.

When used with a `Single.Type` value, the "G9" format specifier ensures that the original `Single.Type` value successfully round-trips. This is because `Single.Type` is an IEEE 754-2008-compliant single-precision (`binary32`) floating-point number that gives up to nine significant digits of precision. For performance reasons, we recommend its use instead of the ["R" format specifier](#RFormatString).

The result string is affected by the formatting information of the current culture. <!--The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the result string. -->
<!--
|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalSeparator%2A>|Defines the string that separates integral digits from decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.PositiveSign%2A>|Defines the string that indicates that an exponent is positive.| -->

The following example formats assorted floating-point values with the general format specifier:

```powerquery-m
    number = 12345.6789,
    result = Number.ToText(number, "G"),
    // Displays 12345.6789
    result2 = Number.ToText(number, "G", "fr-FR"),
    // Displays 12345,6789

    result3 = Number.ToText(number, "G7),
    // Displays 12345.68

    number2 = .0000023,
    result4 = Number.ToText(number2, "G"),
    // Displays 2.3E-06
    result5 = Number.ToText(number2, "G", "fr-FR"),
    // Displays 2,3E-06

    number3 = .0023,
    result6 = Number.ToText(number3, "G"),
    // Displays 0.0023

    number4 = 1234,
    result7 = Number.ToText(number4, "G2")
    // Displays 1.2E+03

    number5 = Number.PI,
    result8 = Number.ToText(number5, "G5"),
    // Displays 3.1416
```

<a name="NFormatString"></a>

## Numeric format specifier (N)

The numeric ("N") format specifier converts a number to a string of the form "-d,ddd,ddd.ddd…", where "-" indicates a negative number symbol if required, "d" indicates a digit (0-9), "," indicates a group separator, and "." indicates a decimal point symbol. The precision specifier indicates the desired number of digits after the decimal point. If the precision specifier is omitted, the number of decimal places is defined by the current culture.

The result string is affected by the formatting information of the current culture. <!--The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the result string. -->
<!--
|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|
|<xref:System.Globalization.NumberFormatInfo.NumberNegativePattern%2A>|Defines the format of negative values, and specifies whether the negative sign is represented by parentheses or the <xref:System.Globalization.NumberFormatInfo.NegativeSign%2A> property.|
|<xref:System.Globalization.NumberFormatInfo.NumberGroupSizes%2A>|Defines the number of integral digits that appear between group separators.|
|<xref:System.Globalization.NumberFormatInfo.NumberGroupSeparator%2A>|Defines the string that separates groups of integral numbers.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalSeparator%2A>|Defines the string that separates integral and decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalDigits%2A>|Defines the default number of decimal digits. This value can be overridden by using a precision specifier.| -->

The following example formats assorted floating-point values with the number format specifier:

```powerquery-m
    dblValue = -12445.6789,
    result = Number.ToText(dblValue, "N"),
    // Displays -12,445.68
    result2 = Number.ToText(dblValue, "N1", "sv-SE"),
    // Displays -12 445,7

    intValue = 123456789,
    result3 = Number.ToText(intValue, "N1"),
    // Displays 123,456,789.0
```

<a name="PFormatString"></a>

## Percent format specifier (P)

The percent ("P") format specifier multiplies a number by 100 and converts it to a string that represents a percentage. The precision specifier indicates the desired number of decimal places. If the precision specifier is omitted, the default numeric precision supplied by the current culture is used.

<!--The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the returned string.

|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.PercentPositivePattern%2A>|Defines the placement of the percent symbol for positive values.|
|<xref:System.Globalization.NumberFormatInfo.PercentNegativePattern%2A>|Defines the placement of the percent symbol and the negative symbol for negative values.|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|
|<xref:System.Globalization.NumberFormatInfo.PercentSymbol%2A>|Defines the percent symbol.|
|<xref:System.Globalization.NumberFormatInfo.PercentDecimalDigits%2A>|Defines the default number of decimal digits in a percentage value. This value can be overridden by using the precision specifier.|
|<xref:System.Globalization.NumberFormatInfo.PercentDecimalSeparator%2A>|Defines the string that separates integral and decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.PercentGroupSeparator%2A>|Defines the string that separates groups of integral numbers.|
|<xref:System.Globalization.NumberFormatInfo.PercentGroupSizes%2A>|Defines the number of integer digits that appear in a group.|
-->
The following example formats floating-point values with the percent format specifier:

```powerquery-m
    number = .2468013,
    result = Number.ToText(number, "P"),
    // Displays 24.68%
    result2 = Number.ToText(number, "P", "hr-HR"),
    // Displays 24,68 %
    result3 = Number.ToText(number, "P1"),
    // Displays 24.7%
```

<a name="RFormatString"></a>

## Round-trip format specifier (R)

The round-trip ("R") format specifier attempts to ensure that a numeric value that is converted to a string is parsed back into the same numeric value. This format is supported only for the `Single.Type`, `Double.Type`, and `Decimal.Type` types.

In Power Query M, the "R" format specifier fails to successfully round-trip `Double.Type` values in some cases. For both `Double.Type` and `Single.Type` values, the "R" format specifier offers relatively poor performance. Instead, we recommend that you use the ["G17"](#GFormatString) format specifier for `Double.Type` values and the ["G9"](#GFormatString) format specifier to successfully round-trip `Single.Type` values.

<!-- Not relevant to Power Query
When a <xref:System.Numerics.BigInteger> value is formatted using this specifier, its string representation contains all the significant digits in the <xref:System.Numerics.BigInteger> value. -->

Although you can include a precision specifier, it is ignored. Round trips are given precedence over precision when using this specifier. The result string is affected by the formatting information of the current culture. <!-- Not relevant for Power Query. The following table lists the <xref:System.Globalization.NumberFormatInfo> properties that control the formatting of the result string. -->
<!--
|NumberFormatInfo property|Description|
|-------------------------------|-----------------|
|<xref:System.Globalization.NumberFormatInfo.NegativeSign%2A>|Defines the string that indicates that a number is negative.|
|<xref:System.Globalization.NumberFormatInfo.NumberDecimalSeparator%2A>|Defines the string that separates integral digits from decimal digits.|
|<xref:System.Globalization.NumberFormatInfo.PositiveSign%2A>|Defines the string that indicates that an exponent is positive.| -->

The following example formats a whole number value with the round-trip format specifier.

```powerquery-m
let
    initialValue = 92233720368547758079,
    result = Number.ToText(initialValue, "R")
in
    result

// The example dislays the following output:
//      92233720368547758079
```

> [!IMPORTANT]
> In some cases, `Double.Type` values formatted with the "R" standard numeric format string do not successfully round-trip. See the following paragraph for more information.

To work around the problem of `Double.Type` values formatted with the "R" standard numeric format string not successfully round-tripping, you can format `Double.Type` values by using the "G17" standard numeric format string. The following example uses the "R" format string with a `Double.Type` value that doesn't round-trip successfully, and also uses the "G17" format string to successfully round-trip the original value:

[!code-csharp[System.Double.ToString#5](../../../samples/snippets/csharp/VS_Snippets_CLR_System/system.Double.ToString/cs/roundtripex1.cs#RoundTrip)]
[!code-vb[System.Double.ToString#5](../../../samples/snippets/visualbasic/VS_Snippets_CLR_System/system.Double.ToString/vb/roundtripex1.vb#5)]

<a name="XFormatString"></a>

## Hexadecimal format specifier (X)

The hexadecimal ("X") format specifier converts a number to a string of hexadecimal digits. The case of the format specifier indicates whether to use uppercase or lowercase characters for hexadecimal digits that are greater than 9. For example, use "X" to produce "ABCDEF", and "x" to produce "abcdef". This format is supported only for integral types.

The precision specifier indicates the minimum number of digits desired in the resulting string. If required, the number is padded with zeros to its left to produce the number of digits given by the precision specifier.

The result string isn't affected by the formatting information of the current culture.

The following example formats values with the hexadecimal format specifier.

```powerquery-m
    value1 = 0x2045e,
    result1 = Number.ToText(value1, "x"),
    // Displays 2045e
    result2 = Number.ToText(value1, "X"),
    // Displays 2045E
    result4 = Number.ToText(value1, "X8"),
    // Displays 0002045E

    value2 = 123456789,
    result5 = Number.ToText(value2, "X"),
    // Displays 75BCD15
    result6 = number.ToText(value2, "X2"),
    // Displays 75BCD15
```

## Notes

This section contains additional information about using standard numeric format strings.

<!-- Reviewers - I don't think this control panel settings section describes anything relevant for Power Query M. However, perhaps it should be replaced with information about how a language can be set on a system to affect how culture works in Power Query M. Someone will need to supply this information. -->
### Control Panel settings

The settings in the **Regional and Language Options** item in Control Panel influence the result string produced by a formatting operation. Those settings are used to initialize the <xref:System.Globalization.NumberFormatInfo> object associated with the current culture, which provides values used to govern formatting. Computers that use different settings generate different result strings.

In addition, if the <xref:System.Globalization.CultureInfo.%23ctor%28System.String%29> constructor is used to instantiate a new <xref:System.Globalization.CultureInfo> object that represents the same culture as the current system culture, any customizations established by the **Regional and Language Options** item in Control Panel will be applied to the new <xref:System.Globalization.CultureInfo> object. You can use the <xref:System.Globalization.CultureInfo.%23ctor%28System.String%2CSystem.Boolean%29> constructor to create a <xref:System.Globalization.CultureInfo> object that does not reflect a system's customizations.

<!-- Reviewers - I don't think this section is relevant. If it is, let me know how to change it for Power Query M. -->
### NumberFormatInfo properties

Formatting is influenced by the properties of the current <xref:System.Globalization.NumberFormatInfo> object, which is provided implicitly by the current culture or explicitly by the <xref:System.IFormatProvider> parameter of the method that invokes formatting. Specify a <xref:System.Globalization.NumberFormatInfo> or <xref:System.Globalization.CultureInfo> object for that parameter.

> [!NOTE]
> For information about customizing the patterns or strings used in formatting numeric values, see the <xref:System.Globalization.NumberFormatInfo> class topic.

### Integral and floating-point numeric types

Some descriptions of standard numeric format specifiers refer to integral or floating-point numeric types. The integral numeric types are <xref:System.Byte>, <xref:System.SByte>, <xref:System.Int16>, <xref:System.Int32>, <xref:System.Int64>, <xref:System.UInt16>, <xref:System.UInt32>, <xref:System.UInt64>, and <xref:System.Numerics.BigInteger>. The floating-point numeric types are <xref:System.Decimal>, <xref:System.Half>, <xref:System.Single>, and <xref:System.Double>.

### Floating-point infinities and NaN

Regardless of the format string, if the value of a <xref:System.Half>, <xref:System.Single>, or <xref:System.Double> floating-point type is positive infinity, negative infinity, or not a number (NaN), the formatted string is the value of the respective <xref:System.Globalization.NumberFormatInfo.PositiveInfinitySymbol%2A>, <xref:System.Globalization.NumberFormatInfo.NegativeInfinitySymbol%2A>, or <xref:System.Globalization.NumberFormatInfo.NaNSymbol%2A> property that is specified by the currently applicable <xref:System.Globalization.NumberFormatInfo> object.

## Code example

The following example formats a floating point and an integral numeric value using the en-US culture and all the standard numeric format specifiers. This example uses two particular numeric types (`Double.Type` and `Int32.Type`), but would yield similar results for any of the other numeric base types (`Byte.Type`, `Decimal.Type`, `Int8.Type`, `Int16.Type`, `Int64.Type`, and `Single.Type`).

```powerquery-m
let
    // Display string representations of numbers for en-us culture
    culture = "en-US",

    // Output floating point values
    floating = Double.From(10761.937554),
    result1 = Text.Format("C: #{0}", {Number.ToText(floating, "C", culture)}),             // Displays "C: $10,761.94"
    result2 = Text.Format("E: #{0}", {Number.ToText(floating, "E03", culture)}),           // Displays "E: 1.076E+004"
    result3 = Text.Format("F: #{0}", {Number.ToText(floating, "F04", culture)}),           // Displays "F: 10761.9376"
    result4 = Text.Format("G: #{0}", {Number.ToText(floating, "G", culture)}),             // Displays "G: 10761.937554"
    result5 = Text.Format("N: #{0}", {Number.ToText(floating, "N03", culture)}),           // Displays "N: 10,761.938"
    result6 = Text.Format("P: #{0}", {Number.ToText(floating/10000, "P02", culture)}),     // Displays "P: 107.62%"
    result7 = Text.Format("R: #{0}", {Number.ToText(floating, "R", culture)}),             // Displays "R: 10761.937554"
    #"Floating results" = result1 & "#(cr,lf)" & result2 & "#(cr,lf)" &result3 & "#(cr,lf)" &result4 & "#(cr,lf)" &result5 & "#(cr,lf)" &result6 & "#(cr,lf)" & result7 & "#(cr,lf)", 
    
    // Output integral values
    integral = Int32.From(8395),
    result8 = Text.Format("C: #{0}", {Number.ToText(integral, "C", culture)}),             // Displays "C: $8,395.00"
    result9 = Text.Format("D: #{0}", {Number.ToText(integral, "D6", culture)}),            // Displays "D: 008395"
    result10 = Text.Format("E: #{0}", {Number.ToText(integral, "E03", culture)}),          // Displays "E: 8.395E+003"
    result11 = Text.Format("F: #{0}", {Number.ToText(integral, "F01", culture)}),          // Displays "F: 8395.0"
    result12 = Text.Format("G: #{0}", {Number.ToText(integral, "G", culture)}),            // Displays "G: 8395"
    result13 = Text.Format("N: #{0}", {Number.ToText(integral, "N01", culture)}),          // Displays "N: 8,395.0"
    result14 = Text.Format("P: #{0}", {Number.ToText(integral/10000, "P02", culture)}),    // Displays "P: 83.95 %"
    result15 = Text.Format("X: 0x#{0}", {Number.ToText(integral, "X", culture)}),          // Displays "X: 0x20CB"
    #"Integral results" = result8 & "#(cr,lf)" & result9 & "#(cr,lf)" &result10 & "#(cr,lf)" &result11 & "#(cr,lf)" &result12 & "#(cr,lf)" &result13 & "#(cr,lf)" & result14 & "#(cr,lf)" & result15,
    results = #"Floating results" & #"Integral results"

in
    results
```

## Related content

- [Custom Numeric Format Strings](custom-numeric-format-strings.md)
- [Formatting Types](formatting-types.md)
- [How to: Pad a Number with Leading Zeros](how-to-pad-a-number-with-leading-zeros.md)
- [Composite Formatting](composite-formatting.md)
