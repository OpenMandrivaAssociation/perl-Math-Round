%define upstream_name    Math-Round
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Round numbers in different ways
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Math::Round supplies functions that will round numbers in different ways.
The functions round and nearest are exported by default; others are available
as described below. "use ... qw(:all)" exports all functions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Math
%{perl_vendorlib}/auto/Math
%{_mandir}/*/*
