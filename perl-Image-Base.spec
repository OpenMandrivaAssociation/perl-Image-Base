%define module	Image-Base
%define name	perl-%{module}
%define version 1.07
%define release %mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Base class for loading, manipulating and saving images
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This class should not be used directly. Known inheritors are Image::Xbm and
Image::Xpm.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*

