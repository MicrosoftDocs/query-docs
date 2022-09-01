---
title: M Language Consolidated Grammar 
description: Describes all of the grammar associated with the Power Query M formula language
ms.topic: conceptual
ms.date: 8/2/2022
---

# Consolidated Grammar

## Lexical grammar

_lexical-unit:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-elements<sub>opt</sub><br/>
lexical-elements:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lexical-element lexical-elements<sub>opt</sub><br/>
lexical-element:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;whitespace<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token comment_

### White space

_whitespace:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character with Unicode class Zs<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Horizontal tab character (`U+0009`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vertical tab character (`U+000B`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form feed character (`U+000C`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`) followed by line feed character (`U+000A`)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_new-line-character<br/>
new-line-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Carriage return character (`U+000D`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line feed character (`U+000A`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next line character (`U+0085`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Line separator character (`U+2028`)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paragraph separator character (`U+2029`)

### Comment

_comment:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-line-comment<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimited-comment</em><br/> 
single-line-comment:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`//`  _single-line-comment-characters<sub>opt</sub><br/>
single-line-comment-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-line-comment-character  single-line-comment-characters<sub>opt</sub><br/> 
single-line-comment-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except a _new-line-character<br/>
delimited-comment:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/*` _delimited-comment-text<sub>opt</sub>  asterisks_  `/`<br/>
_delimited-comment-text:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delimited-comment-section delimited-comment-text<sub>opt</sub><br/>
delimited-comment-section:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`/`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_asterisks<sub>opt</sub>  not-slash-or-asterisk<br/> 
asterisks:_ <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`*` _asterisks<sub>opt</sub><br/> 
not-slash-or-asterisk:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any Unicode character except `*` or `/`

### Tokens

_token:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operator-or-punctuator_

### Character escape sequences

_character-escape-sequence:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#(`  _escape-sequence-list_  `)`<br/>
_escape-sequence-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;escape-sequence-list_  `,`  _single-escape-sequence<br/>
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

_literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;null-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;verbatim-literal<br/>
logical-literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`true`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`false`<br/>
number-literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-number-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hexadecimal-number-literal<br/>
decimal-digits:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit decimal-digits<sub>opt</sub><br/>
decimal-digit:_  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9`<br/>
_hexadecimal-number-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0x`  _hex-digits_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0X`  _hex-digits<br/>
hex-digits:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex-digit hex-digits<sub>opt</sub><br/>
hex-digit:_  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  a  b  c  d e  f`<br/>
_decimal-number-literal:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digits_  `.`  _decimal-digits  exponent-part<sub>opt</sub>_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  _decimal-digits  exponent-part<sub>opt</sub><br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digits  exponent-part<sub>opt</sub><br/>
exponent-part:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`e`  _sign<sub>opt</sub>  decimal-digits_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`E`  _sign<sub>opt</sub>  decimal-digits<br/> sign:_  one of<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+  -`<br/>
_text-literal:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"`  _text-literal-characters<sub>opt</sub>_  `"`<br/>
_text-literal-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal-character  text-literal-characters<sub>opt</sub><br/>
text-literal-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single-text-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;character-escape-sequence<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;double-quote-escape-sequence<br/>
single-text-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any character except `"` (`U+0022`) or `#` (`U+0023`) followed by `(` (`U+0028`)<br/>
_double-quote-escape-sequence:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`""` (`U+0022`, `U+0022`)<br/>
_null-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`null`<br/>
_verbatim-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#!"` _text-literal-characters<sub>opt</sub>_ `"`

### Identifiers

_identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regular-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quoted-identifier<br/>
regular-identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;available-identifier  dot-character  regular-identifier<br/>
available-identifier:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A _keyword-or-identifier_ that is not a _keyword<br/>
keyword-or-identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underscore-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-start-character 
identifier-part-characters<br/>
identifier-start-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underscore-character<br/>
identifier-part-characters:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-part-character  identifier-part-characters<sub>opt</sub><br/>
identifier-part-character:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;letter-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underscore-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connecting-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;combining-character<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;formatting-character<br/>
generalized-identifier:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier-part<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier_ separated only by blanks (`U+0020`) _generalized-identifier-part<br/>
generalized-identifier-part:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier-segment<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decimal-digit-character generalized-identifier-segment<br/>
generalized-identifier-segment:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword-or-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keyword-or-identifier dot-character  keyword-or-identifier<br/>
dot-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.`  (`U+002E`)<br/>
_underscore-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`_`  (`U+005F`)<br/>
letter-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Lu, Ll, Lt, Lm, Lo, or Nl<br/>
_combining-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of classes Mn or Mc<br/>
_decimal-digit-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Nd<br/>
_connecting-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Pc<br/>
_formatting-character:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Unicode character of the class Cf<br/>
_quoted-identifier:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#"`  _text-literal-characters<sub>opt</sub>_  `"`

### Keywords and predefined identifiers

Predefined identifiers and keywords cannot be redefined. A quoted identifier can be used to handle identifiers that would otherwise collide with predefined identifiers or keywords.

_keyword:_  one of</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`and as each else error false if in is let meta not null or otherwise`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`section shared then true try type #binary #date #datetime`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`#datetimezone #duration #infinity #nan #sections #shared #table #time`

### Operators and punctuators

_operator-or-punctuator:_  one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`, ; = < <= > >= <> + - * / & ( ) [ ] { } @ ? ?? => .. ...`

## Syntactic grammar

### Documents

_document:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section-document<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression-document_

### Section Documents

_section-document:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section<br/>
section:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-attributes<sub>opt</sub>_  `section`  _section-name_  `;`  _section-members<sub>opt</sub><br/>
section-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
section-members:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section-member section-members<sub>opt</sub><br/>
section-member:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-attributes<sub>opt</sub>  shared<sub>opt</sub>  section-member-name_  `=`  _expression_  `;`<br/>
_section-member-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_

### Expression Documents

#### Expressions

_expression-document:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-or-expression</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;each-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;let-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;error-raising-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;error-handling-expression_

#### Logical expressions

_logical-or-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-and-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-and-expression_  `or`  _logical-or-expression<br/>
logical-and-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-and-expression_  `and`  _is-expression_

#### Is expression

_is-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is-expression_ `is`  _nullable-primitive-type<br/>
nullable-primitive-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nullable`_<sub>opt</sub>  primitive-type_

#### As expression

_as-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;equality-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as-expression_  `as`  _nullable-primitive-type_

#### Equality expression

_equality-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression_  `=`  _equality-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;relational-expression_  `<>`  _equality-expression_

#### Relational expression

_relational-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `<`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `>`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `<=`  _relational-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additive-expression_  `>=`  _relational-expression_

#### Arithmetic expressions

_additive-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression_  `+`  _additive-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression_  `-`  _additive-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplicative-expression_  `&`  _additive-expression<br/>
_multiplicative-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metadata-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metadata-expression_  `*`  _multiplicative-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metadata-expression_  `/`  _multiplicative-expression_

#### Metadata expression

_metadata-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unary-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unary-expression_  `meta`  _unary-expression_

#### Unary expression

_unary-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type-expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`+`  _unary-expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-`  _unary-expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`not`  _unary-expression_

#### Primary expression

_primary-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;section-access-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parenthesized-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-access-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item-access-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;invoke-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;not-implemented-expression_

#### Literal expression

_literal-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal_

#### Identifier expression

_identifier-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier-reference<br/>
identifier-reference:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclusive-identifier-reference<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inclusive-identifier-reference<br/> 
exclusive-identifier-reference:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
inclusive-identifier-reference:_<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`@`  _identifier_

#### Section-access expression

_section-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_ `!` _identifier_

#### Parenthesized expression

_parenthesized-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  _expression_  `)`

#### Not-implemented expression

_not-implemented-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`...`

#### Invoke expression

_invoke-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_  `(`  _argument-list<sub>opt</sub>_  `)`<br/>
_argument-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_  `,`   _argument-list_

#### List expression

_list-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{`  _item-list<sub>opt</sub>_  `}`<br/>
_item-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item_  `,`  _item-list<br/>
item:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_  `..`  _expression_

#### Record expression

_record-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`  _field-list<sub>opt<sub>_  `]`<br/>
_field-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field_  `,`  _field-list<br/>
field:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-name_  `=`  _expression<br/>
field-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quoted-identifier_<br/>

#### Item access expression

_item-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;item-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-item-selection<br/>
item-selection:</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_  `{`  _item-selector_  `}`<br/>
_optional-item-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_  `{`  _item-selector_  `} ?`<br/>
_item-selector:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_

#### Field access expressions

_field-access-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;implicit-target-field-selection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;projection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;implicit-target-projection<br/>
field-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression  field-selector<br/>
field-selector:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-field-selector<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-field-selector<br/>
required-field-selector:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-name_  `]`<br/>
_optional-field-selector:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-name_  `] ?`<br/>
_field-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generalized-identifier<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quoted-identifier<br/>
implicit-target-field-selection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-selector<br/>
projection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression  required-projection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression  optional-projection<br/>
required-projection:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` _required-selector-list_ `]`<br/>
_optional-projection:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` _required-selector-list_ `] ?`<br/>
_required-selector-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-field-selector<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-field-selector_ `,`  _required-selector-list<br/>
implicit-target-projection:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-projection<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-projection_

#### Function expression

_function-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(`  _parameter-list<sub>opt</sub>_  `)`  _return-type<sub>opt</sub>_  `=>`  _function-body<br/>
function-body:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed-parameter-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed-parameter-list_  `,`  _optional-parameter-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter-list<br/>
fixed-parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter_  `,`  _fixed-parameter-list<br/>
parameter:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter-name  parameter-type<sub>opt</sub><br/>
parameter-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier<br/>
parameter-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertion<br/>
return-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assertion<br/>
assertion:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`as`  _nullable-primitive-type<br/>
optional-parameter-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter_  `,`  _optional-parameter-list<br/>
optional-parameter:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional`  _parameter_

#### Each expression

_each-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`each` _each-expression-body<br/>
each-expression-body:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function-body_

#### Let expression

_let-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`let`  _variable-list_  `in`  _expression<br/>
variable-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable_  `,`  _variable-list<br/>
variable:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variable-name_  `=`  _expression<br/>
variable-name:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier_

#### If expression

_if-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if` _if-condition_  `then`  _true-expression_  `else`  _false-expression<br/>
if-condition:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/> 
true-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
false-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_

#### Type expression

_type-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-expression_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`type`  _primary-type<br/>
type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parenthesized-expression<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary-type<br/>
primary-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primitive-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;table-type<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nullable-type<br/>
primitive-type:_ one of<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`any anynonnull binary date datetime datetimezone duration function`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`list logical none null number record table text time type`<br/> 
_record-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`  _open-record-marker_  `]`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-specification-list<sub>opt</sub>_  `]`<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-specification-list_  `,`  _open-record-marker_  `]` <br/>
_field-specification-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-specification<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-specification_
  `,`  _field-specification-list<br/>
field-specification:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional`_<sub>opt</sub> field-name field-type-specification<sub>opt</sub><br/>
field-type-specification:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`=` _field-type<br/>
field-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type<br/>
open-record-marker:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`...`<br/>
_list-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{`   _item-type_   `}`<br/>
_item-type:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type<br/>
function-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`function (`  _parameter-specification-listopt_  `)`  _return-type<br/>
parameter-specification-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-parameter-specification-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-parameter-specification-list_  `,`  _optional-parameter-specification-list<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter-specification-list<br/>
required-parameter-specification-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-parameter-specification<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;required-parameter-specification_  `,`  _required-parameter-specification-list<br/>
required-parameter-specification:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter-specification<br/>
optional-parameter-specification-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter-specification<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optional-parameter-specification_  `,`  _optional-parameter-specification-list<br/>
optional-parameter-specification:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`optional` _parameter-specification<br/> 
parameter-specification:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter-name  parameter-type<br/>
table-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`table`  _row-type<br/>
row-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[`   _field-specification-list_<sub>opt</sub>  `]`<br/>
_nullable-type:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nullable`  _type_

#### Error raising expression

_error-raising-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`error`  expression_

#### Error handling expression

_error-handling-expression:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`try` _protected-expression otherwise-clause<sub>opt</sub><br/>
protected-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression<br/>
otherwise-clause:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`otherwise` _default-expression<br/>
default-expression:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expression_

### Literal Attributes

_literal-attributes:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record-literal<br/>
record-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[` _literal-field-list<sub>opt</sub>_ `]`<br/>
_literal-field-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-field<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;literal-field_ `,` _literal-field-list<br/>
literal-field:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field-name_ `=` _any-literal<br/>
list-literal:_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`{` _literal-item-list<sub>opt</sub>_ `}`<br/>
_literal-item-list:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any-literal_ `,` _literal-item-list<br/>
any-literal:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logical-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text-literal<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;null-literal_
