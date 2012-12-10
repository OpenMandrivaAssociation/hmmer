%define name		hmmer
%define version		3.0
%define rel		2
%define release		%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Profile HMMs for protein sequence analysis
Group:		Sciences/Biology
License:	GPLv3
URL:		http://hmmer.janelia.org
Source:		ftp://selab.janelia.org/pub/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch:		%{name}-3.0.makefile.patch

BuildRequires:	openmpi
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Profile hidden Markov models (profile HMMs) can be used to do sensitive
database searching using statistical descriptions of a sequence family's
consensus. HMMER is a freely distributable implementation of profile HMM
software for protein sequence analysis.

%prep
%setup -q
%patch

%build
%configure2_5x --enable-mpi
%make
%make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README INSTALL LICENSE RELEASE-NOTES Userguide.pdf
%doc documentation tutorial
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Mon Nov 29 2010 Stéphane Téletchéa <steletch@mandriva.org> 3.0-2mdv2011.0
+ Revision: 603122
- Update license version

* Mon Nov 29 2010 Stéphane Téletchéa <steletch@mandriva.org> 3.0-1mdv2011.0
+ Revision: 602714
- Update to hmmer 3.0
- Enable installation of man pages with a ugly hack
- Enable mpi version using openmpi
- Enable checks for catching regressions

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 2.3.2-6mdv2010.1
+ Revision: 519811
- rebuild

* Mon Aug 17 2009 Eric Fernandez <zeb@mandriva.org> 2.3.2-5mdv2010.0
+ Revision: 417349
- man fix and rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.3.2-4mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 2.3.2-4mdv2007.0
+ Revision: 99677
- new URL
- Import hmmer

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon,org,uk> 2.3.2-3mdv2007.0
- rebuild

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.2-2mdk
- %%mkrel
- spec cleanup

* Wed Sep 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.3.2-1mdk 
- first mdk release

