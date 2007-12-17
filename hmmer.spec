%define name		hmmer
%define version		2.3.2
%define rel		4
%define release		%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Profile HMMs for protein sequence analysis
Group:		Sciences/Biology
License:	GPL
URL:		http://hmmer.janelia.org
Source:		ftp://selab.janelia.org/pub/software/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch:		%{name}-2.3.2.makefile.patch

%description
Profile hidden Markov models (profile HMMs) can be used to do sensitive
database searching using statistical descriptions of a sequence family's
consensus. HMMER is a freely distributable implementation of profile HMM
software for protein sequence analysis.

%prep
%setup -q
%patch

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc 00README COPYRIGHT INSTALL NOTES LICENSE Userguide.pdf
%doc documentation tutorial
%{_bindir}/*
%{_mandir}/man1/*


