%global tl_name mdwtools
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05.4
Release:	%{tl_revision}.1
Summary:	Miscellaneous tools by Mark Wooding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mdwtools
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This collection of tools includes: support for short commands starting
with @, macros to sanitise the OT1 encoding of the cmtt fonts; a 'do
after' command; improved footnote support; mathenv for various alignment
in maths; list handling; mdwmath which adds some minor changes to LaTeX
maths; a rewrite of LaTeX's tabular and array environments; verbatim
handling; and syntax diagrams.

