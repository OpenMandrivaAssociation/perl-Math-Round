%define modname	Math-Round
%define modver	0.06

Summary:	Round numbers in different ways
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Math/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Math::Round supplies functions that will round numbers in different ways.
The functions round and nearest are exported by default; others are available
as described below. "use ... qw(:all)" exports all functions.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{perl_vendorlib}/auto/Math
%{_mandir}/man3/*

