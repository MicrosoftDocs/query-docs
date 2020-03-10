---
title: M Language lexical structure | Microsoft Docs
description: Use the "create from blank" option to create a custom connector for Power Automate and Power Apps
author: dougklopfenstein

ms.service: powerquery

ms.topic: article
ms.date: 02/25/2020
ms.author: v-douklo
---


# Lexical Structure

## Documents

An M _document_ is an ordered sequence of Unicode characters. M allows different classes of Unicode characters in different parts of an M document. For information on Unicode character classes, see _The Unicode Standard, Version 3.0_, section 4.5.

A document either consists of exactly one _expression_ or of groups of _definitions_ organized into _sections_. Sections are described in detail in Chapter 10. Conceptually speaking, the following steps are used to read an expression from a document:

1. The document is decoded according to its character encoding scheme into a sequence of Unicode characters.

2. Lexical analysis is performed, thereby translating the stream of Unicode characters into a stream of tokens. The remaining subsections of this section cover lexical analysis.

3. Syntactic analysis is performed, thereby translating the stream of tokens into a form that can be evaluated. This process is covered in subsequent sections.

## Grammar conventions

The lexical and syntactic grammars are presented using _grammar productions_. Each grammar production defines a non-terminal symbol and the possible expansions of that nonterminal symbol into sequences of non-terminal or terminal symbols. In grammar productions, _non-terminal+ symbols are shown in italic type, and _terminal_ symbols are shown in a fixed-width font.

The first line of a grammar production is the name of the non-terminal symbol being defined, followed by a colon. Each successive indented line contains a possible expansion of the nonterminal given as a sequence of non-terminal or terminal symbols. For example, the production:

_if-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if` _if-condition_ `then` _true-expression_  `else`  _false-expression_

defines an _if-expression_ to consist of the token `if`,  followed by an _if-condition_, followed by the token `then`, followed by a _true-expression_, followed by the token `else`, followed by a _false-expression_.

When there is more than one possible expansion of a non-terminal symbol, the alternatives are listed on separate lines. For example, the production:

_variable-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable-list , variable_


defines a _variable-list_ to either consist of a _variable_ or consist of a _variable-list_ followed by a _variable_. In other words, the definition is recursive and specifies that a variable list consists of one or more variables, separated by commas.

A subscripted suffix "<sub>opt</sub>" is used to indicate an optional symbol. The production:

_field-specification:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional`_<sub>opt</sub> identifier = field-type_
</code>

is shorthand for:

_field-specification:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier = field-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional identifier = field-type_

and defines a _field-specification_ to optionally begin with the terminal symbol `optional` followed by an _identifier_, the terminal symbol `=`, and a _field-type_.

Alternatives are normally listed on separate lines, though in cases where there are many alternatives, the phrase "one of" may precede a list of expansions given on a single line. This is simply shorthand for listing each of the alternatives on a separate line. For example, the production:

_decimal-digit:_  one of<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9`

is shorthand for:

_decimal-digit:_ <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`1`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`2`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`3`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`4`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`5`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`6`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`7`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`8`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`9`<br/>

## Lexical Analysis

The _lexical-unit_ production defines the lexical grammar for an M document. Every valid M document conforms to this grammar.

_lexical-unit:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-elements<sub>opt</sub><br/>
lexical-elements:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-element<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-element<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-elements<br/> 
lexical-element:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;whitespace<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token comment_

At the lexical level, an M document consists of a stream of _whitespace_, _comment_, and _token_ elements. Each of these productions is covered in the following sections. Only _token_ elements are significant in the syntactic grammar.

## Whitespace

Whitespace is used to separate comments and tokens within an M document. Whitespace includes the space character (which is part of Unicode class Zs), as well as horizontal and vertical tab, form feed, and newline character sequences. Newline character sequences include carriage return, line feed, carriage return followed by line feed, next line, and paragraph separator characters.

_whitespace_:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character with Unicode class Zs<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Horizontal tab character (`U+0009`)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vertical tab character (`U+000B`)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form feed character (`U+000C`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`) followed by line feed character (`U+000A`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_new-line-character_<br/>
_new-line-character_:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line feed character (`U+000A`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next line character (`U+0085`)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line separator character (`U+2028`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paragraph separator character (`U+2029`)

For compatibility with source code editing tools that add end-of-file markers, and to enable a document to be viewed as a sequence of properly terminated lines, the following transformations are applied, in order, to an M document:

* If the last character of the document is a Control-Z character (`U+001A`), this character is deleted.

* A carriage-return character (`U+000D`) is added to the end of the document if that document is non-empty and if the last character of the document is not a carriage return (`U+000D`), a line feed (`U+000A`), a line separator (`U+2028`), or a paragraph separator (`U+2029`).

## Comments

Two forms of comments are supported: single-line comments and delimited comments. _Single-line comments_ start with the characters `//` and extend to the end of the source line. _Delimited comments_ start with the characters `/*` and end with the characters `*/`.

Delimited comments may span multiple lines.


_comment:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-line-comment<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimited-comment<br/>
single-line-comment:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`//` _single-line-comment-characters<sub>opt</sub><br/>
single-line-comment-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-line-comment-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-line-comment-characters  single-line-comment-character<br/>
single-line-comment-character:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except a _new-line-character<br/>
delimited-comment:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/*` _delimited-comment-text<sub>opt</sub>  asterisks_  `/`<br/>
_delimited-comment-text:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimited-comment-section<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimited-comment-text  delimited-comment-section</br> 
delimited-comment-section:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_asterisks<sub>opt</sub>  not-slash-or-asterisk<br/>
asterisks:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`*`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`*`  _asterisks<br/>
not-slash-or-asterisk:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except `*` or `/` 

Comments do not nest. The character sequences `/*` and `*/` have no special meaning within a single-line comment, and the character sequences `//` and `/*` have no special meaning within a delimited comment.

Comments are not processed within text literals. The example

```
/* Hello, world 
*/ 
    "Hello, world"
```

includes a delimited comment.

The example

```
// Hello, world 
// 
"Hello, world" // This is an example of a text literal
```

shows several single-line comments.

## Tokens

A _token_ is an identifier, keyword, literal, operator, or punctuator. Whitespace and comments are used to separate tokens, but are not considered tokens.

_token:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operator-or-punctuator_

### Character Escape Sequences

M text values can contain arbitrary Unicode characters. Text literals, however, are limited to graphic characters and require the use of _escape sequences_ for non-graphic characters. For example, to include a carriage-return, linefeed, or tab character in a text literal, the `#(cr)`, `#(lf)`, and `#(tab)` escape sequences can be used, respectively. To embed the escapesequence start characters `#(` in a text literal, the `#` itself needs to be escaped:

```
#(#)(
```

Escape sequences can also contain short (four hex digits) or long (eight hex digits) Unicode code-point values. The following three escape sequences are therefore equivalent:

```
#(000D)     // short Unicode hexadecimal value 
#(0000000D) // long Unicode hexadecimal value 
#(cr)       // compact escape shorthand for carriage return
```

Multiple escape codes can be included in a single escape sequence, separated by commas; the following two sequences are thus equivalent:

```
#(cr,lf) 
#(cr)#(lf)
```

The following describes the standard mechanism of character escaping in an M document.

_character-escape-sequence:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#(`  _escape-sequence-list_  `)`<br/> _escape-sequence-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-escape-sequence  ,  escape-sequence-list<br/>
single-escape-sequence:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;long-unicode-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short-unicode-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;control-character-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;escape-escape<br/> 
long-unicode-escape-sequence:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit  hex-digit<br/> 
short-unicode-escape-sequence:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex-digit  hex-digit  hex-digit  hex-digit<br/>
control-character-escape-sequence:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;control-character<br/> 
control-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cr`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`lf`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`tab`<br/> 
_escape-escape:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#`

### Literals

A _literal_ is a source code representation of a value.

_literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;null-literal_

#### Null literals

The null literal is used to write the `null` value. The `null` value represents an absent value.

_null-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`null`

#### Logical literals

A logical literal is used to write the values `true` and `false` and produces a logical value.

_logical-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`true`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`false`

#### Number literals

A number literal is used to write a numeric value and produces a number value.

_number-literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-number-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hexadecimal-number-literal<br/>
decimal-number-literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digits_  `.`  _decimal-digits  exponent-part<sub>opt</sub>_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  _decimal-digits  exponent-part<sub>opt</sub><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digits  exponent-part<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digits<br/> 
decimal-digits:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit  decimal-digits<br/> 
decimal-digit:_  one of<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9`<br/>
_exponent-part:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`e` _sign<sub>opt</sub>  decimal-digits_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`E` _sign<sub>opt</sub>  decimal-digits<br/> sign:_ one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+  -`<br/>
_hexadecimal-number-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0x` _hex-digits_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0X` _hex-digits<br/>
hex-digits:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex-digit<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex-digit hex-digits<br/>
hex-digit:_  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  a  b  c  d e  f`

A number can be specified in hexadecimal format by preceding the _hex-digits_ with the characters `0x`. For example:

```
0xff // 255
```

Note that if a decimal point is included in a number literal, then it must have at least one digit following it. For example, `1.3` is a number literal but `1.` and `1.e3` are not.

#### Text literals

A text literal is used to write a sequence of Unicode characters and produces a text value.

_text-literal:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"`  _text-literal-characters<sub>opt</sub>_  `"`<br/>
_text-literal-characters:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal-character text-literal-characters<br/>
text-literal-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-text-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;character-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;double-quote-escape-sequence<br/> 
single-text-character:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`)<br/>
_double-quote-escape-sequence:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`""` (`U+0022`, `U+0022`)

To include quotes in a text value, the quote mark is repeated, as follows:

```
"The ""quoted"" text" // The "quoted" text
```

The [_character-escape-sequence_](#character-escape-sequences) production can be used to write characters in text values without having to directly encode them as Unicode characters in the document. For example, a carriage return and line feed can be written in a text value as:

```
"Hello world#(cr,lf)"
```

### Identifiers

An _identifier_ is a name used to refer to a value. Identifiers can either be regular identifiers or quoted identifiers.

_identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regular-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quoted-identifier<br/>
regular-identifier:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available-identifier  dot-character  regular-identifier<br/>
available-identifier:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A _keyword-or-identifier_ that is not a _keyword<br/>
keyword-or-identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-start-character  identifier-part-characters<sub>opt</sub><br/> 
identifier-start-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underscore-character<br/>
identifier-part-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-part-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-part-character  identifier-part-characters<br/>
identifier-part-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underscore-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connecting-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;combining-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;formatting-character<br/> 
dot-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  (`U+002E`)<br/>
_underscore-character:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`_`  (`U+005F`)<br/>
_letter-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nl<br/>
_combining-character:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Mn or Mc<br/>
_decimal-digit-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Nd<br/>
_connecting-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Pc<br/> 
_formatting-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Cf

A _quoted-identifier_ can be used to allow any sequence of zero or more Unicode characters to be used as an identifier, including keywords, whitespace, comments, operators and punctuators.

_quoted-identifier:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#"`   _text-literal-characters<sub>opt</sub>_   `"`

Note that escape sequences and double-quotes to escape quotes can be used in a _quoted identifier_, just as in a _text-literal_.

The following example uses identifier quoting for names containing a space character:

```
[ 
    #"1998 Sales" = 1000, 
    #"1999 Sales" = 1100, 
    #"Total Sales" = #"1998 Sales" + #"1999 Sales"
]
```

The following example uses identifier quoting to include the `+` operator in an identifier:

```
[ 
    #"A + B" = A + B, 
    A = 1, 
    B = 2 
]
```

#### Generalized Identifiers

There are two places in M where no ambiguities are introduced by identifiers that contain blanks or that are otherwise keywords or number literals. These places are the names of record fields in a record literal and in a field access operator (`[ ]`) There, M allows such identifiers without having to use quoted identifiers.

```
[ 
    Data = [ Base Line = 100, Rate = 1.8 ], 
    Progression = Data[Base Line] * Data[Rate]
]
```

The identifiers used to name and access fields are referred to as _generalized identifiers_ and defined as follows:

_generalized-identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier-part<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier_ separated only by blanks (`U+0020`)<br/> _generalized-identifier-part<br/>
generalized-identifier-part:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier-segment<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit-character generalized-identifier-segment<br/>
generalized-identifier-segment:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword-or-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword-or-identifier  dot-character  keyword-or-identifier_

### Keywords

A _keyword_ is an identifier-like sequence of characters that is reserved, and cannot be used as an identifier except when using the [identifier-quoting mechanism](#identifiers) or where a [generalized identifier is allowed](#generalized-identifiers).

<em>keyword:</em>  one of `and as each else error false if in is let meta not otherwise or`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` section shared then true try type #binary #date #datetime`<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#datetimezone #duration #infinity #nan #sections #shared #table #time`

### Operators and punctuators

There are several kinds of operators and punctuators. Operators are used in expressions to describe operations involving one or more operands. For example, the expression `a + b` uses the `+` operator to add the two operands `a` and `b`. Punctuators are for grouping and separating.

_operator-or-punctuator:_  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`, ; = < <= > >= <> + - * / & ( ) [ ] { } @ ! ? => .. ...`

