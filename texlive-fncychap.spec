# revision 20710
# category Package
# catalog-ctan /macros/latex/contrib/fncychap
# catalog-date 2010-12-10 10:22:28 +0100
# catalog-license lppl1.3
# catalog-version v1.34
Name:		texlive-fncychap
Version:	v1.34
Release:	1
Summary:	Seven predefined chapter heading styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fncychap
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncychap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Each style can be modified using a set of simple commands.
Optionally one can modify the formatting routines in order to
create additional chapter headings. This package was previously
known as FancyChapter.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fncychap/fncychap.sty
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjarne.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjarnes.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Bjornstrup.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/BjornstrupS.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Conny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Connys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Glenn.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Glenns.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Lenny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Lennys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/README
%doc %{_texmfdistdir}/doc/latex/fncychap/Rejne.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Rejnes.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Sonny.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/Sonnys.eps
%doc %{_texmfdistdir}/doc/latex/fncychap/fncychap.pdf
%doc %{_texmfdistdir}/doc/latex/fncychap/fncychap.tex
%doc %{_texmfdistdir}/doc/latex/fncychap/manifest.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
