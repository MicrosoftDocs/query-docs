---
title: "Custom numeric format strings"
description: Learn how to create a custom numeric format string to format numeric data in .NET. A custom numeric format string has one or more custom numeric specifiers.
ms.date: 9/20/2024
ms.topic: reference
---
# Custom numeric format strings

You can create a custom numeric format string, which consists of one or more custom numeric specifiers, to define how to format numeric data. A custom numeric format string is any format string that isn't a [standard numeric format string](standard-numeric-format-strings.md).

<a name="table"></a> The following table describes the custom numeric format specifiers and displays sample output produced by each format specifier. Go to the [Notes](#NotesCustomFormatting) section for additional information about using custom numeric format strings, and the [Example](#example) section for a comprehensive illustration of their use.

|Format specifier|Name|Description|Examples|
|----------------------|----------|-----------------|--------------|
|"0"|Zero placeholder|Replaces the zero with the corresponding digit if one is present; otherwise, zero appears in the result string.<br /><br /> More information: [The "0" Custom Specifier](#Specifier0).|1234.5678 ("00000") -> 01235<br /><br /> 0.45678 ("0.00", en-US) -> 0.46<br /><br /> 0.45678 ("0.00", fr-FR) -> 0,46|
|"#"|Digit placeholder|Replaces the "#" symbol with the corresponding digit if one is present; otherwise, no digit appears in the result string.<br /><br /> Note that no digit appears in the result string if the corresponding digit in the input string is a non-significant 0. For example, 0003 ("####") -> 3.<br /><br /> More information: [The "#" Custom Specifier](#SpecifierD).|1234.5678 ("#####") -> 1235<br /><br /> 0.45678 ("#.##", en-US) -> .46<br /><br /> 0.45678 ("#.##", fr-FR) -> ,46|
|"."|Decimal point|Determines the location of the decimal separator in the result string.<br /><br /> More information: [The "." Custom Specifier](#SpecifierPt).|0.45678 ("0.00", en-US) -> 0.46<br /><br /> 0.45678 ("0.00", fr-FR) -> 0,46|
|","|Group separator and number scaling|Serves as both a group separator and a number scaling specifier. As a group separator, it inserts a localized group separator character between each group. As a number scaling specifier, it divides a number by 1000 for each comma specified.<br /><br /> More information: [The "," Custom Specifier](#SpecifierTh).|Group separator specifier:<br /><br /> 2147483647 ("##,#", en-US) -> 2,147,483,647<br /><br /> 2147483647 ("##,#", es-ES) -> 2.147.483.647<br /><br /> Scaling specifier:<br /><br /> 2147483647 ("#,#,,", en-US) -> 2,147<br /><br /> 2147483647 ("#,#,,", es-ES) -> 2.147|
|"%"|Percentage placeholder|Multiplies a number by 100 and inserts a localized percentage symbol in the result string.<br /><br /> More information: [The "%" Custom Specifier](#SpecifierPct).|0.3697 ("%#0.00", en-US) -> %36.97<br /><br /> 0.3697 ("%#0.00", el-GR) -> %36,97<br /><br /> 0.3697 ("##.0 %", en-US) -> 37.0 %<br /><br /> 0.3697 ("##.0 %", el-GR) -> 37,0 %|
|"‰"|Per mille placeholder|Multiplies a number by 1000 and inserts a localized per mille symbol in the result string.<br /><br /> More information: [The "‰" Custom Specifier](#SpecifierPerMille).|0.03697 ("#0.00‰", en-US) -> 36.97‰<br /><br /> 0.03697 ("#0.00‰", ru-RU) -> 36,97‰|
|"E0"<br /><br /> "E+0"<br /><br /> "E-0"<br /><br /> "e0"<br /><br /> "e+0"<br /><br /> "e-0"|Exponential notation|If followed by at least one 0 (zero), formats the result using exponential notation. The case of "E" or "e" indicates the case of the exponent symbol in the result string. The number of zeros following the "E" or "e" character determines the minimum number of digits in the exponent. A plus sign (+) indicates that a sign character always precedes the exponent. A minus sign (-) indicates that a sign character precedes only negative exponents.<br /><br /> More information: [The "E" and "e" Custom Specifiers](#SpecifierExponent).|987654 ("#0.0e0") -> 98.8e4<br /><br /> 1503.92311 ("0.0##e+00") -> 1.504e+03<br /><br /> 1.8901385E-16 ("0.0e+00") -> 1.9e-16|
|"\\"|Escape character|Causes the next character to be interpreted as a literal rather than as a custom format specifier.<br /><br /> More information: [The "\\" Escape Character](#SpecifierEscape).|987654 ("\\###00\\#") -> #987654#|
|'*string*'<br /><br /> "*string*"|Literal string delimiter|Indicates that the enclosed characters should be copied to the result string unchanged.<br/><br/>More information: [Character literals](#character-literals).|68 ("# 'degrees'") -> 68 degrees<br /><br /> 68 ("#' degrees'") -> 68 degrees|
|;|Section separator|Defines sections with separate format strings for positive, negative, and zero numbers.<br /><br /> More information: [The ";" Section Separator](#SectionSeparator).|12.345 ("#0.0#;(#0.0#);-\0-") -> 12.35<br /><br /> 0 ("#0.0#;(#0.0#);-\0-") -> -0-<br /><br /> -12.345 ("#0.0#;(#0.0#);-\0-") -> (12.35)<br /><br /> 12.345 ("#0.0#;(#0.0#)") -> 12.35<br /><br /> 0 ("#0.0#;(#0.0#)") -> 0.0<br /><br /> -12.345 ("#0.0#;(#0.0#)") -> (12.35)|
|Other|All other characters|The character is copied to the result string unchanged.<br/><br/>More information: [Character literals](#character-literals).|68 ("# °") -> 68 °|

The following sections provide detailed information about each of the custom numeric format specifiers.

<a name="Specifier0"></a>

## The "0" custom specifier

The "0" custom format specifier serves as a zero-placeholder symbol. If the value that is being formatted has a digit in the position where the zero appears in the format string, that digit is copied to the result string; otherwise, a zero appears in the result string. The position of the leftmost zero before the decimal point and the rightmost zero after the decimal point determines the range of digits that are always present in the result string.

The "00" specifier causes the value to be rounded to the nearest digit preceding the decimal, where rounding away from zero is always used. For example, formatting 34.5 with "00" would result in the value 35.

The following example displays several values that are formatted by using custom format strings that include zero placeholders.

```powerquery-m
let
    Source =
    {
        Number.ToText(123, "00000"),
        // Displays 00123

        Number.ToText(1.2, "0.00"),
        // Displays 1.20

        Number.ToText(1.2, "00.00"),
        // Displays 01.20

        Number.ToText(1.2, "00.00", "da-DK"),
        // Displays 01,20

        Number.ToText(.56, "0.0"),
        // Displays 0.6

        Number.ToText(1234567890, "0,0"),
        // Displays 1,234,567,890

        Number.ToText(1234567890, "0,0", "el-GR"),
        // Displays 1.234.567.890

        Number.ToText(1234567890.123456, "0,0.0"),
        // Displays 1,234,567,890.1

        Number.ToText(1234.567890, "0,0.00")
        // Displays 1,234.57
    }
in
    Source
```

[Back to table](#table)

<a name="SpecifierD"></a>

## The "#" custom specifier

The "#" custom format specifier serves as a digit-placeholder symbol. If the value that is being formatted has a digit in the position where the "#" symbol appears in the format string, that digit is copied to the result string. Otherwise, nothing is stored in that position in the result string.

Note that this specifier never displays a zero that is not a significant digit, even if zero is the only digit in the string. It will display zero only if it is a significant digit in the number that is being displayed.

The "##" format string causes the value to be rounded to the nearest digit preceding the decimal, where rounding away from zero is always used. For example, formatting 34.5 with "##" would result in the value 35.

The following example displays several values that are formatted by using custom format strings that include digit placeholders.

```powerquery-m
let
    Source =
    {
        Number.ToText(1.2, "#.##"),
        // Displays 1.2

        Number.ToText(123, "#####"),
        // Displays 123

        Number.ToText(123456, "[##-##-##]"),
        // Displays [12-34-56]

        Number.ToText(1234567890, "#"),
        // Displays 1234567890

        Number.ToText(1234567890, "(###) ###-####")
        // Displays (123) 456-7890
    }
in
    Source
```

To return a result string in which absent digits or leading zeroes are replaced by spaces, use the [Text.PadStart](text-padstart.md) and specify a field width, as the following example illustrates.

```powerquery-m
let
   Source = Text.Format("The value is: '#{0}'", {Text.PadStart(Number.ToText(.324, "#.###"), 5)})
in
   Source

// The example displays the following output if the current culture
// is en-US:
//      The value is: ' .324'
```

[Back to table](#table)

<a name="SpecifierPt"></a>

## The "." custom specifier

The "." custom format specifier inserts a localized decimal separator into the result string. The first period in the format string determines the location of the decimal separator in the formatted value; any additional periods are ignored. If the format specifier ends with a "." only the significant digits are formatted into the result string.

The character that is used as the decimal separator in the result string is not always a period; it is determined by the culture that controls formatting.

The following example uses the "." format specifier to define the location of the decimal point in several result strings.

```powerquery-m
let
    Source =
    {
        Number.ToText(1.2, "0.00"),
        // Displays 1.20

        Number.ToText(1.2, "00.00"),
        // Displays 01.20

        Number.ToText(1.2, "00.00", "da-DK"),
        // Displays 01,20

        Number.ToText(.086, "#0.##%"),
        // Displays 8.6%

        Number.ToText(Double.From(86000), "0.###E+0")
        // Displays 8.6E+4
    }
in
    Source
```

[Back to table](#table)

<a name="SpecifierTh"></a>

## The "," custom specifier

The "," character serves as both a group separator and a number scaling specifier.

- Group separator: If one or more commas are specified between two digit placeholders (0 or #) that format the integral digits of a number, a group separator character is inserted between each number group in the integral part of the output.

  The culture determines the character used as the number group separator and the size of each number group. For example, if the string "#,#" and the invariant culture are used to format the number 1000, the output is "1,000".

- Number scaling specifier: If one or more commas are specified immediately to the left of the explicit or implicit decimal point, the number to be formatted is divided by 1000 for each comma. For example, if the string "0,," is used to format the number 100 million, the output is "100".

You can use group separator and number scaling specifiers in the same format string. For example, if the string "#,0,," and the invariant culture are used to format the number one billion, the output is "1,000".

The following example illustrates the use of the comma as a group separator.

```powerquery-m
let
    Source =
    {
        Number.ToText(1234567890, "#,#"),
        // Displays 1,234,567,890

        Number.ToText(1234567890, "#,##0,,")
        // Displays, 1,235
    }
in
    Source
```

The following example illustrates the use of the comma as a specifier for number scaling.

```powerquery-m
let
    Source =
    {
        Number.ToText(1234567890, "#,,"),
        // Displays 1235

        Number.ToText(1234567890, "#,,,"),
        // Displays 1

        Number.ToText(1234567890, "#,##0,,")
        // Displays 1,235
    }
in
    Source
```

[Back to table](#table)

<a name="SpecifierPct"></a>

## The "%" custom specifier

A percent sign (%) in a format string causes a number to be multiplied by 100 before it is formatted. The localized percent symbol is inserted in the number at the location where the % appears in the format string. The percent character used is defined by the culture.

The following example defines a custom format string that includes the "%" custom specifier.

```powerquery-m
let
    Source = Number.ToText(.086, "#0.##%")
    // Displays 8.6%
in
    Source
```

[Back to table](#table)

<a name="SpecifierPerMille"></a>

## The "‰" custom specifier

A per mille character (‰ or \u2030) in a format string causes a number to be multiplied by 1000 before it is formatted. The appropriate per mille symbol is inserted in the returned string at the location where the ‰ symbol appears in the format string. The per mille character used is defined by the culture, which provides culture-specific formatting information.

The following example defines a custom format string that includes the "‰" custom specifier.

```powerquery-m
let
    Source = Number.ToText(.00354, "#0.##" & Character.FromNumber(0x2030))
    // Displays 3.54‰
in
    Source
```

[Back to table](#table)

<a name="SpecifierExponent"></a>

## The "E" and "e" custom specifiers

If any of the strings "E", "E+", "E-", "e", "e+", or "e-" are present in the format string and are followed immediately by at least one zero, the number is formatted by using scientific notation with an "E" or "e" inserted between the number and the exponent. The number of zeros following the scientific notation indicator determines the minimum number of digits to output for the exponent. The "E+" and "e+" formats indicate that a plus sign or minus sign should always precede the exponent. The "E", "E-", "e", or "e-" formats indicate that a sign character should precede only negative exponents.

The following example formats several numeric values using the specifiers for scientific notation.

```powerquery-m
let
    Source =
    {
        Number.ToText(86000, "0.###E+0"),
        // Displays 8.6E+4

        Number.ToText(86000, "0.###E+000"),
        // Displays 8.6E+004

        Number.ToText(86000, "0.###E-000"),
        // Displays 8.6E004
    }
in
    Source
```

[Back to table](#table)

<a name="SpecifierEscape"></a>

## The "\\" escape character

The "#", "0", ".", ",", "%", and "‰" symbols in a format string are interpreted as format specifiers rather than as literal characters. Depending on their position in a custom format string, the uppercase and lowercase "E" as well as the + and - symbols may also be interpreted as format specifiers.

To prevent a character from being interpreted as a format specifier, you can precede it with a backslash, which is the escape character. The escape character signifies that the following character is a character literal that should be included in the result string unchanged.

To include a backslash in a result string, you must escape it with another backslash (`\\`).

The following example uses the escape character to prevent the formatting operation from interpreting the "#", "0", and "\\" characters as either escape characters or format specifiers. The C# examples uses an additional backslash to ensure that a backslash is interpreted as a literal character.

```powerquery-m
let
    Source =
    {
        Number.ToText(123, "\#\#\# ##0 dollars and \0\0 cents \#\#\#"),
        // Displays ### 123 dollars and 00 cents ###

        Number.ToText(123, """###"" ##0 dollars and ""00"" cents ""###"""),
        // Displays ### 123 dollars and 00 cents ###

        Number.ToText(123, "\\\\\\ ##0 dollars and \0\0 cents \\\\\\"),
        // Displays \\\ 123 dollars and 00 cents \\\

        Number.ToText(123, """\\\"" ##0 dollars and ""00"" cents ""\\\""")
        // Displays \\\ 123 dollars and 00 cents \\\
    }
in
    Source
```

[Back to table](#table)

<a name="SectionSeparator"></a>

## The ";" section separator

The semicolon (;) is a conditional format specifier that applies different formatting to a number depending on whether its value is positive, negative, or zero. To produce this behavior, a custom format string can contain up to three sections separated by semicolons. These sections are described in the following table.

|Number of sections|Description|
|------------------------|-----------------|
|One section|The format string applies to all values.|
|Two sections|The first section applies to positive values and zeros, and the second section applies to negative values.<br /><br /> If the number to be formatted is negative, but becomes zero after rounding according to the format in the second section, the resulting zero is formatted according to the first section.|
|Three sections|The first section applies to positive values, the second section applies to negative values, and the third section applies to zeros.<br /><br /> The second section can be left empty (by having nothing between the semicolons), in which case the first section applies to all nonzero values.<br /><br /> If the number to be formatted is nonzero, but becomes zero after rounding according to the format in the first or second section, the resulting zero is formatted according to the third section.|

Section separators ignore any preexisting formatting associated with a number when the final value is formatted. For example, negative values are always displayed without a minus sign when section separators are used. If you want the final formatted value to have a minus sign, you should explicitly include the minus sign as part of the custom format specifier.

The following example uses the ";" format specifier to format positive, negative, and zero numbers differently.

```powerquery-m
let
    Source =
    {
        Number.ToText(1234, "##;(##)"),
        // Displays 1234

        Number.ToText(-1234, "##;(##)"),
        // Displays (1234)

        Number.ToText(0, "##;(##);**Zero**"),
        // Displays **Zero**
    }
in
    Source
```

[Back to table](#table)

## Character literals

Format specifiers that appear in a custom numeric format string are always interpreted as formatting characters and never as literal characters. This includes the following characters:

- [0](#Specifier0)
- [\#](#SpecifierD)
- [%](#SpecifierPct)
- [‰](#SpecifierPerMille)
- '
- [\\](#SpecifierEscape)
- [.](#SpecifierPt)
- [,](#SpecifierTh)
- [E or e](#SpecifierExponent), depending on its position in the format string.

All other characters are always interpreted as character literals and, in a formatting operation, are included in the result string unchanged.  In a parsing operation, they must match the characters in the input string exactly; the comparison is case-sensitive.

The following example illustrates one common use of literal character units (in this case, thousands):

```powerquery-m
let
    Source = Number.ToText(123.8, "#,##0.0K")
    // Displays 123.8K
in
    Source
```

There are two ways to indicate that characters are to be interpreted as literal characters and not as formatting characters, so that they can be included in a result string or successfully parsed in an input string:

- By escaping a formatting character. For more information, go to [The "\\" escape character](#SpecifierEscape).

- By enclosing the entire literal string in quotation apostrophes.

The following example uses both approaches to include reserved characters in a custom numeric format string.

```powerquery-m
let
    Source =
    {
        Number.ToText(9.3, "##.0\%"),
        // Displays 9.3%

        Number.ToText(9.3, "\'##\'"),
        // Displays '9'

        Number.ToText(9.3, "\\##\\"),
        // Displays \9\

        Number.ToText(9.3, "##.0'%'"),
        // Displays 9.3%

        Number.ToText(9.3, "'\'##'\'")
        // Displays \9\
    }
in
    Source
```

<a name="NotesCustomFormatting"></a>

## Notes

### How culture affects numeric format strings

For information on how culture affects numeric format strings, go to [How culture affects numeric format strings](standard-numeric-format-strings.md#how-culture-affects-numeric-format-strings).

### Floating-Point infinities and NaN

Regardless of the format string, if the value of a `Decimal.Type`, `Single.Type` or `Double.Type` floating-point type is positive infinity, negative infinity, or not a number (NaN), the formatted string is the value of the respective [Number.PositiveInfinity](number-positiveinfinity.md), [Number.NegativeInfinity](number-negativeinfinity.md), or [Number.NaN](number-nan.md) constants specified by the currently applicable culture.

### Rounding and fixed-point format strings

For fixed-point format strings (that is, format strings that don't contain scientific notation format characters), numbers are rounded to as many decimal places as there are digit placeholders to the right of the decimal point. If the format string doesn't contain a decimal point, the number is rounded to the nearest integer. If the number has more digits than there are digit placeholders to the left of the decimal point, the extra digits are copied to the result string immediately before the first digit placeholder.

[Back to table](#table)

<a name="example"></a>

## Example

The following example demonstrates two custom numeric format strings. In both cases, the digit placeholder (`#`) displays the numeric data, and all other characters are copied to the result string.

```powerquery-m
let
    Source =
    {
        Number.ToText(1234567890, "(###) ###-####"),
        // Displays (123) 456-7890

        Number.ToText(42, "My Number = #")
        // Displays My number = 42
    }
in
    Source
```

[Back to table](#table)

## Related content

- [Number type conversion](type-conversion.md#number)
- [Data Types in Power Query](/power-query/data-types)
- [Standard Numeric Format Strings](standard-numeric-format-strings.md)
