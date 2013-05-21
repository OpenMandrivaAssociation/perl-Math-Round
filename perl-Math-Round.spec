%define upstream_name    Math-Round
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Round numbers in different ways
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Math::Round supplies functions that will round numbers in different ways.
The functions round and nearest are exported by default; others are available
as described below. "use ... qw(:all)" exports all functions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Wed Oct 14 2009 Colin Guthrie <cguthrie@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 457246
- Remove . from summary
- import perl-Math-Round

