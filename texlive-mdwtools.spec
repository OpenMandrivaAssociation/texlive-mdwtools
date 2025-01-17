Name:		texlive-mdwtools
Version:	15878
Release:	2
Summary:	Miscellaneous tools by Mark Wooding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mdwtools
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdwtools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This collection of tools includes: - support for short commands
starting with @, - macros to sanitise the OT1 encoding of the
cmtt fonts; - a 'do after' command; - improved footnote
support; - mathenv for various alignment in maths; - list
handling; - mdwmath which adds some minor changes to LaTeX
maths; - a rewrite of LaTeX's tabular and array environments; -
verbatim handling; and - syntax diagrams.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mdwtools/at.sty
%{_texmfdistdir}/tex/latex/mdwtools/cmtt.sty
%{_texmfdistdir}/tex/latex/mdwtools/doafter.sty
%{_texmfdistdir}/tex/latex/mdwtools/footnote.sty
%{_texmfdistdir}/tex/latex/mdwtools/mTTcmtt.fd
%{_texmfdistdir}/tex/latex/mdwtools/mTTenc.def
%{_texmfdistdir}/tex/latex/mdwtools/mathenv.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwlist.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwmath.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwtab.sty
%{_texmfdistdir}/tex/latex/mdwtools/sverb.sty
%{_texmfdistdir}/tex/latex/mdwtools/syntax.sty
%doc %{_texmfdistdir}/doc/latex/mdwtools/COPYING
%doc %{_texmfdistdir}/doc/latex/mdwtools/README
%doc %{_texmfdistdir}/doc/latex/mdwtools/at.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/cmtt.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/doafter.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/doafter.tex
%doc %{_texmfdistdir}/doc/latex/mdwtools/footnote.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/gpl.tex
%doc %{_texmfdistdir}/doc/latex/mdwtools/mathenv.tex
%doc %{_texmfdistdir}/doc/latex/mdwtools/mdwlist.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/mdwmath.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/mdwtab.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/mdwtools.tex
%doc %{_texmfdistdir}/doc/latex/mdwtools/sverb.pdf
%doc %{_texmfdistdir}/doc/latex/mdwtools/syntax.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mdwtools/at.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/cmtt.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/doafter.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/footnote.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/mdwlist.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/mdwmath.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/mdwtab.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/mdwtools.ins
%doc %{_texmfdistdir}/source/latex/mdwtools/sverb.dtx
%doc %{_texmfdistdir}/source/latex/mdwtools/syntax.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
