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

```
if-expression: if if-condition  then true-expression  else  false-expression
```

defines an _if-expression_ to consist of the token `if`,  followed by an _if-condition_, followed by the token `then`, followed by a _true-expression_, followed by the token `else`, followed by a _false-expression_.

When there is more than one possible expansion of a non-terminal symbol, the alternatives are listed on separate lines. For example, the production:

```
variable-list: variable
    variable-list , variable
```

defines a _variable-list_ to either consist of a _variable_ or consist of a _variable-list_ followed by a _variable_. In other words, the definition is recursive and specifies that a variable list consists of one or more variables, separated by commas.

A subscripted suffix "<sub>opt</sub>" is used to indicate an optional symbol. The production:

<code>
field-specification:<br/>
optional<sub>opt</sub> identifier = field-type
</code>

is shorthand for:

```
field-specification: 
    identifier = field-type
    optional identifier = field-type
```

and defines a _field-specification_ to optionally begin with the terminal symbol `optional` followed by an _identifier_, the terminal symbol `=`, and a _field-type_.

Alternatives are normally listed on separate lines, though in cases where there are many alternatives, the phrase "one of" may precede a list of expansions given on a single line. This is simply shorthand for listing each of the alternatives on a separate line. For example, the production:

```
decimal-digit:  one of 
       0  1  2  3  4  5  6  7  8  9
```

is shorthand for:

```
decimal-digit: 
                0 
                1 
                2 
                3 
                4 
                5 
                6 
                7 
                8 
                9
```

## Lexical Analysis

The _lexical-unit_ production defines the lexical grammar for an M document. Every valid M document conforms to this grammar.

<code>
lexical-unit: lexical-elements<sub>opt</sub> 
lexical-elements: lexical-element
    lexical-element  lexical-elements 
lexical-element:
    whitespace
    token comment
</code>

At the lexical level, an M document consists of a stream of _whitespace_, _comment_, and _token_ elements. Each of these productions is covered in the following sections. Only _token_ elements are significant in the syntactic grammar.

## Whitespace

Whitespace is used to separate comments and tokens within an M document. Whitespace includes the space character (which is part of Unicode class Zs), as well as horizontal and vertical tab, form feed, and newline character sequences. Newline character sequences include carriage return, line feed, carriage return followed by line feed, next line, and paragraph separator characters.

* _whitespace_:
    Any character with Unicode class Zs 
    Horizontal tab character (`U+0009`) 
    Vertical tab character (`U+000B`) 
    Form feed character (`U+000C`) 
    Carriage return character (`U+000D`) followed by line feed character (`U+000A`)
* _new-line-character_: 
    Carriage return character (`U+000D`) 
    Line feed character (`U+000A`) 
    Next line character (`U+0085`) 
    Line separator character (`U+2028`) 
    Paragraph separator character (`U+2029`)

For compatibility with source code editing tools that add end-of-file markers, and to enable a document to be viewed as a sequence of properly terminated lines, the following transformations are applied, in order, to an M document:

* If the last character of the document is a Control-Z character (`U+001A`), this character is deleted.

* A carriage-return character (`U+000D`) is added to the end of the document if that document is non-empty and if the last character of the document is not a carriage return (`U+000D`), a line feed (`U+000A`), a line separator (`U+2028`), or a paragraph separator (`U+2029`).

## Comments

Two forms of comments are supported: single-line comments and delimited comments. _Single-line comments_ start with the characters `//` and extend to the end of the source line. _Delimited comments_ start with the characters `/*` and end with the characters `*/`.

Delimited comments may span multiple lines.

```
comment: 
single-line-comment delimited-comment single-line-comment: 
    //  single-line-comment-charactersopt single-line-comment-characters: single-line-comment-character single-line-comment-characters  single-line-comment-character 
single-line-comment-character: 
    Any Unicode character except a new-line-character delimited-comment: 
    /*  delimited-comment-textopt  asterisks  / delimited-comment-text: 
delimited-comment-section delimited-comment-text  delimited-comment-section 
delimited-comment-section: 
/ 
asterisksopt  not-slash-or-asterisk 
asterisks: 
* 
    *  asterisks not-slash-or-asterisk: 
Any Unicode character except * or / 
```

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

<em>token: identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>operator-or-punctuator</em>

### Character Escape Sequences

M text values can contain arbitrary Unicode characters. Text literals, however, are limited to graphic characters and require the use of _escape sequences_ for non-graphic characters. For example, to include a carriage-return, linefeed, or tab character in a text literal, the `#(cr)`, `#(lf)`, and `#(tab)` escape sequences can be used, respectively. To embed the escapesequence start characters `#(` in a text literal, the `#` itself needs to be escaped:

```
#(#)(
```

Escape sequences can also contain short (four hex digits) or long (eight hex digits) Unicode code-point values. The following three escape sequences are therefore equivalent:

```
#(000D)  // short Unicode hexadecimal value 
#(0000000D) // long Unicode hexadecimal value 
#(cr)   // compact escape shorthand for carriage return
```

Multiple escape codes can be included in a single escape sequence, separated by commas; the following two sequences are thus equivalent:

```
#(cr,lf) 
#(cr)#(lf)
```

The following describes the standard mechanism of character escaping in an M document.

<em>character-escape-sequence:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#(  <em>escape-sequence-list</em>  )<br/> <em>escape-sequence-list:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>single-escape-sequence single-escape-sequence  ,  escape-sequence-list</em><br/>
<em>single-escape-sequence:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>long-unicode-escape-sequence short-unicode-escape-sequence control-character-escape-sequence escape-escape</em><br/> 
<em>long-unicode-escape-sequence: hex-digit  hex-digit  hex-digit  hex-digit  hex-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digit  hex-digit  hex-digit</em><br/> 
<em>short-unicode-escape-sequence: hex-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digit  hex-digit  hex-digit</em><br/> 
<em>control-character-escape-sequence:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>control-character</em><br/> 
<em>control-character:</em>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>cr lf</code><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>tab</code><br/> 
<em>escape-escape:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>#</code>

### Literals

A _literal_ is a source code representation of a value.

<em>literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>logical-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>number-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>text-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>null-literal</em>

#### Null literals

The null literal is used to write the `null` value. The `null` value represents an absent value.

<em>null-literal</em> `null`

#### Logical literals

A logical literal is used to write the values `true` and `false` and produces a logical value.

<em>logical-literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`true false`

#### Number literals

A number literal is used to write a numeric value and produces a number value.

<em>number-literal:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-number-literal</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hexadecimal-number-literal</em><br/> 
<em>decimal-number-literal:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-digits  .  decimal-digits  exponent-part<sub>opt</sub></em>    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>.  decimal-digits  exponent-part<sub>opt</sub> decimal-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>digits  exponent-part    decimal-digits</em><br/> 
<em>decimal-digits: decimal-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>decimal-digit  decimal-digits</em><br/> 
<em>decimal-digit:</em>  one of<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9`<br/>
<em>exponent-part:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`e` <em>sign<sub>opt</sub>  decimal-digits</em> `E`<br/>
<em>sign<sub>opt</sub>  decimal-digits sign:</em><br/>
one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+  -` <em>hexadecimal-number-<br/>
literal:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0x` <em>hex-digits</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0X` <em>hex-digits hex-digits:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digit hex-digit</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>hex-digits</em><br/>
<em>hex-digit:</em>  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  a  b  c  d e  f`

A number can be specified in hexadecimal format by preceding the _hex-digits_ with the characters `0x`. For example:

```
0xff // 255
```

Note that if a decimal point is included in a number literal, then it must have at least one digit following it. For example, `1.3` is a number literal but `1.` and `1.e3` are not.

#### Text literals

A text literal is used to write a sequence of Unicode characters and produces a text value.

<em>text-literal:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>"  text-literal-characters<sub>opt</sub>  "</em><br/>
<em>text-literal-characters:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>text-literal-character text-literal-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>text-literal-characters</em><br/>
<em>text-literal-character: single-text-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character character-escape-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>sequence  double-quote-escape-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>sequence</em><br/> 
<em>single-text-character:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`) <em>double-quote-escape-sequence:</em><br/> 
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

<em>identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>regular-identifier quoted-identifier</em><br/>
<em>regular-identifier:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>available-identifier available-identifier  dot-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character  regular-identifier</em><br/>
<em>available-identifier:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <em>keyword-or-identifier</em> that is not a <em>keyword keyword-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>or-identifier: identifier-start-character  identifier-part-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;characters<sub>opt</sub></em><br/> 
<em>identifier-start-character: letter-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character underscore-character</em><br/>
<em>identifier-part-characters: identifier-part-character</em><br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>identifier-part-character  identifier-part-characters</em><br/>
<em>identifier-part-character: letter-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character decimal-digit-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>character underscore-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>connecting-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>combining-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>formatting-character</em><br/> 
<em>dot-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  (`U+002E`) <em>underscore-</em><br/>
<em>character:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`_`  (`U+005F`) <em>letter-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nl  <em>combining-character:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Mn or Mc  <em>decimal-digit-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Nd  <em>connecting-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Pc<br/> 
<em>formatting-character:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Cf

A _quoted-identifier_ can be used to allow any sequence of zero or more Unicode characters to be used as an identifier, including keywords, whitespace, comments, operators and punctuators.

<em>quoted-identifier:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#"`   <em>text-literal-characters<sub>opt</sub></em>   `"`

Note that escape sequences and double-quotes to escape quotes can be used in a _quoted identifier_, just as in a _text-literal_.

The following example uses identifier quoting for names containing a space character:

```
[ 
  #"1998 Sales" = 1000, 
  #"1999 Sales" = 1100, 
  #"Total Sales" = #"1998 Sales" + #"1999 Sales" ]
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
    Progression = Data[Base Line] * Data[Rate] ]
```

The identifiers used to name and access fields are referred to as _generalized identifiers_ and defined as follows:

<em>generalized-identifier:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-part generalized-identifier</em> separated only by blanks (`U+0020`)<br/>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-part</em><br/>
<em>generalized-identifier-part:</em><br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-segment decimal-digit-character</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>generalized-identifier-segment generalized-identifier-</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>segment:</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword-or-identifier</em><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>keyword-or-identifier  dot-character  keyword-or-identifier</em>

### Keywords

A _keyword_ is an identifier-like sequence of characters that is reserved, and cannot be used as an identifier except when using the [identifier-quoting mechanism](#identifiers) or where a [generalized identifier is allowed](#generalized-identifiers).

<em>keyword:</em>  one of `and as each else error false if in is let meta not`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`otherwise or section shared then true try type #binary #date`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#datetime`<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#datetimezone #duration #infinity #nan #sections #shared #table #time`

### Operators and punctuators

There are several kinds of operators and punctuators. Operators are used in expressions to describe operations involving one or more operands. For example, the expression `a + b` uses the `+` operator to add the two operands `a` and `b`. Punctuators are for grouping and separating.

<em>operator-or-punctuator:</em>  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`, ; = < <= > >= <> + - * / & ( ) [ ] { } @ ! ? => .. ...`

