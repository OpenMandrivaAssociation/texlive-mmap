Name:		texlive-mmap
Version:	15878
Release:	2
Summary:	Include CMap resources in PDF files from PDFTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mmap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mmap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mmap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is an extension of cmap with improved flexibility
and coverage, including the ability to re-encode Knuth's basic
mathematics fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mmap/lmr-m.cmap
%{_texmfdistdir}/tex/latex/mmap/lmr.cmap
%{_texmfdistdir}/tex/latex/mmap/ly1.cmap
%{_texmfdistdir}/tex/latex/mmap/mmap.sty
%{_texmfdistdir}/tex/latex/mmap/oml-m.cmap
%{_texmfdistdir}/tex/latex/mmap/oml.cmap
%{_texmfdistdir}/tex/latex/mmap/omlbit-m.cmap
%{_texmfdistdir}/tex/latex/mmap/omlbit.cmap
%{_texmfdistdir}/tex/latex/mmap/omlmit-m.cmap
%{_texmfdistdir}/tex/latex/mmap/omlmit.cmap
%{_texmfdistdir}/tex/latex/mmap/oms-m.cmap
%{_texmfdistdir}/tex/latex/mmap/oms.cmap
%{_texmfdistdir}/tex/latex/mmap/omsb-m.cmap
%{_texmfdistdir}/tex/latex/mmap/omx-m.cmap
%{_texmfdistdir}/tex/latex/mmap/omx.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rbxit-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rbxit.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rbxn-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rbxn.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rmit-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rmit.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rmn-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1rmn.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ssbxn-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ssbxn.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ssmn-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ssmn.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ttmn-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1ttmn.cmap
%{_texmfdistdir}/tex/latex/mmap/ot1xxx-m.cmap
%{_texmfdistdir}/tex/latex/mmap/t1-m.cmap
%{_texmfdistdir}/tex/latex/mmap/t1.cmap
%{_texmfdistdir}/tex/latex/mmap/ueuf-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ueufb-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ulasy-m.cmap
%{_texmfdistdir}/tex/latex/mmap/ulasy.cmap
%{_texmfdistdir}/tex/latex/mmap/umsa-m.cmap
%{_texmfdistdir}/tex/latex/mmap/umsa.cmap
%{_texmfdistdir}/tex/latex/mmap/umsb-m.cmap
%{_texmfdistdir}/tex/latex/mmap/umsb.cmap
%{_texmfdistdir}/tex/latex/mmap/upsy-m.cmap
%{_texmfdistdir}/tex/latex/mmap/upsy.cmap
%{_texmfdistdir}/tex/latex/mmap/upzd-m.cmap
%{_texmfdistdir}/tex/latex/mmap/upzd.cmap
%doc %{_texmfdistdir}/doc/latex/mmap/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
