#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : UCD
Version  : 1
Release  : 3
URL      : https://www.unicode.org/Public/zipped/12.1.0/UCD.zip
Source0  : https://www.unicode.org/Public/zipped/12.1.0/UCD.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: UCD-data = %{version}-%{release}
Patch1: build.patch

%description
No detailed description available

%package data
Summary: data components for the UCD package.
Group: Data

%description data
data components for the UCD package.


%prep
%setup -q -n auxiliary
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559114854
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1559114854
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/unicode/ucd/ArabicShaping.txt
/usr/share/unicode/ucd/BidiBrackets.txt
/usr/share/unicode/ucd/BidiCharacterTest.txt
/usr/share/unicode/ucd/BidiMirroring.txt
/usr/share/unicode/ucd/BidiTest.txt
/usr/share/unicode/ucd/Blocks.txt
/usr/share/unicode/ucd/CJKRadicals.txt
/usr/share/unicode/ucd/CaseFolding.txt
/usr/share/unicode/ucd/CompositionExclusions.txt
/usr/share/unicode/ucd/DerivedAge.txt
/usr/share/unicode/ucd/DerivedCoreProperties.txt
/usr/share/unicode/ucd/DerivedNormalizationProps.txt
/usr/share/unicode/ucd/EastAsianWidth.txt
/usr/share/unicode/ucd/EmojiSources.txt
/usr/share/unicode/ucd/EquivalentUnifiedIdeograph.txt
/usr/share/unicode/ucd/HangulSyllableType.txt
/usr/share/unicode/ucd/Index.txt
/usr/share/unicode/ucd/IndicPositionalCategory.txt
/usr/share/unicode/ucd/IndicSyllabicCategory.txt
/usr/share/unicode/ucd/Jamo.txt
/usr/share/unicode/ucd/LineBreak.txt
/usr/share/unicode/ucd/NameAliases.txt
/usr/share/unicode/ucd/NamedSequences.txt
/usr/share/unicode/ucd/NamedSequencesProv.txt
/usr/share/unicode/ucd/NamesList.html
/usr/share/unicode/ucd/NamesList.txt
/usr/share/unicode/ucd/NormalizationCorrections.txt
/usr/share/unicode/ucd/NormalizationTest.txt
/usr/share/unicode/ucd/NushuSources.txt
/usr/share/unicode/ucd/PropList.txt
/usr/share/unicode/ucd/PropertyAliases.txt
/usr/share/unicode/ucd/PropertyValueAliases.txt
/usr/share/unicode/ucd/ReadMe.txt
/usr/share/unicode/ucd/ScriptExtensions.txt
/usr/share/unicode/ucd/Scripts.txt
/usr/share/unicode/ucd/SpecialCasing.txt
/usr/share/unicode/ucd/StandardizedVariants.txt
/usr/share/unicode/ucd/TangutSources.txt
/usr/share/unicode/ucd/USourceData.txt
/usr/share/unicode/ucd/USourceGlyphs.pdf
/usr/share/unicode/ucd/USourceRSChart.pdf
/usr/share/unicode/ucd/UnicodeData.txt
/usr/share/unicode/ucd/VerticalOrientation.txt
/usr/share/unicode/ucd/auxiliary/GraphemeBreakProperty.txt
/usr/share/unicode/ucd/auxiliary/GraphemeBreakTest.html
/usr/share/unicode/ucd/auxiliary/GraphemeBreakTest.txt
/usr/share/unicode/ucd/auxiliary/LineBreakTest.html
/usr/share/unicode/ucd/auxiliary/LineBreakTest.txt
/usr/share/unicode/ucd/auxiliary/Makefile
/usr/share/unicode/ucd/auxiliary/SentenceBreakProperty.txt
/usr/share/unicode/ucd/auxiliary/SentenceBreakTest.html
/usr/share/unicode/ucd/auxiliary/SentenceBreakTest.txt
/usr/share/unicode/ucd/auxiliary/WordBreakProperty.txt
/usr/share/unicode/ucd/auxiliary/WordBreakTest.html
/usr/share/unicode/ucd/auxiliary/WordBreakTest.txt
/usr/share/unicode/ucd/extracted/DerivedBidiClass.txt
/usr/share/unicode/ucd/extracted/DerivedBinaryProperties.txt
/usr/share/unicode/ucd/extracted/DerivedCombiningClass.txt
/usr/share/unicode/ucd/extracted/DerivedDecompositionType.txt
/usr/share/unicode/ucd/extracted/DerivedEastAsianWidth.txt
/usr/share/unicode/ucd/extracted/DerivedGeneralCategory.txt
/usr/share/unicode/ucd/extracted/DerivedJoiningGroup.txt
/usr/share/unicode/ucd/extracted/DerivedJoiningType.txt
/usr/share/unicode/ucd/extracted/DerivedLineBreak.txt
/usr/share/unicode/ucd/extracted/DerivedName.txt
/usr/share/unicode/ucd/extracted/DerivedNumericType.txt
/usr/share/unicode/ucd/extracted/DerivedNumericValues.txt
