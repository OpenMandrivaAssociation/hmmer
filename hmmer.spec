%define name		hmmer
%define version		3.0
%define rel		1
%define release		%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Profile HMMs for protein sequence analysis
Group:		Sciences/Biology
License:	GPL
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
